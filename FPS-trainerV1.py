import random
from tkinter import messagebox

lst = ['w', 'a', 's', 'd','<space>','<button-1>','<Double-Button-1>','<Triple-Button-1>']
score = 0
timer = 20

def timerfunc(event=None):
    global timer
    if timer > 0:
        button.destroy()
        timer -= 1
        window.after(1000, timerfunc)
        label1.config(text=f"time remaining: {timer}")
        label.config(text=f"score: {score}")
    elif timer == 0:
        scoreAnswer()

def startUp(event=None):
    timerfunc()
    randomItem()

def randomItem(event=None):
    global score
    lstItem = random.choice(lst)
    if timer > 0:
        label2 = tk.Label(frame,text=lstItem, bg="black", fg="white", font=("danger", 15))
        label2.place(x=random.randint(50, 400), y=random.randint(50, 400))

        if lstItem == 'w':
            window.bind('<KeyPress-w>', lambda event: clear_frame())
            score += 2
        elif lstItem == 'a':
            window.bind('<KeyPress-a>', lambda event: clear_frame())
            score += 2
        elif lstItem == 's':
            window.bind('<KeyPress-s>', lambda event: clear_frame())
            score += 2
        elif lstItem == 'd':
            window.bind('<KeyPress-d>', lambda event: clear_frame())
            score += 2
        elif lstItem == '<space>':
            window.bind('<KeyPress-space>', lambda event: clear_frame())
            score += 2
        elif lstItem == '<button-1>':
            label2.bind('<Button-1>', lambda event: clear_frame())
            score += 1
        elif lstItem == '<Double-Button-1>':
            label2.bind('<Double-Button-1>', lambda event: clear_frame())
            score += 1
        elif lstItem == '<Triple-Button-1>':
            label2.bind('<Triple-Button-1>', lambda event: clear_frame())
            score += 1

def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()
    for i in lst:
        window.unbind(i)
    randomItem()

def scoreAnswer():
    global score, timer
    if score <= 20:
        askYesNo = messagebox.askyesno("Score", f"Your score is {score}" + "\n"+ "speed: old lady" + "\n" + "Would you like to play again?")
    elif score >= 25 and score <= 30:
        askYesNo = messagebox.askyesno("Score", f"Your score is {score}" + "\n"+ "speed: middle aged person" + "\n" + "Would you like to play again?")
    elif score >= 35:
        askYesNo = messagebox.askyesno("Score", f"Your score is {score}" + "\n"+ "speed: sonic" + "\n" + "Would you like to play again?")
    if askYesNo == True:
        timer = 20
        startUp()
    else:
        window.destroy()

import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry("500x500")
window.title("FPS Trainer")

frame = Frame(window)
frame.pack(side="top", fill="both", expand=True)

button = tk.Button(text="click here to start", bg="black", fg="white", width=20, height=5)
button.bind("<Button-1>", startUp)
button.place(relx=0.5, rely=0.5, anchor="center")

label1 = tk.Label(text=f"time remaining: {timer}", bg="black", fg="white", font=("danger", 15), width=45, height=1)
label1.place(relx=0.01, rely=0.01, anchor="nw")

label = tk.Label(text=f"score: {score}", bg="black", fg="white", font=("danger", 15))
label.pack(side="right")

window.mainloop()