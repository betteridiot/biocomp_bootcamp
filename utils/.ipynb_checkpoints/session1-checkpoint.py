#!/usr/env/bin python
""" Session 1 Utility functions

This script is meant to be importable to aide in session 1 demonstrations
"""
import turtle

def start():
    """Initializes the turtle session with pre-defined presets"""
    turtle.getscreen()
    turtle.left(90)
    turtle.pen(fillcolor='#FFCB05', pencolor='#00274C', speed=5)
    return None

def reset():
    """ Clears the canvas and resets the turtle to origin"""
    turtle.clear()
    turtle.reset()
    turtle.left(90)
    turtle.pen(fillcolor='#FFCB05', pencolor='#00274C', speed=5)
    return None

def demo():
    turtle.begin_fill()
    while True:
        turtle.forward(200)
        turtle.left(170)
        if abs(turtle.pos()) < 1:
            break
    turtle.end_fill()