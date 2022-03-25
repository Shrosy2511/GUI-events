num = 0

def plus():
    global num
    num += 1
    color()

def minus():
    global num
    num -= 1
    color()

def color():
    global num
    label.config(text=num)
    if num == 0:
        window.config(bg="grey")
    elif num > 0:
        window.config(bg="green")
    else:
        window.config(bg="red")

def ColorChange(event):
    window.config(bg="yellow")

def colorRemove(event):
    color()

import tkinter as tk

window = tk.Tk()
window.geometry("300x300")

label = tk.Label(text=f"{num}", bg="black", fg="white", font=("danger", 30))
label.place(relx=0.5, rely=0.5, anchor="center")

button = tk.Button(text="click here for +", bg="black", fg="white", width=20, height=5)
button.config(command=plus)
button.pack(side=tk.TOP)

button1 = tk.Button(text="click here for -", bg="black", fg="white", width=20, height=5)
button1.config(command=minus)
button1.pack(side=tk.BOTTOM)

label.bind("<Enter>", ColorChange)
label.bind("<Leave>", colorRemove)

window.mainloop()


