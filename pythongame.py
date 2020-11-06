
from tkinter import *
import tkinter.font as font
import tkinter as tk
from tkinter import messagebox
import random
colors = ["Red", "Orange", "White", "Black", "Green", "Blue", "Brown", "Purple", "Cyan", "Yellow", "Pink", "Magenta"]
timer = 60
score = 0
# displayed_word_color = ''
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
    
    # user_name = Label(my_window, text = string, font = app_font, fg= "red", bg="#ffdacc")
    # user_name.pack(pady=10)  



            #LEVEL 2
# This fuction will be called when start button is clicked
def level2():
   global displayed_word_color
   if(timer == 60):
       startCountDown2()
       displayed_word_color = random.choice(colors).lower()
       display_words.config(text=random.choice(colors), fg=displayed_word_color)
       color_entry.bind('<Return>', displayNextWord2)



def startCountDown2():
    global timer
    if(timer >= 0):
        time_left.config(text = "Game Ends in : " + str(timer) + "s")
        timer -= 1
        time_left.after(500,startCountDown2)
        if (timer == -1):
            time_left.config(text="Game Over!!!")

def displayNextWord2(event):
    global displayed_word_color
    global score
    if(timer > 0):
        if(displayed_word_color == color_entry.get().lower()):
            score += 1
            game_score.config(text = "Your Score : " + str(score))
        color_entry.delete(0, END)
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text = random.choice(colors), fg = displayed_word_color)



# def name():


def startGame():
    global displayed_word_color
    if(timer == 60):
        startCountDown()
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text=random.choice(colors), fg=displayed_word_color,bg="#ffdacc")
        color_entry.bind('<Return>', displayNextWord)
# #This function is to reset the game
def resetGame():
    global timer, score, displayed_word_color
    timer = 60
    score = 0
    displayed_word_color = ''
    game_score.config(text = "Your Score : " + str(score))
    #startGame()
    # display_words.config(text=random.choice(colors), fg=displayed_word_color,bg="#ffdacc")
    # display_words.config(text = '')
    time_left.config(text="Game Ends in : --")
    color_entry.delete(END)
#This function will start count down
def startCountDown():
    global timer
    if(timer >= 0):
        if username:
            username_label.config(text = f"Welcome {username}")
            time_left.config(text = "Game Ends in : " + str(timer) + "s")
            timer -= 1
            time_left.after(1000,startCountDown)
            if (timer == -1):
                time_left.config(text="Game Over!!!")
#This function to display random words
def displayNextWord(event):
    global displayed_word_color
    global score
    if(timer > 0):
        if(displayed_word_color == color_entry.get().lower()):
            score += 1
            game_score.config(text = "Your Score : " + str(score))
        color_entry.delete(0, END)
        displayed_word_color = random.choice(colors).lower()
        display_words.config(text = random.choice(colors), fg = displayed_word_color,bg="#ffdacc")
name = tk.Tk()
name.title("username")
name.geometry("300x100")
my_window = Tk()
my_window.title("Color Game")
my_window.geometry("500x200")
#my_window.title('Name')

e = Entry(name)
e.pack()
e.focus_set()

b = Button(name,text='okay',command=printtext)
b.pack(side='bottom')

app_font = font.Font(family='Helvetica', size = 12)

game_desp = "Enter the color of the words displayed below. \n And Keep in mind not to enter the word text itself"

myFont = font.Font(family='Helvetica')

game_description = Label(my_window, text = game_desp, font = app_font, fg= "black", bg="#ffdacc")
game_description.pack()
game_score = Label(my_window, text = "Your Score : " + str(score), font = (font.Font(size=16)), fg = "green",bg="#ffdacc")
game_score.pack()

display_words = Label(my_window , font = (font.Font(size=55)), pady = 10,bg="#ffdacc")
display_words.pack()

time_left = Label(my_window, font = (font.Font(size=14)), fg = "red",bg="#ffdacc")
time_left.pack()

username_label = Label(my_window, font = (font.Font(size=14)), fg = "red",bg="#ffdacc")
username_label.pack()


color_entry = Entry(my_window, width = 30)
color_entry.pack(pady = 10)

btn_frame = Frame(my_window, width= 80, height = 40, bg= 'white')
btn_frame.pack(side = BOTTOM)

start_button = Button(btn_frame, text = "Start", width = 20, fg = "black", bg = "yellow", bd = 12,padx = 20, pady = 10 , command = startGame)
start_button.grid(row=0, column= 0)

start_button = Button(btn_frame, text = "level-2", width = 20, fg = "black", bg = "pink", bd = 12,padx = 20, pady = 10 , command = level2)
start_button.grid(row=0, column= 2)

reset_button = Button(btn_frame, text = "Reset", width = 20, fg = "black", bg = "salmon", bd = 12,padx = 20, pady = 10 , command = resetGame)
reset_button.grid(row=0, column= 1)


my_window.configure(background='#ffdacc')
my_window.geometry('600x300')
my_window.mainloop()