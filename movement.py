from pybricks.tools import wait
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.robotics import DriveBase

from logger import logAndSay
from scanner import getColor, getDistance
from utilities import run_in_thread


motor_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D)

motor_neck = Motor(Port.B)


robot = DriveBase(motor_left, motor_right, wheel_diameter=56, axle_track=47.7)
print("Base Settings:", robot.settings())
robot.settings(100, 200, 90, 180)
print("New Settings:", robot.settings())

base_speed = 100

def turnRight():
    logAndSay("Turning right!")
    robot.turn(90)


def turnLeft():
    logAndSay("Turning left!")
    robot.turn(-90)
    robot.state()

def spin():
    logAndSay("You spin my head right round right round")
    robot.turn(360)

def driveForward(distance: int):
    robot.settings
    robot.straight(distance)

def allignForwards():
    robot.stop()
    
    run_in_thread(motor_right.run_until_stalled, 100, Stop.BRAKE, 35)
    run_in_thread(motor_left.run_until_stalled, 100, Stop.BRAKE, 35)
    wait(1000)
    while(motor_right.speed() > 0 or motor_left.speed() > 0):
        print("still driving", motor_left.speed(), motor_right.speed())


def allignBackwards():
    robot.stop()
    
    run_in_thread(motor_right.run_until_stalled, -100, Stop.BRAKE, 35)
    run_in_thread(motor_left.run_until_stalled, -100, Stop.BRAKE, 35)
    wait(1000)
    while(motor_right.speed() < 0 or motor_left.speed() < 0):
        print("still driving", motor_left.speed(), motor_right.speed())


def allignNeck(isRight: bool = True):
    motor_neck.reset_angle(0)
    if isRight:
        motor_neck.run_until_stalled(-200, Stop.COAST, 40)
    else:
        motor_neck.run_until_stalled(200, Stop.COAST, 40)
    motor_neck.reset_angle(0)


def scan() -> tuple[int, int, int, Color]:

    color = getColor()

    allignNeck(True)
    # Scan right
    r_distance = getDistance()
    wait(500)
    # Turn left (to middle) and scan
    motor_neck.run_angle(200, 105)
    wait(500)
    m_distance = getDistance()
    wait(500)
    # Turn left (to left)
    allignNeck(False)
    l_distance = getDistance()


    return [r_distance, m_distance, l_distance, color]
