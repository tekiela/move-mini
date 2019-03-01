from microbit import *
import radio
channel = 1

radio.on()
radio.config(channel=channel)

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        buttonNum = 5
        sleep(100)
    elif button_a.is_pressed():
        buttonNum = 1
    elif button_b.is_pressed():
        buttonNum = 3
    else:
        buttonNum = 0
    radio.send(str(buttonNum))
