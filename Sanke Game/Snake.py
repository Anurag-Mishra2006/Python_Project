from turtle import Turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
           self.add_segment(position)

    def add_segment(self,position):
        tin = Turtle()
        tin.shape("square")
        tin.color("white")
        tin.up()
        tin.goto(position)
        self.segment.append(tin)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(self.segment[-1].position())
    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
