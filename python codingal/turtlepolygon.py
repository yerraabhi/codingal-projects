# import turtle
# turtle.Screen().bgcolor("Orange")
# turtle.Screen().setup(300,400)
# polygon=turtle.Turtle()
# polygon.width(5)
# polygon.fillcolor("red")
# sides=int(input("Enter sides:"))
# sidelength=int(input("Enter length of side:"))
# angle=360/sides
# polygon.begin_fill()
# for i in range(sides):
#     polygon.forward(sidelength)
#     polygon.right(angle)
# polygon.end_fill()
# turtle.done()

import turtle
turtle.Screen().bgcolor("Orange")
turtle.Screen().setup(300,400)
star=turtle.Turtle()
star.width(5)
star.fillcolor("red")
star.begin_fill()
for i in range(3):
    star.forward(200)
    star.right(120)
star.end_fill()
star.penup()
star.goto(200,-100)
star.pendown()
star.left(120)
star.begin_fill()
for i in range(3):
    star.forward(200)
    star.left(120)
star.end_fill()
turtle.done()