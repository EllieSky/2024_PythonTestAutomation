from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)

judy = Turtle()
judy.shape('turtle')
judy.color("purple")
judy.pensize(4)
judy.speed(30)

def draw_shape(size, num_sides):
    angle = 360 / num_sides
    for s in range(num_sides):
        judy.forward(size)
        judy.left(angle)

def draw_stem(size):
    judy.pencolor("dark green")
    judy.left(90)
    judy.forward(size)
    judy.right(90)

def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

def draw_flower(petals, color=get_color()):
    judy.pencolor(color)
    turn_degrees = 360 / petals
    for _ in range(petals):
        draw_shape(30, 7)
        judy.right(turn_degrees)

def draw_garden(num_flowers, stem_height, petals):
    start_x = -100 * num_flowers / 2
    for i in range(num_flowers):
        judy.penup()
        judy.goto(start_x + 150 * i, -200)
        judy.pendown()
        draw_stem(stem_height)
        draw_flower(petals)

scr = Screen()
scr.listen()

draw_garden(4, 260, 7)

scr.exitonclick()