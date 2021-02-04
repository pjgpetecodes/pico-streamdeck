# Imports
import time
import usb_hid
import board

from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Define Pins
btn1_Pin = board.GP0
btn2_Pin = board.GP1
btn3_Pin = board.GP2
btn4_Pin = board.GP3
btn5_Pin = board.GP4
btn6_Pin = board.GP5
btn7_Pin = board.GP6
btn8_Pin = board.GP7
btn9_Pin = board.GP8
btn10_Pin = board.GP9

#Setup all Buttons as Inputs with PullUps
btn1 = DigitalInOut(btn1_Pin)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP

btn2 = DigitalInOut(btn2_Pin)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP

btn3 = DigitalInOut(btn3_Pin)
btn3.direction = Direction.INPUT
btn3.pull = Pull.UP

btn4 = DigitalInOut(btn4_Pin)
btn4.direction = Direction.INPUT
btn4.pull = Pull.UP

btn5 = DigitalInOut(btn5_Pin)
btn5.direction = Direction.INPUT
btn5.pull = Pull.UP

btn6 = DigitalInOut(btn6_Pin)
btn6.direction = Direction.INPUT
btn6.pull = Pull.UP

btn7 = DigitalInOut(btn7_Pin)
btn7.direction = Direction.INPUT
btn7.pull = Pull.UP

btn8 = DigitalInOut(btn8_Pin)
btn8.direction = Direction.INPUT
btn8.pull = Pull.UP

btn9 = DigitalInOut(btn9_Pin)
btn9.direction = Direction.INPUT
btn9.pull = Pull.UP

btn10 = DigitalInOut(btn10_Pin)
btn10.direction = Direction.INPUT
btn10.pull = Pull.UP

# Define HID Key Outputs
key_Keypad1=Keycode.KEYPAD_ONE
key_Keypad2=Keycode.KEYPAD_TWO
key_Keypad3=Keycode.KEYPAD_THREE
key_Keypad4=Keycode.KEYPAD_FOUR
key_Shift = Keycode.SHIFT
key_Ctrl = Keycode.CONTROL
keyboard=Keyboard(usb_hid.devices)

# Loop around and check for key presses
while True:
    if not btn1.value:
        keyboard.press(key_Ctrl, key_Keypad1)
        keyboard.release(key_Ctrl, key_Keypad1)
    elif not btn2.value:
        keyboard.press(key_Ctrl, key_Keypad2)
        keyboard.release(key_Ctrl, key_Keypad2)
    elif not btn3.value:
        keyboard.press(key_Ctrl, key_Keypad3)
        keyboard.release(key_Ctrl, key_Keypad3)
    elif not btn4.value:
        keyboard.press(key_Ctrl, key_Keypad4)
        keyboard.release(key_Ctrl, key_Keypad4)
    else:
        pass

    # sleep for debounce
    time.sleep(0.1) 