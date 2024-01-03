# PICO-Remote-Power
Remotely Power on and off your computer with a Raspberry PI Pico

## Requirements
- Raspberry Pi Pico W
- 2 jumper cables
- USB Micro C cable

## Python Instructions
- Download the python code provided (connection.py, main.py, startup.py)
- Open Thonny and create 3 files with the same names and copy contents
- Insert your ssid and pwd in connection.py
- Run the connection.py and check for connection and IPV4 address (Save this address)

## PICO Board Instructions
- Solder a resistor to an LED on one leg
- In GP2 solder the LED with the resistor
- In GND (above GP2) solder the other leg
- In GP4 solder a jumper cable
- In GP6 solder a jumper cable
- In GND (above GP10) solder a jumper cable

![uXQ-tEmN](https://github.com/trycehuffman/PICO-Remote-Power/assets/45830492/f81abb6b-9e1b-4290-833b-2c32e74e3813)

## PC Setup
- On the PW Button + place the GP6 cable
- On the PW Button - place the GND cable
- On the PW LED + place the GP4 cable
- In Computer BIOS make sure USB power is always on
- Plug in USB Micro C cable into PC and run it into case

## Website
- Visit the ip of your device example -> http://10.0.0.15

## Use outside of your local LAN
- Visit cloudflare zero trust center and setup a tunnel (Requires a computer/server that is always powered on)

## Use with Apple Products
- Open Shortcuts App
- Create a new shortcut called Turn Computer On
- Add an action called Get Contents of URL
- In the URL field insert http://10.0.0.15/led_on where 10.0.0.15 is your device IP
- Create a new shortcut called Turn Computer Off
- Add an action called Get Contents of URL
- In the URL field insert http://10.0.0.15/led_off where 10.0.0.15 is your device IP
