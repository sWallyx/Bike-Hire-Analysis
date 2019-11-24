# File with generic functions

from defaultParams import DEFAULT_TIME_VALUE

def isNaN(num):
    return num != num

def checkNaNValue(num):
    if(isNaN(num)):
        num = DEFAULT_TIME_VALUE

    return num