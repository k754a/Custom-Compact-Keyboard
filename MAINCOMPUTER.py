from machine import Pin
import time
import board
import digitalio
import time
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

pin0 = Pin(0, Pin.IN, Pin.PULL_DOWN)
pin1 = Pin(1, Pin.IN, Pin.PULL_DOWN)
pin2 = Pin(3, Pin.IN, Pin.PULL_DOWN)
pin3 = Pin(4, Pin.IN, Pin.PULL_DOWN)
pin4 = Pin(6, Pin.IN, Pin.PULL_DOWN)
pin5 = Pin(7, Pin.IN, Pin.PULL_DOWN)
pin6 = Pin(8, Pin.IN, Pin.PULL_DOWN)
pin7 = Pin(5, Pin.IN, Pin.PULL_DOWN)
pin8 = Pin(2, Pin.IN, Pin.PULL_DOWN)



pins = [pin0, pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8]


debounce_time = 0.1  #
last_pressed_time = [0] * len(pins)

while True:
     if pin0.value() == 1:
         #pin0
         
     if pin1.value() == 1:
         #pin1
        
     if pin2.value() == 1:
         #pin2
         
     if pin3.value() == 1:
         #pin3
        
     if pin4.value() == 1:
         #pin4
         
     if pin5.value() == 1:
         #pin5
        
     if pin6.value() == 1:
         #pin6
         
     if pin7.value() == 1:
         #pin7
        
     if pin8.value() == 1:
         #pin8