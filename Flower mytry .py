# My try with the code form riju_ghosh___ instagram profile

import turtle
turtle.setworldcoordinates(-2000,-2000,2000,2000)

def draw_football(x,y,tilt,radius):
  turtle.Screen().bgcolor("black")
  turtle.pencolor('green')
  turtle.width(4)
  turtle.speed('fast')
  turtle.up()
  turtle.goto(x,y)
  turtle.down()
  turtle.seth(tilt-45)
  turtle.circle(radius,90)
  turtle.left(90)
  turtle.circle(radius,90)

for tilt in range(0,360,30):
    
    draw_football(0,0,tilt,1000) 
    
#end of the program
    
    