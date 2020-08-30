import turtle

# Background

wn = turtle.Screen()
wn.title("Pong by Aaryan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Objects
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = 0.1

pen = turtle.Turtle()
pen.penup()
pen.color("orange")
pen.speed(0)
pen.goto(0, 270)
pen.hideturtle()

# Scoring

score_1 = 0
score_2 = 0

# Movement


def paddle_1_up():
    y = paddle_1.ycor()
    if y < 300:
        y += 15
    paddle_1.sety(y)


def paddle_1_down():
    y = paddle_1.ycor()
    if y > -300:
        y -= 15
    paddle_1.sety(y)


def paddle_2_up():
    y = paddle_2.ycor()
    if y < 300:
        y += 15
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    if y > -300:
        y -= 15
    paddle_2.sety(y)


wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")


# Main Game Loop

while True:
    wn.update()
    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


# Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        pen.clear()
        pen.write("Player 1: {}    PLayer 2: {}".format(score_1, score_2), align="Center",
                  font=("Courier", 15, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Player 1: {}    PLayer 2: {}".format(score_1, score_2), align="Center",
                  font=("Courier", 15, "normal"))

    # Ball and Paddle

    if 340 < ball.xcor() < 350 and (paddle_2.ycor() + 40 > ball.ycor() > paddle_2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        if ball.dx < 0:
            ball.dx -= 0.01
        elif ball.dx < 0:
            ball.dx += 0.01

    if -340 > ball.xcor() > -350 and (paddle_1.ycor() + 40 > ball.ycor() > paddle_1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        if ball.dx < 0:
            ball.dx -= 0.01
        elif ball.dx < 0:
            ball.dx += 0.01

    if score_1 == 5:
        wn.bgcolor("green")
        pen.clear()
        pen.goto(0, 0)
        pen.write("PLAYER 1 WINS!", align="center", font=("courier", 40, "bold"))
    elif score_2 == 5:
        wn.bgcolor("yellow")
        pen.clear()
        pen.goto(0, 0)
        pen.write("PLAYER 2 WINS!", align="center", font=("courier", 40, "bold"))
