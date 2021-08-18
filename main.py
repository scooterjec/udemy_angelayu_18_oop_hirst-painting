# import colorgram
#
# colors = colorgram.extract('image.jpg', 40)
# color_list = [tuple(x.rgb) for x in colors]
# print(color_list)

from turtle import Turtle, Screen, colormode
from random import choice

colors = [(131, 166, 205), (222, 148, 106), (31, 42, 61), (199, 134, 147), (165, 59, 48), (140, 184, 162), (39, 105, 157), (238, 212, 89), (152, 58, 66), (217, 81, 70), (169, 29, 33), (236, 165, 156), (50, 112, 90), (35, 61, 55), (17, 97, 71), (156, 33, 30), (231, 160, 165), (53, 44, 49), (170, 188, 221), (57, 51, 48), (189, 100, 110), (31, 60, 109), (103, 127, 161), (34, 151, 209), (174, 200, 188), (65, 66, 56), (105, 140, 123), (152, 202, 228), (50, 68, 71), (130, 128, 122)]


def draw_circle():
    color = choice(colors)
    t.dot(10, color)


def draw_line():
    for _ in range(10):
        draw_circle()
        t.forward(50)


colormode(255)
t = Turtle()
t.hideturtle()
t.speed("fastest")
t.penup()
t.setposition(-200.0, -200.0)

for _ in range(10):
    draw_line()
    t.setposition(-200.0, t.ycor() + 50.0)



s = Screen()
s.exitonclick()