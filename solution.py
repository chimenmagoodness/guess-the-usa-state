import turtle
import pandas

# get hold of the csv file
data_file = pandas.read_csv("50_states.csv")
# the screen
screen = turtle.Screen()
turtle.penup()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_state = []
score = 0
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's Another State's Name?").title()

    # Check for missing states
    if answer_state == "Exit".title():
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        # giving the user state to learn when they exit
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Check if the user's answer is in the states list and they got it right
    if answer_state in all_states:
        # Adding the correct user guess to a list
        guessed_state.append(answer_state)
        # Check if the state have been guessed before
        number_of_guesses = guessed_state.count(answer_state)
        print(number_of_guesses)
        if number_of_guesses > 1:
            score += 0
        else:
            score += 1
            text = turtle.Turtle()
            text.penup()
            text.hideturtle()
            state_data = data[data.state == answer_state]
            text.goto(int(state_data.x), int(state_data.y))
            text.write(answer_state)
            # text.write(state_data.state.item())


screen.exitonclick()