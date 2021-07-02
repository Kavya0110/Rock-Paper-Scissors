import tkinter
from idlelib import window
from tkinter import *
from tkinter import messagebox
import PIL
from PIL import ImageTk, Image
import random

top = Tk()
top.geometry('500x600+10+10')
top.title("Game")

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""


def choice_to_num(choice):
    rps = {'rock': 0, 'paper': 1, 'scissors': 2}
    return rps[choice]


def num_to_choice(number):
    rps = {0: 'rock', 1: 'paper', 2: 'scissors'}
    return rps[number]


def random_comp_choice():
    random.choice(['rock', 'paper', 'scissor'])
    return


def result(human_choice, comp_choice):
    global USER_SCORE
    global COMP_SCORE

    user = choice_to_num(human_choice)
    comp = choice_to_num(comp_choice)

    if user == comp:
        print("It is a tie")
    elif (user - comp) % 3 == 1:
        print("You win!")
        USER_SCORE += 1
    else:
        print("You Lose, Better luck next time")
        COMP_SCORE += 1
    text_area = Text(master=window, height=12, width=30, bg="#FFFF99")
    text_area.pack()
    answer = "Your choice: {uc} \nComputer's Choice: {cc} \n Your Score: {u} \nComputer's Choice: {c}".format(
        uc=USER_CHOICE, cc=COMP_CHOICE, u=USER_SCORE, c=COMP_SCORE)
    text_area.insert(END, answer)


def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "rock"
    COMP_CHOICE = random.choice(['rock', 'paper', 'scissors'])
    result(USER_CHOICE, COMP_CHOICE)


def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "paper"
    COMP_CHOICE = random.choice(['rock', 'paper', 'scissors'])
    result(USER_CHOICE, COMP_CHOICE)


def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE = "scissors"
    COMP_CHOICE = random.choice(['rock', 'paper', 'scissors'])
    result(USER_CHOICE, COMP_CHOICE)


welcome = Label(top, text="Welcome to the Game!", bg="dark green", fg="white", width=100, height=1).place(x=-90, y=0)

rockimg = ImageTk.PhotoImage(Image.open("rock.png"))
paperimg = ImageTk.PhotoImage(Image.open("paper.png"))
scissorsimg = ImageTk.PhotoImage(Image.open("scissors.png"))
rocklabel = Label(top, image=rockimg, height=150).place(x=0, y=55)
paperlabel = Label(top, image=paperimg).place(x=250, y=30)
scissorslabel = Label(top, image=scissorsimg).place(x=125, y=230)

button1 = Button(top, text="rock", height=2, width=15, bg="yellow").place(x=50, y=430)
button2 = Button(top, text="paper", height=2, width=15, bg="red").place(x=175, y=430)
button3 = Button(top, text="scissors", height=2, width=15, bg="blue").place(x=300, y=430)

top.mainloop()
