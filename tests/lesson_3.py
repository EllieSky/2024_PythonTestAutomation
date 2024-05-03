from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)

judy = Turtle()
judy.shape('turtle')
judy.color("purple")
judy.pensize(4)
judy.speed(30)

def draw_square(size = 40):
    draw_shape(size, 4)
    # for side in range(4):
    #     judy.forward(size)
    #     judy.left(90)

def draw_triangle(size = 40):
    for s in range (3):
        judy.forward(size)
        judy.left(120)

def draw_shape(size, num_sides):
    angle = 360 / num_sides
    for s in range(num_sides):
        judy.forward(size)
        judy.left(360 / num_sides)

def get_color ():
    r=randint (0, 255)
    b=randint(0, 255)
    g=randint(0, 255)
    return r, b, g

def draw_flower(petals, color=get_color()):
    judy.pencolor(color)
    turn_degrees = 360 / petals
    for petals in range (petals):
        draw_shape(50, 7)
        judy.right(turn_degrees)

# def get_color ():
#     r=randint (0, 255)
#     b=randint(0, 255)
#     g=randint(0, 255)
#     return r, b, g


scr = Screen()
scr.listen()

# draw_square()
# draw_square()
# draw_triangle()
# draw_flower(10, "pink")
# draw_flower(10, get_color())

draw_flower(8)
judy.right(90)
judy.pencolor("dark green")
judy.forward(300)

scr.exitonclick()

