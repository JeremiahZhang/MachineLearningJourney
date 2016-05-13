# -*- coding: utf-8 -*-
import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)

    draw_square(brad)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    angie.speed(2)

    # how synonmous
    window.exitonclick()

def draw_trangle():
    trans = turtle.Turtle()
    trans.shape("turtle")
    trans.color('yellow')

draw_square()