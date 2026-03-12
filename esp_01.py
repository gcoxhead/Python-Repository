from machine import UART, Pin
import time

# Initialize UART (TX=GP17, RX=GP16)

uart = UART(0,baudrate = 115200,bits = 8,parity = None,stop = 1 ,tx = Pin(16),rx = Pin(17))
while True:
    # Send data to ESP01
    uart.write("AT\r\n")  # Test command to check ESP01 response
    time.sleep(1)
    
    # Check if data is available from ESP01
    if uart.any():
        response = uart.read()
        print("Received from ESP01: ", response)
