from turtle import *
speed(1)
color("red")

# I-Shape
up()
goto(-250,125)
down()

pensize(15)
left(180)
forward(133)

right(135)
forward(187)

right(135)
forward(210)

circle(-60,180)
forward(10)

up()
goto(0,0)
down()
# Love-Shape
pensize(3)
begin_fill()
fillcolor("red")
left(50)
forward(180)

circle(-90,200)

setheading(60)
circle(-90,200)

forward(180)
end_fill()

#ICU
up()
goto(0,0)
goto(-200,135)
down()
color("green")
setheading(0)
pensize(7)
forward(150)

pensize(6)
setheading(70)
forward(65)

pensize(5)
setheading(-70)
forward(130)

pensize(4.5)
setheading(70)
forward(120)

pensize(4)
setheading(-70)
forward(55)

pensize(3.5)
setheading(0)
forward(140)

# Top aro of ICU
pensize(3)
setheading(135)
forward(8)

pensize(3)
left(180)
forward(8)

pensize(3)
setheading(225)
forward(8)


#U-Shape
up()
goto(0,0)
goto(260,255)
down()
color("red")
pensize(15)

setheading(270)
forward(175)

circle(70,180)

setheading(90)
forward(175)


hideturtle()
done()
