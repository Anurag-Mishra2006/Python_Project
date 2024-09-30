from turtle import Turtle
from random import randint
r=randint(0,255)
b=randint(0,255)
g=randint(0,255)
colors=(r/255,b/255,g/255)
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(colors)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
         x=randint(-280,280)
         y=randint(-280,280)
         self.goto(x,y)




