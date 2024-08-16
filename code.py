import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

pin_map = {
    0: board.GP0,  
    1: board.GP3,  
    2: board.GP4,  
    3: board.GP6,  
    4: board.GP7,  
    5: board.GP8,  
    6: board.GP5,  
    7: board.GP2,  
    8: board.GP1,  
}
11299

keycodes = {
    0: Keycode.ONE,   
    1: Keycode.THREE,   
    2: Keycode.FOUR, 
    3: Keycode.FIVE,  
    4: Keycode.SIX,  
    5: Keycode.SEVEN,   
    6: Keycode.EIGHT, 
    7: Keycode.NINE, 
    8: Keycode.TWO,  
}

pins = {}
for i in range(9):  
    pins[i] = digitalio.DigitalInOut(pin_map[i])
    pins[i].direction = digitalio.Direction.INPUT
    pins[i].pull = digitalio.Pull.DOWN  

def send_key(keycode, delay=0.1):
    keyboard.press(keycode)
    time.sleep(delay)
    keyboard.release_all()

while True:
    for i in range(9):  
        if pins[i].value:  
            send_key(keycodes[i])
            time.sleep(0.5)  
    time.sleep(0.1)  
