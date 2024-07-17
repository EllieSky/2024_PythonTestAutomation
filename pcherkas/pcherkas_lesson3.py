from turtle import Turtle, Screen, colormode
import random
from random import randint


colormode(255)
sea_tutrle_natashka = Turtle()
sea_tutrle_natashka.shape("turtle")
sea_tutrle_natashka.color("red")
sea_tutrle_natashka.pensize(4)
sea_tutrle_natashka.speed(30)

def move_forward():
    sea_tutrle_natashka.forward(10)

def draw_square(size = 40, ):
    # sea_tutrle_natashka.forward(size)
    # sea_tutrle_natashka.left(90)
    # sea_tutrle_natashka.forward(size)
    # sea_tutrle_natashka.left(90)
    # sea_tutrle_natashka.forward(size)
    # sea_tutrle_natashka.left(90)
    # sea_tutrle_natashka.forward(size)
    # sea_tutrle_natashka.left(90)

    for side in range(4):
        sea_tutrle_natashka.forward(size)
        sea_tutrle_natashka.left(90)

def draw_triangle (size=40):
    for side in range(3):
        sea_tutrle_natashka.forward(size)
        sea_tutrle_natashka.left(120)


def draw_shape(size, num_sides):
    angle = 360 / num_sides
    for s in range(num_sides):
        sea_tutrle_natashka.forward(size)
        sea_tutrle_natashka.left(angle)

def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b
def draw_flower(petals, color= get_color()):

    sea_tutrle_natashka.pencolor(color)
    turn_degrees = 360 / petals
    for petal in range(petals):
        draw_shape(50, 7)
        sea_tutrle_natashka.right(turn_degrees)






draw_flower(50, get_color())
scr = Screen()
scr.listen()
move_forward()
scr.exitonclick()
