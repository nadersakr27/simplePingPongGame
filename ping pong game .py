import turtle
ban = 4
na = 3

ban2 = 4
wind = turtle.Screen() 
wind.title(" ping pong ")
wind.bgcolor("green")
wind.setup(width=800 , height=600)
wind.tracer(0)
madriab1 = turtle.Turtle()
madriab1.speed (0)
madriab1.shape("square")
madriab1.color("blue")
madriab1.shapesize(stretch_wid= 4 , stretch_len=1)
madriab1.penup()
madriab1.goto(-350,0)

madriab2 = turtle.Turtle()
madriab2.speed (0)
madriab2.shape("square")
madriab2.color("red")
madriab2.penup()
madriab2.shapesize(stretch_wid= 4 , stretch_len=1 )
madriab2.goto(350,0)
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("black")
score.penup()
score.hideturtle()
score.goto(0,240)  
score.write("0 . 0" , align="center" , font =("courter",24,"normal"))
khat = turtle.Turtle()
khat.shape("square")
khat.color("white")
khat.penup()
khat.shapesize(stretch_len=0.2 , stretch_wid= 2)
khat.goto(0,260)
ball = turtle.Turtle()
ball.speed (0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4
def madriab1_up ():
    y = madriab1.ycor()
    y += 40
    madriab1.sety (y)
wind.onkeypress( madriab1_up , "w")
def madriab1_down ():
    y = madriab1.ycor()
    y -= 40
    madriab1.sety (y)
wind.listen()
wind.onkeypress( madriab1_down , "s")
def madriab2_up ():
    y = madriab2.ycor()
    y += 40
    madriab2.sety (y)
wind.onkeypress( madriab2_up , "Up")
def madriab2_down ():
    y = madriab2.ycor()
    y -= 40
    madriab2.sety (y)
wind.listen()
wind.onkeypress( madriab2_down , "Down")
while True:
    wind.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < madriab2.ycor() + 10 * ban and ball.ycor() > madriab2.ycor() -10*ban :
       ball.setx(340)
       ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < madriab1.ycor() + 10*ban2  and ball.ycor() > madriab1.ycor() - 10*ban2:
       ball.setx(-340)
       ball.dx *= -1
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
       ball.goto(0,0)
       ball.dx *= -1
       score1 += 1
       score.clear()
       score.write("{} . {}".format(score1, score2) , align="center" , font =("courter",24,"normal"))
       ban +=1 
    if ban > 10 :
       ban = 10
    if ban < 10 :
       
       madriab1.shapesize(stretch_wid = ban , stretch_len=1)  
    if ball.xcor() < -390:
       ball.goto(0,0)
       ball.dx *= -1
       score2 += 1
       score.clear()
       score.write("{} . {}".format(score1, score2) , align="center" , font =("courter",24,"normal"))
       ban2 +=1
    if ban2 >10 :
       ban2 = 10
    if ban2 < 10:
       madriab2.shapesize(stretch_wid = ban2 , stretch_len=1)
    if score1 == na or score2 == na and na < 12:
        ball.dx += -0.05
        ball.dy += -0.05
        na = na + 3
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < madriab2.ycor() + 10 * ban and ball.ycor() > madriab2.ycor() -10*ban :
       ball.setx(340)
       ball.dx *= -1
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < madriab1.ycor() + 10*ban2  and ball.ycor() > madriab1.ycor() - 10*ban2:
       ball.setx(-340)
       ball.dx *= -1    
    if score1 == 10 :
        score.clear()
        score.color("blue")
        score.write("BLUE WINS" , align="center" , font =("courter",24,"normal"))
        khat.hideturtle()
        ball.sety (0)
        ball.setx (0)
    if score2 == 10 :
        score.clear()
        score.color("red")
        score.write("RED WINS" , align="center" , font =("courter",24,"normal"))
        khat.hideturtle()
        ball.sety (0)
        ball.setx (0)