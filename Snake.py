from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)



def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

    
