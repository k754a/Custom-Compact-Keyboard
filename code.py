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

def key_action_0():

   

def key_action_1():

   

def key_action_2():

    print("Ending script...")
    while True:
        pass  

def type_text(text):
   
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
            time.sleep(0.1)
            keyboard.release(Keycode.SHIFT)
        elif char.islower():
            keyboard.press(getattr(Keycode, f"{char.upper()}"))
            keyboard.release_all()
        elif char == ' ':
            keyboard.press(Keycode.SPACE)
            keyboard.release_all()
        else:

            pass
        time.sleep(0.1)

def key_action_3():

    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.5)
    type_text("explorer.exe shell:appsFolder\\Microsoft.MinecraftUWP_8wekyb3d8bbwe!App")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_4():

    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.5)
    type_text("steam")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_5():

    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.5)
    type_text("nms")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_6():

    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.5)
    type_text("code")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_7():

    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.5)
    type_text("devenv")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

def key_action_8():

    keyboard.press(Keycode.WINDOWS)
    keyboard.press(Keycode.R)
    keyboard.release_all()
    time.sleep(0.5)
    type_text("pycharm")
    keyboard.press(Keycode.ENTER)
    keyboard.release_all()

pins = {}
for i in range(9):  
    pins[i] = digitalio.DigitalInOut(pin_map[i])
    pins[i].direction = digitalio.Direction.INPUT
    pins[i].pull = digitalio.Pull.DOWN  

while True:
    if pins[0].value:  
        key_action_0()

    if pins[1].value:  
        key_action_1()

    if pins[2].value:  
        key_action_2()

    if pins[3].value:  
        key_action_3()

    if pins[4].value:  
        key_action_4()

    if pins[5].value:  
        key_action_5()

    if pins[6].value:  
        key_action_6()

    if pins[7].value:  
        key_action_7()

    if pins[8].value:  
        key_action_8()

    time.sleep(0.01)  