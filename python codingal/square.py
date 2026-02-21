import turtle
turtle.Screen().bgcolor("Orange")
turtle.title("Welcome To Turtle Window")
turtle.pensize(4)
turtle.speed(4)
turtle.pencolor("White")
turtle.fillcolor("red")
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.done