#trying out the turtle module

import turtle

start = turtle.Screen()

star = turtle.Turtle()

turtle.speed ('slowest')

for i in range(5):
    star.forward(144)
    
    star.right(144)
    
turtle.write("Aash Gates Star", font=("") )