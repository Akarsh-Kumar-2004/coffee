import turtle
import random
tinny_turtle = turtle.Turtle()
tinny_turtle.shape("turtle")
screen = turtle.Screen()
screen.colormode(255)

def tiny_turtle_shape(number_of_sides):
    
    for i in range(3,number_of_sides+1):
        s=0
        angle = 360/i
        r = random.randrange(0,255,10)
        g = random.randrange(0,255,10)
        b = random.randrange(0,255,10)
        tinny_turtle.color(r,g,b)
        while s<i:
            tinny_turtle.forward(100)
            tinny_turtle.right(angle)
            s+=1
    


user_input= int(input("Enter the number of sides you need :"))
tiny_turtle_shape(user_input)
    

screen.exitonclick()
    