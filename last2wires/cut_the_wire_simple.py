from gpiozero import DigitalOutputDevice, InputDevice
from time import sleep

orange = { "tx": DigitalOutputDevice(26), "rx": InputDevice(20) }

try:
    orange["tx"].value = 1
    while True:
        print(orange["rx"].value)
        sleep(.3)
except KeyboardInterrupt:
    orange["tx"].value = 0
    print("bye")
        