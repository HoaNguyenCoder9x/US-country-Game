from turtle import Turtle, Screen
import pandas as pd
from score import ScoreBoard

score = ScoreBoard()
data = pd.read_csv('50_states.csv')
t = Turtle()
s = Screen()
image = 'blank_states_img.gif'
s.addshape(image)
t.shape(image)
s.title('Map game')


answer_list = data.state.to_list()
guess_list = []



while len(guess_list) < len(answer_list):
    answer_input = s.textinput(title='Be a geography',
                               prompt=f"Let's guess the country: {score.score}/{len(answer_list)}").title()
    if answer_input == 'Exit':
        miss_sate = [sa for sa in answer_list if sa != guess_list]
        ai = pd.DataFrame(miss_sate).to_csv('learn_file.txt')
        break

    if answer_input in answer_list:
        guess_list.append(answer_input)
        t = Turtle()
        t.hideturtle()
        state = data[data.state == answer_input]
        t.penup()
        t.goto(int(state.x), int(state.y))
        t.write(answer_input)
        score.increase_score()





