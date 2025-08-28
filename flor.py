import turtle

ventana=turtle.Screen()
t=turtle.Turtle()
t.color ("green")

for i in range(9):
    t.circle(100)
    t.left(45)

t.write("flor verde:D", font=("comic sans", 30, "normal"))

turtle.done() 