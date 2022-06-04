import random
from turtle import Turtle, Screen

list_turtle_color = ["red", "green", "blue", "orange", "black", "brown"]
list_of_turtle = []

screen = Screen()
screen.setup(width=650, height=750)

set_x_position = -200
set_y_position = -340

for turtle_index in range(6):
    make_turtle = Turtle(shape="turtle")
    make_turtle.color(list_turtle_color[turtle_index])
    set_x_position += 55
    make_turtle.penup()
    make_turtle.goto(x=set_x_position, y=set_y_position)
    make_turtle.left(90)
    list_of_turtle.append(make_turtle)

x_line = -175
y_line = -340

# make race line

for tutle_index in range(7):
    make_turtle = Turtle()
    make_turtle.speed(0)
    make_turtle.hideturtle()
    make_turtle.penup()
    make_turtle.goto(x_line, y_line)
    make_turtle.setheading(90)
    make_turtle.pendown()
    make_turtle.forward(680)
    x_line += 55

# make finish line

finish = Turtle(shape="classic")
finish.penup()
finish.goto(x=-210, y=340)
finish.pendown()
finish.forward(400)

race_is_on = False

user_bet = screen.textinput(title="Guess the winner", prompt="red, green, blue, orange, black, or brown").lower()

if user_bet:
    race_is_on = True

while race_is_on:

    for turtles in list_of_turtle:

        if turtles.ycor() > 320:
            race_is_on = False
            the_winner_color = turtles.pencolor()
            if the_winner_color == user_bet:
                print(f"You win, The winner turtle is {the_winner_color}")
            else:
                print(f"You lose, The winner turtle is {the_winner_color}")
            break

        move = random.randint(2, 10)
        turtles.forward(move)

screen.exitonclick()
