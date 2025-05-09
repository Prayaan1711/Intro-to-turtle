import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
star = turtle.Turtle()

star.forward(100)
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

star.penup()
star.right(90)
star.forward(60)
star.right(90)
star.pendown()
star.forward(100)
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

turtle.done()