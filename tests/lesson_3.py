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


def draw_flower(petals, stem_length, color):
    #Draw stem
    tom.penup()
    tom.setheading(90)
    tom.pencolor("green")
    tom.pendown()
    tom.forward(stem_length)

    #Draw flower
    tom.penup()
    tom.pencolor(color)
    tom.pendown()
    turn_degree = 360 / petals
    for petal in range(petals):
        draw_shape(50, 3)
        tom.right(turn_degree)

def draw_garden(num_flowers):
    stem_length = 250

    # Calculate starting position:
    screen = Screen()
    screen_height = screen.window_height()
    screen_width = screen.window_width()
    start_x = (screen_width / 3)
    start_y = -(screen_height / 4)

    # Go to starting position:
    tom.penup()
    tom.goto(start_x, start_y)

    # Draw flowers
    for n in range(num_flowers):
        tom.penup()
        draw_flower(randint(3, 12), stem_length, color=choose_color())
        tom.penup()
        tom.backward(stem_length)
        tom.left(90)
        tom.forward(100)  # Spacing between flowers


draw_garden(7)  # Draw a garden with n flowers

scr = Screen()
scr.listen()
scr.exitonclick()
