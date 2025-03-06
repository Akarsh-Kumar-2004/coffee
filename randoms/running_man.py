import turtle
import random
tiny_turtle = turtle.Turtle()
direction = [0,90,180,270]
screen = turtle.Screen()
tiny_turtle.shape("turtle")
tiny_turtle.color('red')
screen.colormode(255)


def running_man(number_of_repetition):
    for i in range(number_of_repetition):
        r = random.randrange(0,255,10)
        g = random.randrange(0,255,10)
        b = random.randrange(0,255,10)
        tiny_turtle.color(r,g,b)
        tiny_turtle.pensize(10)
        tiny_turtle.speed('fast')
        tiny_turtle.forward(100)
        tiny_turtle.setheading(random.choice(direction))
user_input = int(input("enter number of times the turtle should run: "))
running_man(user_input)


screen.exitonclick()
        