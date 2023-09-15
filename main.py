###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
# import colorgram
# to get the data for the colors_list (inside color_file)
# rgb_colors = []
# # print(type(rgb_colors))
# colors = colorgram.extract('image.jpg', 30)
# # print(colors)
# for color in colors:
#     # print(color)
#     # rgb_colors.append(color.rgb)
#     # print(rgb_colors)
#     r = color.rgb.r
# #     to extract the value of r from the RGB tuple
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb_tuple = (r,g,b)
#     rgb_colors.append(new_rgb_tuple)
# print(rgb_colors)
# [<colorgram.py Color: Rgb(r=245, g=243, b=238), 64.68350168350169%>]
# the above line is what shows up when print(color), the datas inside the angle bracket(<>) is
# an object of the "color" class.colors is a list object. color is one object inside this list.
# rgb is an attribute.
# https://pypi.org/project/colorgram.py/


import turtle as t
import random
from color_file import colors_list

tim = t.Turtle()
t.colormode(255)

screen =t.Screen()

dot_size = 20
distance = 2 * dot_size
tim.penup()
tim.hideturtle()
# changing the starting point of my turtle
tim.right(90)
tim.forward(100)
tim.right(90)
tim.forward(200)
tim.right(180)
height = 10
current_position = tim.position()
print(current_position)

def paiting_dots(height):
 y_cor = -100
 while height > 0:
  for a in range(10):
   tim.dot(dot_size, random.choice(colors_list))
   tim.forward(distance)
  y_cor += 40
  tim.goto(-200,y_cor)
  height -= 1

paiting_dots(10)


#  current_position = tim.pos()
#  print(current_position)
#
# tim.goto(0, 40)
# for a in range(5):
#  tim.dot(dot_size, random.choice(colors_list))
#  tim.forward(distance)
#
# tim.goto(0, 80)
# current_position = tim.pos()
# print(current_position)

screen.exitonclick()




