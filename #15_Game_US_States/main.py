import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"

screen.addshape(image)
# Now are image is available to use as the shape our turtle

turtle.shape(image)

# To get the coordinates where we click
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinates)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 states Correct",
        prompt="What's another state name ?\n Write <exit> to quit  ").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
    else:
        print("Wrong Answer")

# screen.exitonclick()
# turtle.mainloop()
# to keep the screen open, because we using click for other operations
