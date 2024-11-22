#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from movement import allignBackwards, allignForwards, allignNeck, scan, spin, turnLeft, turnRight


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

sharpness_of_correction = 1

drive_distance = 1000

# turnRight()

# turnLeft()

#allignBackwards()

allignNeck()
print(scan())

exit()

allignForwards()
 

exit()

wait(2000)

speed = 1


robot.stop()
motor_left.brake()
motor_right.brake()

wait(2000)



ev3.speaker.beep()
ev3.speaker.say("Ich habe mich um " + str(gyro.angle()) + " Grad gedreht!")



print("Angles:")
print(motor_left.angle())
print(motor_right.angle())
print(gyro.angle())
