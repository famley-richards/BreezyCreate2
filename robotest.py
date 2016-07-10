#!/usr/bin/env python3

DRIVETIME = 1 #seconds

from breezycreate2 import Robot
import time

# Create a Create2. This will automatically try to connect to your robot over serial
bot = Robot()

# Play a note to let us know you're alive!
bot.playNote('A4', 100)

'''
# Tell the Create2 to drive straight forward at a speed of 100 mm/s
bot.setForwardSpeed(100)

# Wait for a few seconds
time.sleep(DRIVETIME)

# Stop
bot.stop()


# Listen for a bumper hit
while True:
    
    #Packet 100 contains all sensor data.
    bot.get_packet(100)

    #print json.dumps(bot.sensor_state, indent=4, sort_keys=False)
    sensors = bot.sensor_state # a dictionary
    for key in sensors.keys():
        if key == 'wheel drop and bumps':
            print(sensors[key])
    print('-------------------------------')

    time.sleep(.5)
'''

# Close the connection
bot.close()
