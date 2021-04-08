import board
from digitalio import Direction
from analogio import AnalogIn
import time
import math

#set up A3 (GP29) for analog in
#special internal pin, reads VBUS/Vsys
volts = AnalogIn(board.A3)

#return Vsys based on regular USB 5VDC
#or the equivalent??? 3.3VDC
#1 = 5VDC 0 = 3.3VDC
def Vsys(type):
    if type:
        return volts.value * ( 10.0 / 65535 ) - 0.1
    else:
        return volts.value * ( 6.6 / 65535 ) - .05

# get an analog input constant for either
# 5 volt range or 3.3V range
# 1 = 5VDC 0 = 3.3VDC
def AIconstant(type):
    if type:
        return 5.0 / 65535
    else:
        return 3.3 / 65535

#Basic Sanity Test light
#send in a set up pin and seconds
#and a light will blink to say, "Yes, I'm awake!"
def basic_sanity(bst, delay):
    bst.direction = Direction.OUTPUT
    bst.value=True
    time.sleep(delay)
    bst.value=False
    time.sleep(delay)
    

# thermistor is defined pin from caller
# Ro is thermistor type either 10 or 100 for 10k or 100k thermistors
# Rseries is series resistor in in put circuit, in thousands only
# Beta number for this thermistor product
# celsius - return celsius if any positive number, fahrenheit if zerocircuit    
def read_thermistor(thermistor, Ro, Rseries, Beta, celsius):
    #Ro = thermistor type, 10K or 100k
    #Beta =  Nominal resistance 50K, Beta constant
    #Rseries = 15  Series resistor 10K
    To = 298.15           #Nominal Temperature
    
    #Vrt = Voltage across thermistor
    Vrt = thermistor.value * ( Vsys(0) / ( 65535 )) 
    
    #Convert voltage measured to resistance value
    #All Resistances are in kilo ohms.
    R = (Vrt * Rseries) / ( Vsys(0) - Vrt)
      
    #Use R value in steinhart and hart equation
    #Calculate temperature value in kelvin
    T =  1 / ((1/To) + (( math.log(R / Ro)) / Beta))
    Tc = T - 273.15               #Converting kelvin to celsius
    Tf = Tc * 9.0 / 5.0 + 32.0    #Converting celsius to Fahrenheit
    if celsius:
        return "{:.1f}".format(Tc)
    else:
        return "{:.1f}".format(Tf)