from tkinter import *
import tkinter.font as font
import random
game = Tk()
game.title("Color Text Game")
game.geometry("500x200")
game.configure(background='#008B8B')
colors=["Red","Blue","Green","Yellow","Brown","Pink","Cyan","Magenta","Purple","White","Black","Orange"]
timer = 60
score = 0
givenWordColor = ""
app_font = font.Font(family='goergia', size = 12)
game_desp = "Game Description: Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself"
myFont = font.Font(family='Helvetica')
game_description = Label(game, text = game_desp, font = app_font, fg= "#dc143c",bg="#008B8B")
game_description.pack()
game_score = Label(game, text = "Your Score : " + str(score), font = (font.Font(size=16)), fg = "green",bg="#008B8B")
game_score.pack()

display_words = Label(game , font = (font.Font(size=28)), pady = 10)
display_words.pack()
enteredcolor = Entry(game, width = 30)
enteredcolor.pack(pady = 10)

time_left = Label(game, text = "Game Ends in : -", font = (font.Font(size=14)), fg = "red",bg="#008B8B")
time_left.pack()
current_level = Label(game, text = "your current level : -", font = (font.Font(size=14)), fg = "red",bg="#008B8B")
current_level.pack()
# def gameStart():#function to start
#     # global givenWordColor
#     if (timer == 60):
#         startTimer()
#         print("hi")
#         givenWordColor = random.choice(colors).lower()#displays a random element from the given sequence
#         words.config(text = random.choice(colors),fg=givenWordColor)#used to access attributes of an object after initialization
#         enteredcolor.bind('<Return>',nextdisplayedWord)
    # return gameStart()

#This fuction will be called when start button is clicked
def startGame(timer=None,level=None):
    global givenWordColor
    if(timer):
        startCountDown(timer=timer, level=level)
        givenWordColor = random.choice(colors).lower()
        display_words.config(text=random.choice(colors), fg=givenWordColor)
        enteredcolor.bind('<Return>', displayNextWord)
#This function is to reset the game
def resetGame():
    global timer, score, givenWordColor
    timer = 60
    score = 0
    givenWordColor = ''
    game_score.config(text = "Your Score : " + str(score))
    display_words.config(text = '')
    time_left.config(text="Game Ends in : -")
    enteredcolor.delete(0, END)
#This function will start count down
def startCountDown(timer=None,level=None):
    # global timer
    if(timer >= 0):
        time_left.config(text = "Game Ends in : " + str(timer) + "s")
        current_level.config(text = "your current level is : " + str(level))
        timer -= 1
        time_left.after(1000,startCountDown)
        if (timer == -1):
            time_left.config(text="Game Over!!!")
#This function to display random words
def displayNextWord(event):
    global givenWordColor
    global score
    if(timer > 0):
        if(givenWordColor == enteredcolor.get().lower()):
            score += 1
            game_score.config(text = "Your Score : " + str(score))
        enteredcolor.delete(0, END)
        givenWordColor = random.choice(colors).lower()
        display_words.config(text = random.choice(colors), fg = givenWordColor)
def startgameprocess():
    timer=60
    for level in range(1,4):
        startGame(timer=(timer//level),level=level)
    next_level = Button(btn_frame, text = "next level", width = 20, fg = "black", bg = "orange", bd = 0,padx = 20, pady = 10 , command = startgameprocess)
    next_level.grid(row=0, column= 1) 

# btn_frame = Frame(game, width= 80, height = 40, bg= 'red')
btn_frame=Frame(game)
btn_frame.pack(side = BOTTOM)
start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "violet", bd = 0,padx = 20, pady = 10 , command = startgameprocess)
start_button.grid(row=0, column= 0)
reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "orange", bd = 0,padx = 20, pady = 10 , command = resetGame)
reset_button.grid(row=0, column= 1)
game.geometry('600x300')

game.mainloop()
