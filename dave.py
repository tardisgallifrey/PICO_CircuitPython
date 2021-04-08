from digitalio import Direction
import time
import math

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
    Vrt = thermistor.value * (3.27 / ( 65535 )) 
    
    #Convert voltage measured to resistance value
    #All Resistances are in kilo ohms.
    R = (Vrt * Rseries) / (3.27 - Vrt)
      
    #Use R value in steinhart and hart equation
    #Calculate temperature value in kelvin
    T =  1 / ((1/To) + (( math.log(R / Ro)) / Beta))
    Tc = T - 273.15               #Converting kelvin to celsius
    Tf = Tc * 9.0 / 5.0 + 32.0    #Converting celsius to Fahrenheit
    if celsius:
        return Tc
    else:
        return Tf