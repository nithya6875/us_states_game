import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="Whats another state?").title()

    data = pandas.read_csv("50_states.csv")
    all_states = data.state.to_list()

    if answer_state=="Exit":
        missing_sates = []
        for state in all_states:
            if state not in guessed_states:
                missing_sates.append(state)
        new_data = pandas.DataFrame(missing_sates)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_row = data[data.state == answer_state]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(state_row.state.item())


