from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setpos(x=x_cor, y=y_cor)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y >= 250:
            new_y = 250
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y <= -250:
            new_y = -250
        self.goto(self.xcor(), new_y)