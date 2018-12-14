import turtle
import math

window = turtle.Screen()
window.bgpic("images/background.gif")
window.setup(1200, 800)

BASE_X, BASE_Y = 0, -315


def calc_heading(x1, y1, x2, y2):
    dx = x2 - x1
    length = (dx ** 2 + (y2 - y1) ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    return alpha, length


def fire_missle(x, y):
    alpha, length = calc_heading(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)

    missle = turtle.Turtle()
    missle.color("white")
    missle.penup()
    missle.setpos(x=BASE_X, y=BASE_Y)

    missle.setheading(alpha)
    missle.pendown()

    missle.forward(length)
    missle.shape("circle")
    missle.clear()

    # create bang animation
    for bang_size in [1, 2, 3, 4]:
        missle.shapesize(bang_size)

    missle.hideturtle()


window.onclick(fire_missle)

window.mainloop()
