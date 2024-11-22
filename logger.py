from cfg import ev3


def logAndSay(string: str):
    print(string)
    ev3.speaker.say(string)