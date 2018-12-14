import turtle
import random


window = turtle.Screen()
window.bgpic("images/background.gif")
window.setup(1200, 800)


pen = turtle.Turtle()
pen.color("orange")
pen.shape("turtle")
pen.speed(50)

def airplane(y):
    for current_x in [-200, 0, 200]:
        pen.penup()
        pen.setpos(x=current_x, y=y)
        pen.pendown()
        pen.circle(radius=random.randint(50, 200))
        pen.penup()
        pen.forward(100)

airplane(100)
airplane(200)



window.mainloop()

