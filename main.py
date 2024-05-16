#TODO : for extracting colors from the image
# import colorgram
#
# colors = colorgram.extract('dot.jpg',30)
# total_color = []
#
# for item in range(len(colors)):
#     red = colors[item].rgb.r
#     greeen = colors[item].rgb.g
#     blue = colors[item].rgb.b
#     color = (red,greeen,blue)
#     total_color.append(color)
#
# print(total_color)

import turtle
import random
turtle.colormode(255)

color_list =[
    (233, 222, 92), (211, 158, 105), (116, 177, 210),
    (226, 57, 131), (181, 78, 33), (210, 135, 174),
    (41, 103, 161), (12, 21, 62), (184, 46, 111),
    (186, 164, 23), (43, 182, 112), (122, 187, 155),
    (25, 32, 158), (173, 16, 67), (234, 164, 199),
    (229, 75, 43), (22, 179, 205), (11, 41, 23),
    (49, 126, 73), (146, 218, 196), (51, 21, 11),
    (227, 220, 10), (106, 95, 206), (133, 215, 229),
    (175, 177, 227), (59, 16, 31)
]
turtle.speed(0)

for y in range(-250,250,50):
    turtle.penup()
    turtle.sety(y)
    for x in range(-250,250,50):
        turtle.setx(x)
        turtle.dot(20,random.choice(color_list))
        turtle.forward(50)



screen = turtle.Screen()
screen.exitonclick()