import turtle
import random
tiny_turtle = turtle.Turtle()

screen = turtle.Screen()
tiny_turtle.shape("turtle")
tiny_turtle.color('red')
screen.colormode(255)


def running_man(gap):
    
    for _ in range(int(360 / gap)):
        r = random.randrange(0,255,10)
        g = random.randrange(0,255,10)
        b = random.randrange(0,255,10)
        tiny_turtle.color(r,g,b)
        tiny_turtle.pensize(2)
        tiny_turtle.speed('fastest')
        tiny_turtle.circle(100)
        tiny_turtle.setheading(tiny_turtle.heading() + gap)

user_input = int(input("enter the gap needed in between the circles for a spirograph :"))
running_man(user_input)


screen.exitonclick()
        