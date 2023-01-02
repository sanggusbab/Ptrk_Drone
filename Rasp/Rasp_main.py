import RPi.GPIO as GPIO
import pigpio
import sys
import keyboard

print("Boot successful")

print("Start flight?: Y/N")

while True:
    if keyboard.is_pressed('y'):
        print("select mode: M/S/A")
        break
    elif keyboard.is_pressed('n'):
        break

while True:
    print("Press Q to quit")
    if keyboard.is_pressed('q'):
        print("Quit flight")
        break

    if keyboard.is_pressed('m'):
        print("Manual flight mode")
    elif keyboard.is_pressed('s'):
        print("Stabilized flight mode")
    elif keyboard.is_pressed('a'):
        print("Auto flight mode")

print("End of boot.py")
GPIO.cleanup()
# hello World!
