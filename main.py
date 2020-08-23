#trqq da mozhe da se cukat 2 kopcheta ednovremenno
#trqq se opravi tova sus zadurzhnaeto i dvizhenieto

import turtle
import winsound

window = turtle.Screen()
window.title("Ping Pong by @deiv_reiv follow on instagram")
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)  # making the window static / not updating it

# Paddle A, part of Turtle module
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")  # 20 x 20 pixels
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)  # making the paddle not a square
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B = copy of Paddle A, except coordinates
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")  # 20 x 20 pixels
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  # making the paddle not a square
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball - basicly the same xd
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # every time the ball moves it moves 2 pixels
ball.dy = 0.2

# bukvite lmao
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Milichko A: 0    Milichko B: 0", align="center", font=("Courier", 18, "normal"))

# Score durzhachkite
score_a = 0
score_b = 0


# Moving Paddle A Up Function
def paddle_a_up():
    y = paddle_a.ycor()  # returns the Y cor
    y += 20
    paddle_a.sety(y)


# Moving Paddle A Down Function
def paddle_a_down():
    y = paddle_a.ycor()  # returns the Y cor
    y -= 20
    paddle_a.sety(y)


# Moving Paddle B Up Function
def paddle_b_up():
    y = paddle_b.ycor()  # returns the Y cor
    y += 20
    paddle_b.sety(y)


# Moving Paddle B Down Function
def paddle_b_down():
    y = paddle_b.ycor()  # returns the Y cor
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
window.listen()
window.onkeypress(paddle_a_up, "w")
window.onkeypress(paddle_a_down, "s")

window.onkeypress(paddle_b_up, "Up")
window.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:  # za gornata stena
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("boing2.wav", winsound.SND_ASYNC)

    if ball.ycor() < -290:  # za dolnata stena
        ball.sety(- 290)
        ball.dy *= -1
        winsound.PlaySound("boing2.wav", winsound.SND_ASYNC)

    if ball.xcor() > 390:  # stena dqsna
        ball.goto(0, 0)
        ball.dx *= -1  # lqvo
        score_a += 1
        pen.clear()
        pen.write("Milichko A: {}    Milichko B: {}".format(score_a, score_b), align="center",
                  font=("Courier", 18, "normal"))

    if ball.xcor() < -390:  # stena lqva
        ball.goto(0, 0)
        ball.dx *= -1  # dqsno
        score_b += 1
        pen.clear()
        pen.write("Milichkoto mi: {}    Milichkoto ti: {}".format(score_a, score_b), align="center",
                  font=("Courier", 18, "normal"))

    if paddle_a.ycor() > 250:  # za gornata stena
        paddle_a.sety(250)

    if paddle_a.ycor() < -250:  # za dolnata stena
        paddle_a.sety(- 250)

    if paddle_b.ycor() > 250:  # za gornata stena
        paddle_b.sety(250)

    if paddle_b.ycor() < -250:  # za dolnata stena
        paddle_b.sety(- 250)

    # Paddle and Ball Collisions
    if (340 < ball.xcor() < 350) and (paddle_b.ycor() + 40 > ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("milichkoW.m4a", winsound.SND_ASYNC)

    if (-340 > ball.xcor() > -350) and (paddle_a.ycor() + 40 > ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("milichkoW.m4a", winsound.SND_ASYNC)
