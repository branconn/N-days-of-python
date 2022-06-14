import pandas as pd
import turtle
from state_control import State

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
states = State()

state_list = pd.read_csv("50_states.csv")
all_states = state_list.state.to_list()

correct = 0
game_on = True
while game_on:
    answer = screen.textinput(title=f"{correct}/50 Guess The State", prompt="What's another state's name?").title()

    if answer == "Exit":
        game_on = False
    elif answer in all_states:
        state_row = state_list[state_list.state == answer]
        coor = (float(state_row.x), float(state_row.y))
        states.label(answer, coor)
        all_states.remove(answer)
        correct += 1

panda_states = pd.Series(all_states)
panda_states.to_csv("states_to_learn.csv")
# screen.exitonclick()
