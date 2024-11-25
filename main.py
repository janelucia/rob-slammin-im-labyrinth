#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from movement import allignBackwards, allignForwards, allignNeck, driveForward, scan, spin, turnLeft, turnRight
from cfg import ev3


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

sharpness_of_correction = 1

drive_distance = 1000

allignNeck()

#turnRight()
#turnRight()
# turnLeft()

#allignBackwards()

#spin()


def driveToRed():

    driveForward(300)
    wait(1000)
    turnLeft()
    wait(1000)

    driveForward(300)
    wait(2000)
    print(scan())
    turnRight()
    wait(2000)

    driveForward(300)
    wait(2000)
    print(scan())
    turnLeft()
    wait(2000)

    driveForward(300)
    wait(2000)
    print(scan())
    wait(2000)
    turnRight()
    wait(2000)

    driveForward(300)
    wait(2000)
    turnRight()
    wait(2000)

    driveForward(300)
    wait(2000)
    print(scan())


ev3.speaker.beep()

driveToRed()



ev3.speaker.beep()

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
