from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.segments = [] #to put the 3 sqaures of the snake body together
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        #for snake to disappear
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


    def extend(self):
        self.add_segment(self.segments[-1].position()) #getting hold and position of last segment

    """
    For seg in segments in range (start=2, stops=0, step=-1). 
    Starting positions = [(0, 0), (-20, 0), (-40, 0)], 
    we would want to move part3 (position 2) to part2 and then to part1, 
    hence the below for loop. 
    To move the snake together even during turns, 
    the idea is to move part2 to the previous position of part1, 
    then part3 to part2, and finally move part1 forward.
    """
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

#THE SNAKE IS NOT SUPPOSED TO MOVE BACK HENCE THE IF STATEMENTS
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        #to change the first part of snake to 90, the rest will follow using move()
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



