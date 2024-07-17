from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)
sea_tutrle_natashka = Turtle()
sea_tutrle_natashka.shape("turtle")
sea_tutrle_natashka.color("red")
sea_tutrle_natashka.pensize(4)
sea_tutrle_natashka.speed(30)


# BASIC, ADVANCE, EXPERT
def get_number_of_petals():
    number_of_petals = randint(3, 13)
    return number_of_petals


def get_number_of_sides():
    number_of_sides = randint(3, 11)
    return number_of_sides


def draw_shape(size, num_sides=get_number_of_sides()):
    angle = 360 / num_sides
    for s in range(num_sides):
        sea_tutrle_natashka.forward(size)
        sea_tutrle_natashka.left(angle)


def get_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r, g, b


def get_number_of_flowers():
    number_of_petals = randint(3, 11)
    return number_of_petals


def get_length_of_steam():
    steam_length = randint(150, 351)
    return steam_length


def come_back_to_ground_level(steam_lenght):
    sea_tutrle_natashka.penup()
    sea_tutrle_natashka.left(180)
    sea_tutrle_natashka.forward(steam_lenght)
    sea_tutrle_natashka.left(90)
    sea_tutrle_natashka.forward(200)
    sea_tutrle_natashka.pendown()


def draw_flower(color="white", number_of_flowers=get_number_of_flowers()):
    for flowers in range(number_of_flowers):

        sea_tutrle_natashka.pencolor("green")

        sea_tutrle_natashka.left(90)
        steam_lenght = get_length_of_steam()
        sea_tutrle_natashka.forward(steam_lenght)
        if color == "white":
            sea_tutrle_natashka.pencolor(get_color())
        else:
            sea_tutrle_natashka.pencolor(color)
        petals = get_number_of_petals()
        turn_degrees = 360 / petals
        sides = get_number_of_sides()
        for petal in range(petals):
            draw_shape(40, sides)
            sea_tutrle_natashka.right(turn_degrees)
        come_back_to_ground_level(steam_lenght)


draw_flower()
scr = Screen()
scr.listen()
scr.exitonclick()
