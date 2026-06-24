import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.color("pink")

for i in range(360):
    angle = math.radians(i)

    x = 16 * (math.sin(angle) ** 3)
    y = (13 * math.cos(angle)
         - 5 * math.cos(2 * angle)
         - 2 * math.sin(3 * angle)
         - math.cos(4 * angle))

    x *= 12
    y *= 12

    t.penup()
    t.goto(x, y)
    t.write("Eu te amo!", align="center",
            font=("Arial", 8, "bold"))

turtle.done()
