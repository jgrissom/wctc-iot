from gpiozero import DigitalOutputDevice, InputDevice, LED, Buzzer
from time import sleep

leds = { "green": LED(13), "red": LED(12) }
for led in leds:
    leds[led].off()

orange = { "tx": DigitalOutputDevice(26), "rx": InputDevice(20) }

buzzer = Buzzer(24)

try:
    orange["tx"].value = 1
    while True:
        leds["green"].value = orange["rx"].value
        leds["red"].value = not orange["rx"].value
        buzzer.value = not orange["rx"].value
        print(orange["rx"].value)
        sleep(.3)
except KeyboardInterrupt:
    print("bye")
    buzzer.off()
    for led in leds:
        leds[led].off()
        