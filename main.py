from turtle import Turtle, Screen
import random

colors = [(144, 76, 49), (188, 164, 120), (166, 153, 35), (14, 45, 83), (45, 110, 137), (142, 185, 175), (146, 55, 82),
          (59, 120, 100), (141, 169, 177), (86, 35, 29), (63, 152, 169), (219, 210, 94), (112, 37, 30), (101, 145, 111),
          (166, 98, 129), (94, 121, 170), (169, 144, 162), (178, 103, 83), (206, 183, 195), (50, 52, 90), (71, 38, 55)]
tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.title("Hirst Painting")
tim.hideturtle()
tim.penup()
tim.pos()
tim.speed("fastest")
tim.setposition(-225, -225)

for _ in range(10):
    for _ in range(10):
        color = random.choice(colors)
        tim.dot(20, color)
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.right(180)

screen.exitonclick()

# import colorgram
#
# clr = colorgram.extract("Hirst.jpg", 25)
# # first = clr[0]
# # rgb = first.rgb
# # print(rgb)
# colour_list = []
# for i in range(0, 25):
#     colour = clr[i]
#     r = colour.rgb.r
#     g = colour.rgb.g
#     b = colour.rgb.b
#     tuple = (r, g, b)
#     colour_list.append(tuple)
# print(colour_list)
