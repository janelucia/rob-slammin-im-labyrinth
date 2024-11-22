from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color

colorSensor = ColorSensor(Port.S2)
distanceSensor = UltrasonicSensor(Port.S1)


def getDistance() -> int:
    return distanceSensor.distance()

def getColor() -> Color:
    return colorSensor.color()