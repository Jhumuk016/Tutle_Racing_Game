import random
from turtle import Turtle, Screen
colors = ["red","blue","green","yellow","orange","purple","black"]

screen = Screen()
# tim = Turtle(shape="turtle")

screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle wins the race enter your color.\n")
print(user_bet)
turtles_list =[]
# tim.penup()
# tim.goto(x=-240,y=-100)
is_race_on = False
for i in range(0,280,40):
    index = int(i/40)
    tim = Turtle(shape="turtle")
    tim.color(colors[index])
    tim.penup()
    tim.goto(x=-240,y=-120+i)
    turtles_list.append(tim)

if user_bet:
    is_race_on=True
while is_race_on:
    for turtle in turtles_list:
        if turtle.xcor()>220:
            is_race_on=False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won, winning color is {winner}")
            else:
                print(f"You lost, winning color is {winner}")


        dist = random.randint(0,10)
        turtle.forward(dist)
screen.exitonclick()