num = 0
divide = False

def plus(event=None):
    global num, divide
    num += 1
    divide = True
    color()

def minus(event=None):
    global num, divide
    divide = False
    num -= 1
    color()

def color(event=None):
    global num
    label.config(text=f"{num:.0f}")
    if num == 0:
        window.config(bg="grey")
    elif num > 0:
        window.config(bg="green")
    else:
        window.config(bg="red")

def ColorChange(event=None):
    window.config(bg="yellow")

def divideBy3(event=None):
    global num, divide, label
    if divide == True:
        num = num * 3
        label.config(text=f"{num:.0f}")
    elif divide == False:
        num = num / 3
        label.config(text=f"{num:.0f}")
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
label.bind("<Leave>", color)
label.bind("<Double-Button-1>", divideBy3)

window.bind("=", plus)
window.bind("-", minus)
window.bind("<space>", divideBy3)

window.mainloop()