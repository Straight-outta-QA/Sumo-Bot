#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.tools import wait
from react_to_opponent import set_speed
from sense_edge import is_on_edge

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Constants
# ---------
# Diameter of the sumo bot's wheels
WHEEL_DIAMETER = 43

# The axle track is the distance between the centers of each of the
# wheels.  This is about 200 mm for the sumo bot.
AXLE_TRACK = 180

# Objects
# ---------
ev3 = EV3Brick()
left_motor = Motor(Port.B)
right_motor = Motor(Port.D)
sumo_bot = DriveBase(left_motor, right_motor, WHEEL_DIAMETER, AXLE_TRACK)
light_sensor = ColorSensor(Port.S1)

# Main program
# ------------
ev3.speaker.beep()
sumo_bot.settings(100, 800, 63, 254)
while(True):
    sumo_bot.drive(set_speed(0), 0)
    if (is_on_edge(light_sensor.reflection())):
        sumo_bot.straight(-70)
        sumo_bot.turn(180)
    wait(25)
