# saw it i liked it i did it 

import turtle
turtle.speed("fastest")
turtle.pensize(2)
turtle.bgcolor("black")
colors=["red","blue","yellow","purple"]
for x in range(300):
    turtle.color(colors[x%4])
    turtle.forward(2*x)
    turtle.left(91)
turtle.done()

#end of the program