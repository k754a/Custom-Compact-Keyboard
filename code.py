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

def repeat_keypress(pin_index):
    keycode = keycodes[pin_index]
    initial_delay = 1.0  
    repeat_delay = 0.1  

    keyboard.press(keycode)
    start_time = time.monotonic()

    while pins[pin_index].value:
        if time.monotonic() - start_time > initial_delay:
            keyboard.release(keycode)
            time.sleep(repeat_delay)
            keyboard.press(keycode)

    keyboard.release_all()  

while True:
    if pins[0].value:  
        repeat_keypress(0)

    if pins[1].value:  
        repeat_keypress(1)

    if pins[2].value:  
        repeat_keypress(2)

    if pins[3].value:  
        repeat_keypress(3)

    if pins[4].value:  
        repeat_keypress(4)

    if pins[5].value:  
        repeat_keypress(5)

    if pins[6].value:  
        repeat_keypress(6)

    if pins[7].value:  
        repeat_keypress(7)

    if pins[8].value:  
        repeat_keypress(8)

    time.sleep(0.01)  