# import package
from turtle import*

# loop for pattern
for i in range(4):
	
    # motion
    forward(100)
    right(90)
    forward(20)
    right(90)
    forward(100)
            
    # set the y cordinate
    up()
    sety(-40*(i+1))
    down()
            
    # change the direction
    left(180)
