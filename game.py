import turtle
import math

window = turtle.Screen()
window.bgpic("images/background.gif")
window.setup(1200, 800)
window.tracer(n=2)

BASE_X, BASE_Y = 0, -315


def calc_heading(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    length = (dx ** 2 + (dy) ** 2) ** 0.5
    cos_alpha = dx / length
    alpha = math.acos(cos_alpha)
    alpha = math.degrees(alpha)
    if dy < 0:
        alpha = -alpha
    return alpha, length


def fire_missile(x, y):
    alpha, length = calc_heading(x1=BASE_X, y1=BASE_Y, x2=x, y2=y)
    missile = turtle.Turtle(visible=False)
    missile.color("white")

    missile.speed(0)

    missile.penup()
    missile.setpos(x=BASE_X, y=BASE_Y)
    missile.setheading(alpha)

    missile.showturtle()
    missile.pendown()

    # missile.forward(length)
    # missile.hideturtle()
    our_missiles.append(missile)
    our_missiles_target.append([x, y])
    our_missiles_states.append('launched')
    our_missiles_radius.append(0)

window.onclick(fire_missile)

our_missiles = []
our_missiles_target = []
our_missiles_states = []
our_missiles_radius = []

while True:
    window.update()

    for num, missile in enumerate(our_missiles):
        if our_missiles_states[num] == 'launched':

            missile.forward(4)
            target = our_missiles_target [num]
            if missile.distance (x=target[0], y=target[1]) < 20:
                our_missiles_states[num] = 'explode'
                missile.shape("circle")

        elif our_missiles_states[num] == 'explode':
            our_missiles_radius[num] += 1
            missile.shapesize(our_missiles_radius[num])

