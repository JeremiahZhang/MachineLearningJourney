# -*- coding: utf-8 -*-
import turtle

def draw_rhombus(some_turtle):
    # draw rhombus
    some_turtle.forward(100)
    some_turtle.right(45)
    some_turtle.forward(100)
    some_turtle.right(135)
    some_turtle.forward(100)
    some_turtle.right(45)
    some_turtle.forward(100)
    some_turtle.right(135)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    rhombus = turtle.Turtle()
    rhombus.shape("turtle")
    rhombus.color("yellow")
    rhombus.speed(10)

    for i in range(1,37):
        draw_rhombus(rhombus)
        rhombus.right(10)
    
    rhombus.right(90)
    rhombus.forward(300)

    window.exitonclick()

draw_art()