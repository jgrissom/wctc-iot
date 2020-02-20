from gpiozero import DigitalOutputDevice
from time import sleep
import random

d = DigitalOutputDevice(2, active_high=False)
d.on()
sleep(3)
d.off()