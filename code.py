import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)

pin_map = {
    0: board.GP0,  
    1: board.GP1,  
    2: board.GP2,  
    3: board.GP3,  
    4: board.GP4,  
    5: board.GP5,  
    6: board.GP6,  
    7: board.GP7,  
    8: board.GP8,  
}

last_press_time = {i: 0 for i in range(9)}
debounce_delay = 0.1  
button_state = {i: False for i in range(9)}  

def key_action_0():
    print("Ending script...")
    while True:
        pass  

def type_text(text):
    """Helper function to type text as quickly as possible."""
    for char in text:
        if char == ':':
            keyboard.press(Keycode.SHIFT)
            keyboard.press(Keycode.SEMICOLON)
            keyboard.release_all()
        elif char == '!':
            keyboard.press(Keycode.SHIFT)
            keyboard.press(Keycode.ONE)
            keyboard.release_all()
        elif char == '/':
            keyboard.press(Keycode.SLASH)  
            keyboard.release_all()
        elif char == '.':
            keyboard.press(Keycode.PERIOD)
            keyboard.release_all()
        elif char == '\\':
            keyboard.press(Keycode.BACKSLASH)
            keyboard.release_all()
        elif char == '_':
            keyboard.press(Keycode.SHIFT)
            keyboard.press(Keycode.MINUS)
            keyboard.release_all()
        elif char.isupper():
            keyboard.press(Keycode.SHIFT)
            keyboard.press(getattr(Keycode, f"{char}"))
            keyboard.release_all()
            keyboard.release(Keycode.SHIFT)
        elif char.islower():
            keyboard.press(getattr(Keycode, f"{char.upper()}"))
            keyboard.release_all()
        elif char == ' ':
            keyboard.press(Keycode.SPACE)
            keyboard.release_all()
        else:
            pass

def key_action_1():
    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.2)  
    type_text("code")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_2():
    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.2)  
    type_text("devenv")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_3():
    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.2)  
    type_text("notepad")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_4():
    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.2)  
    type_text("cmd")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_5():
    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.2)  
    type_text("powershell")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_6():
    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.2)  
    type_text("explorer")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_7():
    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.2)  
    type_text("mspaint")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_8():
    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.2)  
    type_text("control")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

pins = {}
for i in range(9):  
    pins[i] = digitalio.DigitalInOut(pin_map[i])
    pins[i].direction = digitalio.Direction.INPUT
    pins[i].pull = digitalio.Pull.DOWN  

while True:
    current_time = time.monotonic()
    for i in range(9):
        if pins[i].value:
            if not button_state[i]:  

                button_state[i] = True
                if (current_time - last_press_time[i]) > debounce_delay:
                    if i == 0:
                        key_action_0()
                    elif i == 1:
                        key_action_1()
                    elif i == 2:
                        key_action_2()
                    elif i == 3:
                        key_action_3()
                    elif i == 4:
                        key_action_4()
                    elif i == 5:
                        key_action_5()
                    elif i == 6:
                        key_action_6()
                    elif i == 7:
                        key_action_7()
                    elif i == 8:
                        key_action_8()

                    last_press_time[i] = current_time
        else:
            if button_state[i]:  

                button_state[i] = False
    time.sleep(0.01)  