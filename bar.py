import turtle

#Getting Frame
wn=turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer()
#Paddel A

paddle_A=turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape("square")
paddle_A.color("white")
paddle_A.shapesize(stretch_wid=5,stretch_len=1)
paddle_A.penup()
paddle_A.goto(-350,0)

#Paddle B
paddle_B=turtle.Turtle()
paddle_B.speed(-100000)
paddle_B.shape("square")
paddle_B.color("white")
paddle_B.shapesize(stretch_wid=5,stretch_len=1)
paddle_B.penup()
paddle_B.goto(350,0)

#function
def paddle_Aup():
    y=paddle_A.ycor()
    y+=20
    paddle_A.sety(y)

def paddle_Adown():
    y=paddle_A.ycor()
    y-=20
    paddle_A.sety(y)
def paddle_Bup():
    y=paddle_B.ycor()
    y+=20
    paddle_B.sety(y)

def paddle_Bdown():
    y=paddle_B.ycor()
    y-=20
    paddle_B.sety(y)

#keyBoard binding
wn.listen()
wn.onkeypress(paddle_Aup,"w")
wn.onkeypress(paddle_Adown,"s")
wn.onkeypress(paddle_Bup,"Up")
wn.onkeypress(paddle_Bdown,"Down")


#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=2
#pen

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,60)

score_A=0
score_B=0
#Main Game Loop
while True:
    wn.update()
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    #border Checking
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=1
        score_A+=1
        pen.clear()
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=1
        score_B+=1
        pen.clear()
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_B.ycor()+40 and ball.ycor()>paddle_B.ycor()-40):
        ball.setx(340)
        ball.dx*=-1

    if (ball.xcor()<-340 and ball.xcor()>-350) and (ball.ycor()<paddle_A.ycor()+40 and ball.ycor()>paddle_A.ycor()-40):
        ball.setx(-340)
        ball.dx*=-1
    pen.write("Player A:{} Player B:{}.".format(score_A,score_B),align="center",font=("Courier",24,"normal"))
