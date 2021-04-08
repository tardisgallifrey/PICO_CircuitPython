<h1>Raspberry Pi PICO running with CircuitPython</h1>
<hr>
<p>This is a place where I will store initial work on using the Raspberry Pi PICO</p>
<p>"Code.py" and "Dave.py" can be dropped right into your PICO folder once connected.</p>
<p>Initial work is with getting 10k commercial thermistors to work and read properly</p>
<p>My IDE of choice is Visual Studio Code, with github, MagicPython, and CircuitPython extensions 
added in order to gain Intellisense for the CP package.</p>
<p>Additionally, I've found that the 'cu' app under Linux does just fine as a serial monitor for the PICO.  I couldn't get the one with the extensions to operate correctly.</p>
<hr>
<p>Vsys(type) returns board.A3 Vsys voltage. type=1 returns a 5VDC range, which is VBUS. type=0 returns VBUS scaled to 3.3VDC range.  Useful in Analog input calculations to correct for slight inaccuracies in VBUS voltages.</p>
<p>AIconstant(type) - same type values as above, but returns generic volts/unit (i.e. 3.3 / 65535) for analog input calculations where voltage isn't critical</p>
<p>basic_sanity(led, seconds) - function for a basic sanity test light.
<p>read_thermistor(thermistor, Ro, Rseries, Beta, celsius) - read thermistor function.  Supply AI pin for thermistor (must be already set up with AnalogIn()), Ro = thermistor type (10 or 100, usually), Rseries (the series resistor in the circuit, again probably 10 or 100), the Steinhart/Hart Beta number for the thermistors you have, and whether or not you want celsius(1) or fahrenheit(0) returned.</p>
<p>Please bear in mind, none of these functions use error checking as of yet.</p>