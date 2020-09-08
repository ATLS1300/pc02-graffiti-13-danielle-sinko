#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: YOUR NAME
May 29, 2020
'''

from turtle import * #import the library of commands that you'd like to use

colormode(255)

# Create a panel to draw on. 
panel = Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
# making red line on his eyes
home()
up()
goto(100,100)
goto(120,120)
clear()
pencolor('red')
pensize(2)
right(180)
forward(200)
forward(-200)
#positioning of the circles
down()
forward(300)
pencolor('black')
up()
left(90)
forward(100)
right (180)
forward(220)
right(90)
forward(90)
right(90)
forward(100)
left(180)
forward(50)
right(90)
forward(10)
#pink circles 
down()
pensize(30)
pencolor('pink')
circle(30,360)
up()
forward(100)
down()
pensize(30)
pencolor('pink')
circle(30,360)
up()
#filled circle 
goto(0,-60)
dot(60)
# white square in the sky 
up()
goto(200,100)
down()
pensize(20)
pencolor('white')
pensize('5')
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
# star shape in the sky
up()
goto(-200,100)
down()
pensize(5)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
# triangle in the sky
up()
goto(200,250)
down()
pensize(10)
forward(100)
left(60)
forward(100)
left(150)
forward(170)
#thin white stars
up()
goto(-250,-200)
down()
pensize(5)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
up()
goto(-260,0)
down()
pensize(5)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
# red thin star
up()
goto(260,-100)
down()
pensize(5)
pencolor(255,0,0)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
# blue star
up()
goto(260,-180)
down()
pensize(30)
pencolor('blue')
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
#green star
up()
goto(280,210)
down()
pensize(30)
pencolor(0,255,0)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
#purple star
up()
goto(-280,200)
down()
pensize(30)
pencolor('purple')
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)
forward(50)
left(144)





















        
        


















