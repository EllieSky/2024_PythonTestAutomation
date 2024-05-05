#Disclaimer - used the help of google to define the random flower position ))

from turtle import Turtle, Screen, colormode
import random
import math
from random import randint

colormode(255)

tinytim = Turtle()
tinytim.speed(60)
tinytim.shape('turtle')
tinytim.color("blue")
tinytim.pensize(7)

scr = Screen()
scr.listen()

def draw_shape(size, num_sides):
    angle = 360 / num_sides
    for s in range(num_sides):
       tinytim.forward(size)
       tinytim.left(angle)

def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b

def draw_flower():
    color=get_color()
    num_sides = randint(3, 8)              # Adjust as needed
    petals = randint(5, 15 )               # Adjust as needed
    stem_height = randint(100, 120)        # Adjust as needed
    tinytim.pencolor('green')
    tinytim.left(90)
    tinytim.forward(stem_height)
    tinytim.pencolor(color)
    turn_degrees = 360 / petals

    for petal in range(petals):
        draw_shape(40,num_sides)
        tinytim.right(turn_degrees)

    tinytim.right(90)

def within_distance(x1, y1, x2, y2, distance):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) <= distance

num_flowers = 30                      # Adjust as needed
distance_threshold = 100              # Adjust as needed

flower_positions = []

for _ in range(num_flowers):
    x = random.randint(-600, 600)  # Adjust as needed
    y = random.randint(-200, 200)  # Adjust as needed

    while any(within_distance(x, y, flower_x, flower_y, distance_threshold) for flower_x, flower_y in flower_positions):
        x = random.randint(-600, 600)  # Adjust as needed
        y = random.randint(-200, 200)  # Adjust as needed

# Draw the flower at the new position
    tinytim.penup()
    tinytim.goto(x, y)
    tinytim.pendown()
    draw_flower()

    # Store the position of the drawn flower
    flower_positions.append((x, y))


scr.listen()
scr.exitonclick()
