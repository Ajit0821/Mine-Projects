import turtle
import random
import time
win=turtle.Screen()
win.title("Turtle Racing")
#Finish Line
Finish=turtle.Turtle()
Finish.penup()
Finish.setposition(-380,290)
Finish.pencolor("black")
Finish.pensize(10)
Finish.pendown()
Finish.forward(750)
Finish.speed(0)

#1st Turtle
G=turtle.Turtle()
G.speed(0)
G.shape("turtle")
G.color("purple")
G.penup()
G.left(90)
G.setposition(-300,-200)

A=turtle.Turtle()
A.speed(0)
A.shape("turtle")
A.color("red")
A.penup()
A.setposition(-200,-200)
A.left(90)



#B turtle

B=turtle.Turtle()
B.speed(0)
B.shape("turtle")
B.color("blue")
B.penup()
B.left(90)
B.setposition(-100,-200)

C=turtle.Turtle()
C.speed(0)
C.shape("turtle")
C.color("cyan")
C.penup()
C.setposition(0,-200)
C.left(90)

D=turtle.Turtle()
D.speed(0)
D.shape("turtle")
D.color("green")
D.penup()
D.setposition(100,-200)
D.left(90)

E=turtle.Turtle()
E.speed(0)
E.shape("turtle")
E.color("black")
E.penup()
E.setposition(200,-200)
E.left(90)

F=turtle.Turtle()
F.speed(0)
F.shape("turtle")
F.color("pink")
F.penup()
F.setposition(300,-200)
F.left(90)


time.sleep(1)

for i in range(180):
    A.forward(random.randint(0,5))
    B.forward(random.randint(0,5))
    C.forward(random.randint(0,5))
    D.forward(random.randint(0,5))
    E.forward(random.randint(0,5))
    F.forward(random.randint(0,5))
    G.forward(random.randint(0,5))
turtle
turtle.exitonclick()