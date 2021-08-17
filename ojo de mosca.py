
from turtle import *

setup(1800, 900 ,0,0)
title("ojo de mosca")
#wn = turtle.Screen()
#wn.bgcolor("black")
#wn.title("ojo de mosca")
color('black', 'orange')
begin_fill()
while True:
    hideturtle()
    pensize(2)
    forward(300)
    left(220)
    if abs(pos()) < 1:
        break
end_fill()
done()



