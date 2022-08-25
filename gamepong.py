import turtle
#main screen
wn = turtle.Screen()
wn.title("pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)



#paddle a
paddlea=turtle.Turtle()
paddlea.speed(0)
paddlea.shape("square")
paddlea.color("white")
paddlea.shapesize(stretch_wid=5, stretch_len=1)
paddlea.penup()
paddlea.goto(-350, 0)


#paddle b
paddleb=turtle.Turtle()
paddleb.speed(0)
paddleb.shape("square")
paddleb.color("white")
paddleb.shapesize(stretch_wid=5, stretch_len=1)
paddleb.penup()
paddleb.goto(350, 0)


#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx=0.5
ball.dy=0.5

#score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0", align="center", font=("curior",24,"normal"))

def paddlea_up():
    y=paddlea.ycor()
    y=y+20
    paddlea.sety(y)


def paddlea_down():
    y=paddlea.ycor()
    y=y-20
    paddlea.sety(y)


def paddleb_up():
    y = paddleb.ycor()
    y = y + 20
    paddleb.sety(y)


def paddleb_down():
    y = paddleb.ycor()
    y = y - 20
    paddleb.sety(y)

#score

scorea=0
scoreb=0

#to take user input

wn.listen()
wn.onkeypress(paddlea_up, "w")
wn.onkeypress(paddlea_down, "s")
wn.onkeypress(paddleb_up, "Up")
wn.onkeypress(paddleb_down, "Down")

#main game loop
while True:
    wn.update()
    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy=ball.dy * -0.7

    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy = ball.dy * -0.7

    if ball.xcor()>390:
        ball.setx(390)
        ball.dx=ball.dx * -0.7
        scorea=scorea+1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(scorea,scoreb), align="center", font=("curior", 24, "normal"))

    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx=ball.dx * -0.7
        scoreb=scoreb+1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(scorea,scoreb), align="center", font=("curior", 24, "normal"))

    #paddle and ball collision
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddleb.ycor()+40 and ball.ycor()>paddleb.ycor()-40):
        ball.setx(340)
        ball.dx=ball.dx*-1
    if ( ball.xcor() < -340 and ball.xcor() > -350 ) and (ball.ycor() <paddlea.ycor() + 40 and ball.ycor() > paddlea.ycor() - 40):
        ball.setx(-340)
        ball.dx = ball.dx *- 1