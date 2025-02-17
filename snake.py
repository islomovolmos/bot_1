# from symtable import Class
from turtle import Turtle


Start_Position=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):

        for pos in Start_Position:
            seg = Turtle('square')
            seg.color('white')
            seg.penup()
            seg.goto(pos)
            self.segments.append(seg)

    def move(self):
        for sega_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[sega_num-1].xcor()
            new_y = self.segments[sega_num - 1].ycor()
            self.segments[sega_num].goto(new_x,new_y)
        self.segments[0].forward(20)

    def add_snake(self,position):
        snake=Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    def extend_snake(self):
        self.add_snake(self.segments[-1].position())



    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(270)

    def right(self):
        self.segments[0].setheading(0)

    def left(self):
        self.segments[0].setheading(180)


