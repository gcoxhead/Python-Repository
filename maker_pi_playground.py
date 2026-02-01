from machine import Pin
from time import sleep
import dht

# sensor = dht.DHT22(Pin(27))
sensor = dht.DHT11(Pin(27))

reading_number = 0
seconds_elapsed = 0

def print_sensor_readings(reading_number, seconds_elapsed):
    temp = sensor.temperature()
    hum = sensor.humidity()
    
    print("Time elapsed: " + format_time(seconds_elapsed))
    
    print(f"Reading number:  {reading_number}")
    print('Temperature: %3.1f C' %temp)
#   print('Temperature: %3.1f F' %temp_f)
    print('Humidity: %3.1f %%\n' %hum)
#   temp_f = temp * (9/5) + 32.0
    
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"   

while True:
  try:
    sleep(2)
    seconds_elapsed+=2
    sensor.measure()
    reading_number+=1
    
    print_sensor_readings(reading_number, seconds_elapsed)
    
  except OSError as e:
    print('Failed to read sensor.')