from tkinter import *
import random
from tkinter import messagebox

s=0
root=Tk()
root.geometry("475x275") 
root.title("COLOUR GAME")

label=Label(root, text="Enter the COLOUR of the TEXT to score.",font=("bold", 12)).place(relx=0.5, rely=0.03, anchor='center')
label=Label(root, text="Press SPACE to start.",font=("bold", 12)).place(relx=0.5, rely=0.1, anchor='center')

countdown=Label(root,text="",width=15,font=("bold", 12))
countdown.place(relx=0.5, rely=0.2, anchor='center')

score_label=Label(root, text="",font=("bold", 15))
score_label.place(relx=0.5, rely=0.4, anchor='center')

colourname=Label(root, font=("Courier", 44))
colourname.place(relx=0.5, rely=0.6, anchor='center')

entry=Entry(root,bg="bisque",borderwidth=5)
entry.place(relx=0.5, rely=0.8, anchor='center')

label1=Label(root, text="Press ENTER to submit",font=("bold", 10)).place(relx=0.5, rely=0.9, anchor='center')

colours=['yellow', 'red', 'green', 'blue', 'purple', 'orange', 'brown', 'pink', 'black', 'white']


def change_colour():
    global c
    global d
    c=str(random.choice(colours))
    d=random.choice(colours)
    colourname.configure(text=d, fg=c)
    root.bind('<Return>', score)

def timer():
    global n
    global s
    if n<=0:
        countdown.configure(text="Time's up!")
        messagebox.showinfo("COLOUR GAME", "Your Score:%d" % s)
        root.quit()
    else:
        countdown.configure(text="time left:%d" % n)
        countdown.configure(text="time left:%d" % n)
        countdown.after(1000, timer)
    n=n-1    

def score(event):
    global s
    answer = str(entry.get())
    if answer!= "" and not answer.isspace():
        if c == answer.lower():
            s = s + 1
            score_label.configure(text="Score:%d" % s)
            score_label.configure(text="Score:%d" % s)
        entry.delete(0, END)
        change_colour()

    
def startgame(event):
    entry.focus()
    root.unbind('<space>')
    global n
    n=50
    root.after(0,timer)
    change_colour()


score_label.configure(text="Score:%d" % s)
root.bind('<space>',startgame)

root.mainloop()