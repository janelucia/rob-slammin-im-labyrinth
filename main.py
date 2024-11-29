#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from movement import allignNeck, driveAccordingToList, driveForward, scan, spin, turnLeft, turnRight
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


basic_driving_instruction_list = [
    "drive_forward", 
    "turn_around", 
    "turn_right", 
    "turn_left"
]

def driveToRed():

    driving_instruction_list = [
        "drive_forward",
        "turn_left",
        "drive_forward",
        "turn_right",
        "drive_forward",
        "turn_left",
        "drive_forward",
        "turn_right",
        "drive_forward",
        "turn_right",
        "drive_forward",
        "turn_around",
        "drive_forward"
    ]

    driveAccordingToList(driving_instruction_list)


ev3.speaker.beep()

driveToRed()



ev3.speaker.beep()

exit()
 

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
