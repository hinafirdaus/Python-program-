from turtle import*

def square():
    i=0
    for i in range(4):
        forward(100)
        left(90)

square()
penup()
goto(-100,200)
pendown()
square()
penup()
goto(200,200)
pendown()
square()
