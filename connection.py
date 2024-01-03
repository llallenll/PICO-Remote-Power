try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network
import utime
from startup import timer

led1 = Pin("LED", Pin.OUT)

import gc
gc.collect()

#---------------------------CHANGE THIS--------------------------------------

ssid = 'ssid'
password = 'pwd'

#----------------------------------------------------------------------------

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())
led1.on()
timer.deinit()

led = Pin(2, Pin.OUT)
computer = Pin(6, Pin.OUT)

def web_page():
    html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        .button {
            background-color: #ce1b0e;
            border: none;
            color: white;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }

        .button1 {
            background-color: #000000;
        }
    </style>
</head>

<body>
    <h2>Raspberry Pi Pico Remote Computer Power Switch</h2>
    <p>Computer state: <strong>""" + computer_state + """</strong></p>
    <p>
        <i class="fas fa-lightbulb fa-3x" style="color:#c81919;"></i>
        <a href=\"led_on\"><button class="button">Computer ON/OFF</button></a>
    </p>
</body>

</html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
    try:
        on_detect = Pin(4, Pin.IN)
        if on_detect.value() == 1:
            print("--------------------DETECTED-------------------------")
            computer_state = "ON"
            web_page()
        elif on_detect.value() == 0:
            computer_state = "OFF"
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Rquest Content = %s' % request)
        led_on = request.find('/led_on')
        led_off = request.find('/led_off')
        if led_on == 6:
            print('----------------COMPUTER POWER BUTTON----------------')
            led.on()
            computer.on()
            utime.sleep(2)
            led.off()
            computer.off()
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')