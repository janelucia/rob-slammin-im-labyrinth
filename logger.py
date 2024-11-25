from cfg import ev3

SAY = False


def logAndSay(string: str):
    print(string)
    if (SAY): 
        ev3.speaker.say(string)