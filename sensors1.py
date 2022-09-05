import gpiozero  # GPIO Zero library
import time  # Time library
 
# File name: test_ultrasonic_sensor.py
# Code source (Matt-Timmons Brown): https://github.com/the-raspberry-pi-guy/raspirobots
# Date created: 5/28/2019
# Python version: 3.5.3
# Description: Test the HC-SR04 ultrasonic
# distance sensor
 
# Assign the GPIO pin number to these variables.
TRIG = 23
ECHO = 24
 
# This sends out the signal to the object
trigger = gpiozero.OutputDevice(TRIG)
 
# This variable is an input that receives
# the signal reflected by the object
echo = gpiozero.DigitalInputDevice(ECHO)
 
# Send out a 10 microsecond pulse (ping)
# from the trasmitter (TRIG)
trigger.on()
time.sleep(0.00001)
trigger.off()
 
# Start timer as soon as the reflected sound
# wave is "heard" by the receiver (echo)
while echo.is_active == False:
    pulse_start = time.time() # Time of last LOW reading
 
# Stop the timer one the reflected sound wave
# is done pushing through the receiver (ECHO)
# Wave duration is proportional to duration of travel
# of the original pulse.
while echo.is_active == True:
    pulse_end = time.time() # Time of last HIGH reading
 
pulse_duration = pulse_end - pulse_start
 
# 34300 cm/s is the speed of sound
distance = 34300 * (pulse_duration/2)
 
# Round to two decimal places
round_distance = round(distance,2)
 
# Display the distance
print("Distance: ", round_distance)
