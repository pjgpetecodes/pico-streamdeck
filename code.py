#####################################################
#                                                   #
#           Raspberry Pi Pico Producer              #
#                                                   #
#         Developed by Pete Gallagher 2021          #
#                                                   #
#####################################################

# Author:   Pete Gallagher
# Version:  1.0
# Date:     11th February 2021
# Twitter:  https://www.twitter.com/pete_codes
# Blog:     https://www.petecodes.co.uk

# Imports
import time
import usb_hid
import board

from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# Initialize Keybaord
keyboard = Keyboard(usb_hid.devices)

# Define HID Key Output Actions
hid_actions = [
    {
        "name": "Scene 1",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_ONE),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 2",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_TWO),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 3",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_THREE),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 4",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_FOUR),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 5",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_FIVE),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 6",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_SIX),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 7",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_SEVEN),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 8",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_EIGHT),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 9",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_NINE),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 10",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.KEYPAD_ZERO),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 11",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.F13),
        "button": None,
        "led": None,
    },
    {
        "name": "Scene 12",
        "held": False,
        "keycode": (Keycode.CONTROL, Keycode.F14),
        "button": None,
        "led": None,
    },
]


# Define button pins
btn_pins = [
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP6,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
]

# Define led pins
led_pins = [
    board.GP12,
    board.GP13,
    board.GP14,
    board.GP16,
    board.GP17,
    board.GP18,
    board.GP19,
    board.GP20,
    board.GP21,
    board.GP22,
    board.GP26,
    board.GP27,
]

# Setup all Buttons as Inputs with PullUps
# Setup all LEDs
for i in range(12):
    button = DigitalInOut(btn_pins[i])
    button.direction = Direction.INPUT
    button.pull = Pull.UP
    hid_actions[i]["button"] = button

    led = DigitalInOut(led_pins[i])
    led.direction = Direction.OUTPUT
    hid_actions[i]["led"] = led


# Loop around and check for key presses
while True:

    for i in range(12):

        # check if button is pressed but make sure it is not held down
        if not hid_actions[i]["button"].value and not hid_actions[i]["held"]:

            # print the name of the command for debug purposes
            print(hid_actions[i]["name"])

            # send the keyboard commands
            keyboard.send(*hid_actions[i]["keycode"])
            time.sleep(0.01)

            # light up the associated LED
            hid_actions[i]["led"].value = True

            # turn off other LEDs that may be on
            for j in range(12):
                if i != j:
                    hid_actions[j]["led"].value = False

            # set the held to True for debounce
            hid_actions[i]["held"] = True

        # remove the held indication if it is no longer held
        elif hid_actions[i]["button"].value and hid_actions[i]["held"]:
            hid_actions[i]["held"] = False
