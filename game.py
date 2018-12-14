import turtle
import math

window = turtle.Screen()
window.bgpic("images/background.gif")
window.setup(1200, 800)
window.tracer(n=4)

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

    info = {'missile': missile, 'target': [x, y], 'state': 'launched', 'radius': 0}
    our_missiles.append(info)


window.onclick(fire_missile)

our_missiles = []

while True:
    window.update()

    for info in our_missiles:
        state = info['state']
        missile = info['missile']

        if state == 'launched':

            missile.forward(4)

            target = info['target']

            if missile.distance(x=target[0], y=target[1]) < 20:
                info['state'] = 'explode'
                missile.shape("circle")

        elif state == 'explode':
            info['radius'] += 1
            if info['radius'] > 5:
                missile.clear()
                missile.hideturtle()
                info['state'] = 'dead'
            else:
                missile.shapesize(info['radius'])

        dead_missiles = [info for info in our_missiles if info['state'] == 'dead']
        for dead in dead_missiles:
            our_missiles.remove(dead)



