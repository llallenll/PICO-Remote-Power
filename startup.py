from machine import Pin, Timer
import utime

print("------------------------------------")
print("          REMOTE PC BOOTER          ")
print("          CREATED BY ALLEN          ")
print("               1.0.0                ")
print("------------------------------------")

utime.sleep(2)

print("System Starting")

led1 = Pin("LED", Pin.OUT)
timer = Timer()

def blink(timer):
    led1.toggle()

timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

utime.sleep(2)