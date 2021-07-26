#trying out the turtle module

import turtle


turtle.write("Aash Gates Star", font=("Blackadder ITC",))

import time
time.sleep(2.00)


start = turtle.Screen()

star = turtle.Turtle()

turtle.speed ('slowest')



for i in range(5):
    star.forward(144)
    
