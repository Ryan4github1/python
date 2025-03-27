import turtle
t=turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
angle=360/8
for i in range(8):
    t.forward(100)
    t.left(angle)
t.end_fill()
turtle.done()