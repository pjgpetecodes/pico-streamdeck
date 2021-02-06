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

led1_pin = board.GP13
led2_pin = board.GP14
led3_pin = board.GP15
led4_pin = board.GP16
led5_pin = board.GP17
led6_pin = board.GP18
led7_pin = board.GP19
led8_pin = board.GP20
led9_pin = board.GP21
led10_pin = board.GP22

# Setup all Buttons as Inputs with PullUps
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

# Setup LED Pins
led1 = DigitalInOut(led1_pin)
led1.direction = Direction.OUTPUT

led2 = DigitalInOut(led2_pin)
led2.direction = Direction.OUTPUT

led3 = DigitalInOut(led3_pin)
led3.direction = Direction.OUTPUT

led4 = DigitalInOut(led4_pin)
led4.direction = Direction.OUTPUT

led5 = DigitalInOut(led5_pin)
led5.direction = Direction.OUTPUT

led6 = DigitalInOut(led6_pin)
led6.direction = Direction.OUTPUT

led7 = DigitalInOut(led7_pin)
led7.direction = Direction.OUTPUT

led8 = DigitalInOut(led8_pin)
led8.direction = Direction.OUTPUT

led9 = DigitalInOut(led9_pin)
led9.direction = Direction.OUTPUT

led10 = DigitalInOut(led10_pin)
led10.direction = Direction.OUTPUT

# Define HID Key Outputs
key_Keypad1=Keycode.KEYPAD_ONE
key_Keypad2=Keycode.KEYPAD_TWO
key_Keypad3=Keycode.KEYPAD_THREE
key_Keypad4=Keycode.KEYPAD_FOUR
key_Shift = Keycode.SHIFT
key_Ctrl = Keycode.CONTROL
keyboard=Keyboard(usb_hid.devices)

selectedInput = -1

# Loop around and check for key presses
while True:

    if selectedInput == 1:
        led1.value = True
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
    elif selectedInput == 2:
        led1.value = False
        led2.value = True
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
    elif selectedInput == 3:
        led1.value = False
        led2.value = False
        led3.value = True
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
    elif selectedInput == 4:
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = True
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
    elif selectedInput == 5:
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = True
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
    elif selectedInput == 6:
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = True
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = False
    elif selectedInput == 7:
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = True
        led8.value = False
        led9.value = False
        led10.value = False
    elif selectedInput == 8:
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = True
        led9.value = False
        led10.value = False
    elif selectedInput == 9:
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = True
        led10.value = False
    elif selectedInput == 10:
        led1.value = False
        led2.value = False
        led3.value = False
        led4.value = False
        led5.value = False
        led6.value = False
        led7.value = False
        led8.value = False
        led9.value = False
        led10.value = True
    else:
        pass
 
    if not btn1.value:
        keyboard.press(key_Ctrl, key_Keypad1)
        keyboard.release(key_Ctrl, key_Keypad1)
        selectedInput = 1
    elif not btn2.value:
        keyboard.press(key_Ctrl, key_Keypad2)
        keyboard.release(key_Ctrl, key_Keypad2)
        selectedInput = 2
    elif not btn3.value:
        keyboard.press(key_Ctrl, key_Keypad3)
        keyboard.release(key_Ctrl, key_Keypad3)
        selectedInput = 3
    elif not btn4.value:
        keyboard.press(key_Ctrl, key_Keypad4)
        keyboard.release(key_Ctrl, key_Keypad4)
        selectedInput = 4
    elif not btn5.value:
        keyboard.press(key_Ctrl, key_Keypad4)
        keyboard.release(key_Ctrl, key_Keypad4)
        selectedInput = 5
    elif not btn6.value:
        keyboard.press(key_Ctrl, key_Keypad4)
        keyboard.release(key_Ctrl, key_Keypad4)
        selectedInput = 6
    elif not btn7.value:
        keyboard.press(key_Ctrl, key_Keypad4)
        keyboard.release(key_Ctrl, key_Keypad4)
        selectedInput = 7
    elif not btn8.value:
        keyboard.press(key_Ctrl, key_Keypad4)
        keyboard.release(key_Ctrl, key_Keypad4)
        selectedInput = 8
    elif not btn9.value:
        keyboard.press(key_Ctrl, key_Keypad4)
        keyboard.release(key_Ctrl, key_Keypad4)
        selectedInput = 9
    elif not btn10.value:
        keyboard.press(key_Ctrl, key_Keypad4)
        keyboard.release(key_Ctrl, key_Keypad4)
        selectedInput = 10
    else:
        pass

    # sleep for debounce
    time.sleep(0.1) 