from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)
jimmy = Turtle()
jimmy.penup()
jimmy.goto(250,-150)
jimmy.pendown()
jimmy.speed(10)
jimmy.shape('turtle')
jimmy.color('purple')
jimmy.pensize(4)

def draw_shape(size,num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        jimmy.forward(size)
        jimmy.left(angle)

flower_1_color = input("Enter color for flower 1: ")
def draw_flower_1(petals, flower_1_color):
    jimmy.pencolor(flower_1_color)
    turn_degrees = 360/petals
    for petal in range(petals):
        draw_shape(50,7)
        jimmy.right(turn_degrees)


flower_2_color = input("Enter color for flower 2: ")
def draw_flower_2(petals,flower_2_color ):
    jimmy.pencolor(flower_2_color)
    turn_degrees = 360/petals
    for petal in range(petals):
        draw_shape(25,7)
        jimmy.right(turn_degrees)


flower_3_color = input("Enter color for flower 3: ")


def draw_flower_3(petals,flower_3_color ):
    jimmy.pencolor(flower_3_color)
    turn_degrees = 360/petals
    for petal in range(petals):
        draw_shape(50,7)
        jimmy.right(turn_degrees)


draw_flower_1(7,flower_1_color)

jimmy.right(90)
jimmy.pencolor("green")
jimmy.forward(200)
jimmy.penup()
jimmy.right(90)
jimmy.width(3)
jimmy.forward(200)
jimmy.pendown()
jimmy.right(90)
jimmy.forward(200)

draw_flower_2(4,flower_2_color)

jimmy.pencolor("green")
jimmy.left(100)
jimmy.penup()
jimmy.right(10)
jimmy.width(3)
jimmy.forward(200)
jimmy.pendown()


draw_flower_3(6,flower_3_color)
# Drawing a stem:
jimmy.left(90)
jimmy.pencolor("green")
jimmy.forward(200)
jimmy.penup()



scr = Screen()
scr.listen()

scr.exitonclick()