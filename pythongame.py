
from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter import messagebox
import random
colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]
timer = 60
score = 0
counter = 0

# givenWordColor = ''
def printtext():
    global e
    global username
    username = e.get()
    # username.bind('<Return>') 
    # user_name.config(text=string)
    if username:
        print("Hi"+username+"!!,Welcome")
        messagebox.showinfo("message","Hi " +username+" !!,Welcome")
        name.destroy()
    else:
        messagebox.showwarning("Alert", "Please enter your name")
    
    #if a=="okay":
    
    # user_name = Label(game, text = string, font = app_font, fg= "red", bg="#ffdacc")
    # user_name.pack(pady=10)  


# def name():


def startGame():
    global givenWordColor
    if(timer == 60):
        startCountDown()
        givenWordColor = random.choice(colors).lower()
        display_words.config(text=random.choice(colors), fg=givenWordColor,bg="#ffdacc")
        color_entry.bind('<Return>', displayNextWord)
# #This function is to reset the game
def resetGame():
    global timer, score, givenWordColor
    timer = 60
    score = 0
    givenWordColor = ''
    game_score.config(text = "Your Score : " + str(score))
    #startGame()
    # display_words.config(text=random.choice(colors), fg=givenWordColor,bg="#ffdacc")
    # display_words.config(text = '')
    time_left.config(text="Game Ends in : --")
    # color_entry.bind('', displayNextWord)
    # color_entry.delete(END)
#This function will start count down
def startCountDown():
    global timer
    if(timer >= 0):
        if username:
            username_label.config(text = f"Welcome {username}")
            time_left.config(text = "Game Ends in : " + str(timer) + "")
            timer -= 1
            time_left.after(1000,startCountDown)
            if (timer == -1):
                time_left.config(text="Game Over!!!")
#This function to display random words
def displayNextWord(event):
    global givenWordColor
    global score
    if(timer > 0):
        if(givenWordColor == color_entry.get().lower()):
            score += 1
            game_score.config(text = "Your Score : " + str(score))
        color_entry.delete(0, END)
        givenWordColor = random.choice(colors).lower()
        display_words.config(text = random.choice(colors), fg = givenWordColor,bg="#ffdacc")
                #LEVEL 2
# This fuction will be called when start button is clicked
def level2():
     resetGame()
    global givenWordColor
    global counter
    counter +=1
    # if counter<4:
       
    print(counter)
    if(timer == 60):
       startCountDown2()
       givenWordColor = random.choice(colors).lower()
       display_words.config(text=random.choice(colors), fg=givenWordColor)
       color_entry.bind('<Return>', displayNextWord2)



def startCountDown2():
    global timer
    if(timer >= 0):
        time_left.config(text = "Game Ends in : " + str(timer) + "s")
        timer -= 1
        # delay = counter*100
        time_left.after(1000-(counter*100),startCountDown2)
        if (timer == -1):
            time_left.config(text="Game Over!!!")

def displayNextWord2(event):
    global givenWordColor
    global score
    if(timer > 0):
        if(givenWordColor == color_entry.get().lower()):
            score += 1
            game_score.config(text = "Your Score : " + str(score))
        color_entry.delete(0, END)
        givenWordColor = random.choice(colors).lower()
        display_words.config(text = random.choice(colors), fg = givenWordColor)
def levelupgrade():
    global counter
    if counter<4:
        level2()
    else:
        timer== -1
        time_left.config(text="you have completed all the levels!!!")

name = tk.Tk()
name.title("username")
name.geometry("300x100")
text_display = Label(name, text = "Enter your name", font = (font.Font(size=16)), fg = "green",bg="#ffdacc")
text_display.pack()
game = Tk()
game.title("Color Game")
game.geometry("500x200")
#game.title('Name')

e = Entry(name)
e.pack()
e.focus_set()

b = Button(name,text='okay',command=printtext)
b.pack(side='bottom')

app_font = font.Font(family='Helvetica', size = 12)

game_desp = "Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself"

myFont = font.Font(family='Helvetica')

game_description = Label(game, text = game_desp, font = app_font, fg= "black", bg="#ffdacc")
game_description.pack()
game_score = Label(game, text = "Your Score : " + str(score), font = (font.Font(size=16)), fg = "green",bg="#ffdacc")
game_score.pack()

display_words = Label(game , font = (font.Font(size=55)), pady = 10,bg="#ffdacc")
display_words.pack()

time_left = Label(game, font = (font.Font(size=14)), fg = "red",bg="#ffdacc")
time_left.pack()

username_label = Label(game, font = (font.Font(size=14)), fg = "red",bg="#ffdacc")
username_label.pack()


color_entry = Entry(game, width = 30)
color_entry.pack(pady = 10)

btn_frame = Frame(game, width= 80, height = 40, bg= 'white')
btn_frame.pack(side = BOTTOM)

start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "yellow", bd = 12,padx = 20, pady = 10 , command = startGame)
start_button.grid(row=0, column= 0)

upgrade_button = Button(btn_frame, text = "Upgrade Level", width = 20, fg = "black", bg = "pink", bd = 12,padx = 20, pady = 10 , command = levelupgrade)
upgrade_button.grid(row=0, column= 2)
if(counter<4):
    upgrade_button=level2
reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "salmon", bd = 12,padx = 20, pady = 10 , command = resetGame)
reset_button.grid(row=0, column= 1)


game.configure(background='#ffdacc')
game.geometry('600x300')
game.mainloop()