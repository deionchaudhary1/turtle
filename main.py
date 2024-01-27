import turtle

# create a new turtle object called tommy
tommy = turtle.Turtle() 
# make tommy's initial shape a turtle, look up what other shape turtles can be
tommy.shape("turtle") 
# initialize tommy's draw speed to be 10
tommy.speed(5)

#fill the background green using begin_fill() and end_fill()
#left side
tommy.getscreen().bgcolor('#b51220')
tommy.penup()
tommy.goto(-350,200)
tommy.color('#ffffff')
tommy.begin_fill()
tommy.pendown()
tommy.goto(100,0)
tommy.goto(-350,-200)
tommy.goto(400,-200)
tommy.goto(400,200)
tommy.goto(-350,200)
tommy.end_fill()

tommy.penup()
tommy.goto(-200,200)
tommy.color('#000000')
tommy.begin_fill()
tommy.pendown()
tommy.goto(100,0)
tommy.goto(-200,-200)
tommy.goto(400,-200)
tommy.goto(400,200)
tommy.goto(-200,200)
tommy.end_fill()

tommy.penup()
tommy.goto(100,0)
tommy.color('#118c23')
tommy.begin_fill()
tommy.pendown()
tommy.goto(400,0)
tommy.goto(400,-200)
tommy.goto(-200,-200)
tommy.end_fill()
#circlesfsdfjsldjf
tommy.penup()
tommy.goto(-175,-100)
tommy.pendown()
tommy.color('#000000')
tommy.begin_fill()
tommy.circle(100)
tommy.end_fill()
#cresent
tommy.penup()
tommy.goto(-150,-100)
tommy.pendown()
tommy.color('#b51220')
tommy.begin_fill()
tommy.circle(100)
tommy.end_fill()

tommy.penup()
tommy.goto(-375,-100)
tommy.pendown()
tommy.color('#000000')
tommy.begin_fill()
tommy.circle(100)
tommy.end_fill()
#cresent
tommy.penup()
tommy.goto(-400,-100)
tommy.pendown()
tommy.color('#b51220')
tommy.begin_fill()
tommy.circle(100)
tommy.end_fill()
#star
'''
tommy.color('green')
tommy.begin_fill()
tommy.penup()
tommy.goto(-100,0)
tommy.penup()
tommy.left(60)
tommy.forward(100)
tommy.right(90)
tommy.forward(100)
tommy.left(60)
tommy.forward(100)
tommy.right(150)
tommy.forward(100)

tommy.end_fill()
'''



# make tommy go back home
tommy.penup()
tommy.home()
# change tommy's color to black
tommy.goto(-275,0)
tommy.left(90)
tommy.color('#b51220')
tommy.pendown()

# display some text