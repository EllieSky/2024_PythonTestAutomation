from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)

bobby = Turtle()
bobby.speed(15)
bobby.shape('turtle')
bobby.color("dark green")
bobby.pensize(4)


def draw_square(size=40):
    draw_shape(size, 4)


def draw_triangle(size=40):
    for s in range(3):
        bobby.forward(size)
        bobby.left(120)


def draw_shape(size, num_sides):
    angle = 360 / num_sides
    for s in range(num_sides):
        bobby.forward(size)
        bobby.left(angle)


def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def draw_flower(petals, color=get_color()):
    bobby.pencolor(color)
    turn_degrees = 360 / petals
    for petal in range(petals):
        draw_shape(50, 7)
        bobby.right(turn_degrees)


scr = Screen()
scr.listen()

draw_flower(13)
bobby.right(90)
bobby.pencolor("dark green")
bobby.forward(300)

bobby.penup()
bobby.backward(300)
bobby.pendown()

scr.exitonclick()
