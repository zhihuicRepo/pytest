#!/usr/bin/python
import datetime
import simplegui

def click():
    global message
    message = 'Good job'

def draw(canvas):
    canvas.draw_tex(message,[50,112],36,'Red')

#http://www.codeskulptor.org/#examples-simplegui-0.py

frame = simplegui.create_frame('Home',300,200)
