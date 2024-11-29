from pybricks.tools import wait
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop, Direction, Color
from pybricks.robotics import DriveBase

from cfg import STANDARD_DRIVE_DISTANCE
from logger import logAndSay
from scanner import getColor, getDistance
from utilities import run_in_thread


class LookingDirection:
    
    directions = ["NORTH", "EAST", "SOUTH", "WEST"]

    def __init__(self, direction: str = None):
        if (direction):
            self.current_direction = direction
        else:
            self.current_direction = "NORTH"

    def turn_right(self):
        directions = self.directions
        idx_next = (directions.index(self.current_direction) + 1) % len(directions)
        self.current_direction = directions[idx_next]
    
    def turn_left(self):
        directions = self.directions
        idx_next = (directions.index(self.current_direction) - 1) % len(directions)
        self.current_direction = directions[idx_next]
    
    def turn_around(self):
        directions = self.directions
        idx_next = (directions.index(self.current_direction) + 2) % len(directions)
        self.current_direction = directions[idx_next]

motor_left = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D)

motor_neck = Motor(Port.B)

looking_direction = LookingDirection()
skip_next_instruction = False

robot = DriveBase(motor_left, motor_right, wheel_diameter=56, axle_track=47.7)
print("Base Settings:", robot.settings())
robot.settings(100, 50, 90, 180)
print("New Settings:", robot.settings())

base_speed = 100

def turnRight():
    looking_direction.turn_right()
    logAndSay("Turning right!")
    robot.turn(90)


def turnLeft():
    looking_direction.turn_left()
    logAndSay("Turning left!")
    robot.turn(-90)

def turnAround():
    looking_direction.turn_around()
    logAndSay("Turning around!")
    robot.turn(180)

def spin():
    logAndSay("You spin my head right round right round")
    robot.turn(360)

def driveForward(distance: int, isCheck: bool = True, next_instruction: str = None):
    robot.straight(distance)
    if isCheck:
        wait(1000)
        checkAlignment(next_instruction)

def allignForwards():
    print("Allign Forwards")
    robot.stop()
    
    run_in_thread(motor_right.run_until_stalled, 100, Stop.BRAKE, 22)
    run_in_thread(motor_left.run_until_stalled, 100, Stop.BRAKE, 22)
    wait(1000)
    while(motor_right.speed() > 0 or motor_left.speed() > 0):
        pass
    wait(1000)
    driveForward(-40, False)


def allignBackwards():
    print("Allign Backwards")
    robot.stop()
    
    run_in_thread(motor_right.run_until_stalled, -100, Stop.BRAKE, 23)
    run_in_thread(motor_left.run_until_stalled, -100, Stop.BRAKE, 23)
    wait(1000)
    while(motor_right.speed() < 0 or motor_left.speed() < 0):
        pass
    wait(1000)
    driveForward(40, False)


def allignNeck(isRight: bool = True):
    print("alligning the neck")
    motor_neck.reset_angle(0)
    if isRight:
        motor_neck.run_until_stalled(-200, Stop.COAST, 40)
    else:
        motor_neck.run_until_stalled(200, Stop.COAST, 40)
    motor_neck.reset_angle(0)


def scan() -> dict[str, int | Color]:

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

    return {"distance_r": r_distance, "distance_m": m_distance, "distance_l": l_distance, "color": color}

def checkAlignment(next_instruction: str = ""):
    global skip_next_instruction
    scanResult = scan()
    print("Checking Alignment")
    print(scanResult)

    print("Alignment checker: The next instruction is {}".format(next_instruction))

    # always align to the front if possible
    if scanResult.get("distance_m") < 140: 
        allignForwards()
        wait(2000)

    if scanResult.get("distance_r") < 140:
        turnLeft()
        wait(1000)
        allignBackwards()

        if (next_instruction != "turn_left"):
            wait(1000)
            turnRight()
        else: 
            print("test")
            skip_next_instruction = True

     
    elif scanResult.get("distance_l") < 140:
        turnRight()
        wait(1000)
        allignBackwards()

        if (next_instruction != "turn_right"):
            wait(1000)
            turnLeft()
        else: 
            skip_next_instruction = True
        

def driveAccordingToList(instructions: dict[str]):
    global skip_next_instruction

    print("Driving according to instruction list {}".format(instructions))
    for idx, instruction in enumerate(instructions):
        print("Step: {} of {}: {}".format(idx + 1, len(instructions), instruction))
        
        if (skip_next_instruction == True):
            skip_next_instruction = False
            print("Skipping step: '{}' because it was already fulfilled".format(instruction))
            continue
    
        next_instruction = None

        if (idx + 1 < len(instructions)):
            next_instruction = instructions[idx + 1]

        if (instruction == "drive_forward"):
            driveForward(STANDARD_DRIVE_DISTANCE, next_instruction=next_instruction)

        if (instruction == "turn_around"):
            turnAround()

        if (instruction == "turn_left"):
            turnLeft()

        if (instruction == "turn_right"):
            turnRight()
        
        # wait 1s after each procedure
        wait(1000)




