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
        new_y = self.ycor() + 10
        new_x = self.xcor() + 10

        if new_y >= 290 or new_x >= 290:
            new_y = 290
            new_x = 290

        self.goto(new_x, new_y)
