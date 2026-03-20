from machine import Pin
import network
import socket
import time
import dht
import secrets
import ntptime
from blynklib import Blynk

# ----------------------------
# Hardware setup
# ----------------------------
led = Pin("LED", Pin.OUT)
led.off()

sensor1 = dht.DHT11(Pin(15))

# ----------------------------
# Wi-Fi
# ----------------------------
def connect_to_internet(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    max_wait = 15
    while max_wait > 0:
        status = wlan.status()
        if status < 0 or status >= 3:
            break
        max_wait -= 1
        time.sleep(1)

    if wlan.status() != 3:
        print("Wi-Fi status:", wlan.status())
        raise RuntimeError("network connection failed")

    ip = wlan.ifconfig()[0]
    led.on()
    print("Connected to Wi-Fi")
    print("IP address:", ip)
    return wlan, ip

# ----------------------------
# Time helpers (UTC)
# ----------------------------
def sync_time():
    try:
        ntptime.settime()
        print("Time synchronised with NTP (UTC)")
    except Exception as e:
        print("NTP sync failed:", e)

def get_timestamp_utc():
    t = time.localtime()
    return "{:04}-{:02}-{:02} {:02}:{:02}:{:02}".format(
        t[0], t[1], t[2], t[3], t[4], t[5]
    )

# ----------------------------
# CSV helpers
# ----------------------------
CSV_FILE = "data.csv"
MAX_ROWS = 1000  # stop the file growing forever

def ensure_csv_exists():
    try:
        with open(CSV_FILE, "r") as f:
            first_line = f.readline()
            if "timestamp_utc,temperature,humidity" not in first_line:
                raise OSError
    except OSError:
        with open(CSV_FILE, "w") as f:
            f.write("timestamp_utc,temperature,humidity\n")

def trim_csv_if_needed():
    rows = []
    try:
        with open(CSV_FILE, "r") as f:
            rows = f.readlines()
    except OSError:
        return

    if len(rows) <= MAX_ROWS + 1:
        return

    header = rows[0]
    data_rows = rows[-MAX_ROWS:]
    with open(CSV_FILE, "w") as f:
        f.write(header)
        for row in data_rows:
            f.write(row)

def append_reading(timestamp_str, temp, hum):
    with open(CSV_FILE, "a") as f:
        f.write("{},{},{}\n".format(timestamp_str, temp, hum))

# ----------------------------
# Web pages
# ----------------------------
latest_temp = None
latest_hum = None
latest_timestamp = "No data yet"

def webpage():
    temp_text = "N/A" if latest_temp is None else str(latest_temp)
    hum_text = "N/A" if latest_hum is None else str(latest_hum)

    html = """<!DOCTYPE html>
<html>
<head>
    <title>Pico W Sensor Logger</title>
    <meta http-equiv="refresh" content="10">
</head>
<body>
    <h1>Pico W Sensor Logger</h1>
    <p><strong>Latest UTC timestamp:</strong> {}</p>
    <p><strong>Temperature:</strong> {} C</p>
    <p><strong>Humidity:</strong> {} %</p>
    <p><a href="/data.csv">Download CSV</a></p>
</body>
</html>
""".format(latest_timestamp, temp_text, hum_text)
    return html

def send_response(client, content, content_type="text/html"):
    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: {}\r\n".format(content_type))
    client.send("Connection: close\r\n\r\n")
    client.send(content)

def serve_csv(client):
    client.send("HTTP/1.1 200 OK\r\n")
    client.send("Content-Type: text/csv\r\n")
    client.send("Connection: close\r\n\r\n")

    with open(CSV_FILE, "r") as f:
        while True:
            line = f.readline()
            if not line:
                break
            client.send(line)

def serve_not_found(client):
    client.send("HTTP/1.1 404 Not Found\r\n")
    client.send("Content-Type: text/plain\r\n")
    client.send("Connection: close\r\n\r\n")
    client.send("404 Not Found")

def open_socket(ip):
    addr = socket.getaddrinfo(ip, 80)[0][-1]
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(1)
    s.settimeout(0.2)
    print("Web server running at http://{}/".format(ip))
    return s

def handle_http_request(server):
    try:
        client, addr = server.accept()
    except OSError:
        return

    try:
        request = client.recv(1024)
        if not request:
            client.close()
            return

        request_str = request.decode("utf-8", "ignore")
        request_line = request_str.split("\r\n")[0]
        print("HTTP request:", request_line)

        if "GET /data.csv " in request_line:
            serve_csv(client)
        elif "GET / " in request_line:
            send_response(client, webpage(), "text/html")
        else:
            serve_not_found(client)

    except Exception as e:
        print("HTTP error:", e)
    finally:
        client.close()

# ----------------------------
# Main
# ----------------------------
wlan, ip = connect_to_internet(secrets.SSID, secrets.PASSWORD)
sync_time()
blynk = Blynk(secrets.BLYNK_AUTH_TOKEN)

ensure_csv_exists()
server = open_socket(ip)

last_read_time = 0
read_interval = 60  # seconds

while True:
    now = time.time()

    try:
        blynk.run()
    except Exception as e:
        print("Blynk error:", e)

    handle_http_request(server)

    if now - last_read_time >= read_interval:
        last_read_time = now

        try:
            sensor1.measure()
            temp1 = sensor1.temperature()
            hum1 = sensor1.humidity()

            latest_temp = temp1
            latest_hum = hum1
            latest_timestamp = get_timestamp_utc()

            append_reading(latest_timestamp, temp1, hum1)
            trim_csv_if_needed()

            print("UTC Timestamp:", latest_timestamp)
            print("Temperature: {} C".format(temp1))
            print("Humidity: {} %".format(hum1))

            try:
                blynk.virtual_write(7, temp1)
                blynk.virtual_write(8, hum1)
            except Exception as e:
                print("Blynk write error:", e)

        except OSError:
            print("Failed to read sensor")

    time.sleep(0.05)