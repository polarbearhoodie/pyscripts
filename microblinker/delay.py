import time
from machine import Pin
import _thread

CLOCKS = [pc.blinker(0, 0, 0), pc.blinker(0, 0, 0), pc.blinker(0, 0, 0)]
LEDS = [Pin('LED', Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT)]


def myDelay():
    global CLOCKS
    global LEDS
    while True:
        start = time.ticks_ms()

        for i in range(3):
            CLOCKS[i].tickDown()
            if CLOCKS[i].state():
                LEDS[i].on()
            else:
                LEDS[i].off()

        diff = time.ticks_diff(start, time.ticks_ms())/1000
        time.sleep(0.01 - diff)
