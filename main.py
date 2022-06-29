import turtle
import pandas

screen = turtle.Screen()
screen.title("US states game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []
missing_states = []
game_on = True
while game_on:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct", prompt="What's another state name?").title()
    data = pandas.read_csv("50_states.csv")

    if answer_state == "Exit":
        for state in data.state:
            if state not in guessed_states:
                missing_states.append(state)

        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("learn.cvs")

        break


    for state in data.state:
        if answer_state == state:
            state_name = turtle.Turtle()
            state_name.hideturtle()
            state_name.penup()
            state_name.color("black")
            coordinations = data[data.state == answer_state]
            x = int(coordinations.x)
            y = int(coordinations.y)
            state_name.goto(x, y)
            state_name.write(arg=answer_state, align="center",font=("arial", 10, "normal"))
            guessed_states.append(answer_state)

    if len(guessed_states) == 50:
        game_on = False




