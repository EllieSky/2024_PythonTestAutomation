from turtle import Turtle, Screen, colormode
import random
from random import randint

colormode(255)
bobbby = Turtle()
bobbby.speed(30)
bobbby.shape('turtle')
bobbby.color('purple')
bobbby.pensize(4)

def draw_square(size = 40):
    draw_shape(size,4)
    # bobbby.forward(size)
    # bobbby.left(90)
    # bobbby.forward(size)
    # bobbby.left(90)
    # bobbby.forward(size)
    # bobbby.left(90)
    # bobbby.forward(size)
    # bobbby.left(90)
    # for side in range(4):
    #     bobbby.forward(size)
    #     bobbby.left(90)
def draw_traingle(size=40):
    for s in range(3):
        bobbby.forward(size)
        bobbby.left(120)

def draw_shape(size,num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        bobbby.forward(size)
        bobbby.left(angle)



    # bobbby.forward(size)
    # bobbby.left(120)
    # bobbby.forward(size)
    # bobbby.left(120)
    # bobbby.forward(size)
    # bobbby.left(120)

def get_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return r , g ,b


def draw_flower(petals, color=get_color()):
    bobbby.pencolor(color)
    turn_degrees = 360/petals
    for petal in range(petals):
        draw_shape(50,7)
        bobbby.right(turn_degrees)



# def get_color():
#     r = randint(0,255)
#     g = randint(0,255)
#     b = randint(0,255)
#     return r , g ,b



scr = Screen()
scr.listen()

draw_flower(10)
bobbby.right(90)
bobbby.pencolor("dark green")
bobbby.forward(300)
 # bobby garden

bobbby.right(90)
bobbby.penup()
bobbby.forward(100)
bobbby.right(90)
bobbby.pendown()
bobbby.forward(100)
# draw_flower(10, "pink")
# draw_flower(10,get_color())
# petals = 5
# turn_degrees = (360/petals)
#
# # draw_square(100)
# draw_shape(50,7)
# bobbby.right(turn_degrees)
# draw_shape(50,7)
# bobbby.right(turn_degrees)
# draw_shape(50,7)
# bobbby.right(turn_degrees)
# draw_shape(50,7)
# bobbby.right(turn_degrees)
# draw_shape(50,7)
# bobbby.right(turn_degrees)

# draw_square(10)
# # bobbby.forward(30)
# # draw_square()
# draw_traingle()



# bobbby.forward(40)
# bobbby.right(90)
# bobbby.forward(100)
# bobbby.back(70)
# bobbby.circle(10)



scr.exitonclick()


