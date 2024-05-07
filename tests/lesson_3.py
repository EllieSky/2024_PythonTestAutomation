from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)

tom = Turtle()
tom.shape("turtle")
tom.color("dark blue")
tom.pensize(4)
tom.speed(50)


def draw_shape(size, num_angles):
    angle = 360 / num_angles
    for side in range(num_angles):
        tom.forward(size)
        tom.left(angle)


def choose_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


def draw_flower(petals, color=choose_color()):
    tom.pencolor(color)
    turn_degree = 360 / petals
    for petal in range(petals):
        draw_shape(50, 7)
        tom.right(turn_degree)


draw_flower(7)
tom.right(90)
tom.pencolor("green")
tom.forward(350)


scr = Screen()
scr.listen()
scr.exitonclick()
