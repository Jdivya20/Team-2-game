from tkinter import *
import tkinter.font as font
import random
colors=["Red","Blue","Green","Yellow","Brown","Pink","Cyan","Magenta","Purple","White","Black","Orange"]
timer = 60
score = 0
givenWordColor = ""
def gameStart():#function to start
    # global givenWordColor
    if (timer == 60):
        # startTimer()
        print("hi")
        givenWordColor = random.choice(colors).lower()#displays a random element from the given sequence
        words.config(text = random.choice(colors),fg=givenWordColor)
        enteredcolor.bind('<Enter>',nextdisplayedWord)
    # return gameStart()
game = Tk()
game.title("Color Text Game")
game.geometry("500x200")
game.mainloop()