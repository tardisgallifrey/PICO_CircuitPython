# Dave's 10K thermistor program
# built for CircuitPython
# 04/05/2021

#A0 is thermistor input
#GP0 is led (basic sanity test light)


import board
from analogio import AnalogIn
from digitalio import DigitalInOut
from dave import basic_sanity, read_thermistor, Vsys, AIconstant
import time


led = DigitalInOut(board.GP0)
sensor = AnalogIn(board.GP26_A0)


while True:
    basic_sanity(led, .5)
    
    Temp=read_thermistor(sensor, 10, 12, 3950, 0)
    print(f"{Temp}")
    time.sleep(2)
    