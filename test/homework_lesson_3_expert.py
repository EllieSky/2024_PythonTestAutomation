from turtle import Turtle, Screen, colormode
import random
from random import randint, choice

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

def random_petal_shape():
    shapes = ['triangle', 'pentagon', 'hexagon', 'star']
    return choice(shapes)

def draw_flower(petals, color):
    judy.pencolor(color)
    petal_shape = random_petal_shape()
    turn_degrees = 360 / petals
    for _ in range(petals):
        if petal_shape == 'triangle':
            draw_shape(30, 3)
        elif petal_shape == 'pentagon':
            draw_shape(30, 5)
        elif petal_shape == 'hexagon':
            draw_shape(30, 6)
        elif petal_shape == 'star':
            draw_shape(30, 5)
        judy.right(turn_degrees)

def draw_garden(num_flowers):
    for i in range(num_flowers):
        stem_height = randint(150, 350)
        petals = randint(5, 9)
        color = get_color()
        judy.penup()
        judy.goto(-100 * num_flowers / 2 + 150 * i, -200)
        judy.pendown()
        draw_stem(stem_height)
        draw_flower(petals, color)

scr = Screen()
scr.listen()

draw_garden(4)

scr.exitonclick()

# Honestly, for the 'expert' level homework, I used ChatGPT for assistance. :))