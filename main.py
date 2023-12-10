from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
paddle = Turtle()
paddle.setpos(x=350, y=0)
paddle.penup()
paddle.shape('square')
paddle.color('white')
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.setpos(x=350, y=0)


def move_up():
    new_y = paddle.ycor() + 20
    if new_y >= 300:
        new_y = 300
    paddle.goto(paddle.xcor(), new_y)


def move_down():
    new_y = paddle.ycor() - 20
    if new_y <= -300:
        new_y = -300
    paddle.goto(paddle.xcor(), new_y)


game_is_on = True

while game_is_on:
    screen.update()
    screen.listen()

    screen.onkey(move_up, 'Up')
    screen.onkey(move_down, 'Down')