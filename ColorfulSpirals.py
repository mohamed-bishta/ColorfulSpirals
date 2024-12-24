from turtle import *
import colorsys

speed(0)
bgcolor("black")
h = 0

for i in range(36):
    for j in range(4):  
        c = colorsys.hsv_to_rgb(h, 1, 1)
        color(c)
        h += 0.005
        forward(100)  
        left(90) 
    left(10)  