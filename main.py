from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)



r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

game_is_on = True

while game_is_on:
    ball.move()
    screen.update()
    screen.listen()

    screen.onkey(r_paddle.move_up, 'Up')
    screen.onkey(r_paddle.move_down, 'Down')
    screen.onkey(l_paddle.move_up, 'w')
    screen.onkey(l_paddle.move_down, 's')
