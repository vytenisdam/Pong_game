from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.setpos(0,0)

    def move(self):
        new_y = self.ycor() + 1
        new_x = self.xcor() + 1
        self.goto(new_x, new_y)
