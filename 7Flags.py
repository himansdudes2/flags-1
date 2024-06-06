import turtle
import random

bob = turtle.Turtle()  # give name to a turtle

points = 0
life = 3


def Germany():  # define function which stores drawing of German flag

    bob.fillcolor("black")  # fill the turtle with some color
    bob.begin_fill()  # begin filling with color

    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()  # end filling with color

    bob.pu()
    bob.goto(0, -30)
    bob.pd()

    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.pu()
    bob.goto(0, -60)
    bob.pd()

    bob.fillcolor("yellow")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()

    bob.hideturtle()


def Poland():
    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(50)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -50)
    bob.pd()
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(50)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()


def Italy():
    bob.fillcolor("green")
    bob.begin_fill()
    for i in range(2):
        bob.fd(50)
        bob.rt(90)
        bob.fd(120)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(50, 0)
    bob.pd()
    bob.fillcolor("white")
    bob.begin_fill()
    for i in range(2):
        bob.fd(50)
        bob.rt(90)
        bob.fd(120)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(100, 0)
    bob.pd()
    bob.fillcolor("red")
    bob.begin_fill()
    for i in range(2):
        bob.fd(50)
        bob.rt(90)
        bob.fd(120)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()


def Finland():
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(90)
        bob.rt(90)
    bob.pu()
    bob.fd(30)
    bob.pd()
    bob.color("dark blue")
    bob.begin_fill()
    for i in range(2):
        bob.fd(30)
        bob.rt(90)
        bob.fd(90)
        bob.rt(90)
    bob.end_fill()
    bob.pu()
    bob.goto(0, -30)
    bob.pd()
    bob.begin_fill()
    for i in range(2):
        bob.fd(150)
        bob.rt(90)
        bob.fd(30)
        bob.rt(90)
    bob.end_fill()
    bob.hideturtle()


# put all the drawings into list
flags = [Germany, Poland, Italy, Finland]

# check answers, calculate points and life
while life > 0 and len(flags) > 0:
    bob.reset()  # reset the position of the turtle
    bob.speed(200)  # change the speed of the turtle
    flag = random.choice(flags)  # generate random flag
    flag()
    answer = input("Guess the flag! ")

    if answer == flag.__name__:
        print("Correct answer!")
        points += 1
        print("Points:", points)
        print("Life:", life)
        flags.remove(flag)

    else:
        print("Try again")
        if points > 0:
            points -= 1
        else:
            points = 0
        life -= 1
        print("Points:", points)
        print("Life:", life)

print("GAME OVER")
