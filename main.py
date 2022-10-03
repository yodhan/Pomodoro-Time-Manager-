from cgitb import text
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdcac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timerVariable=None

root=Tk()
root.config(bg=YELLOW, padx=50,pady=50 )
root.title("Time Manager")
count=0
def setTimer():
    global count
    count+=1
    shortBreak= SHORT_BREAK_MIN*60
    longBreak=LONG_BREAK_MIN*60
    work=WORK_MIN*60

    if count%8==0:
        heading.config(text="Long Break", fg=RED)
        updateTimer(longBreak)
    elif count%2==0:
        heading.config(text="Short Break", fg=PINK)
        updateTimer(shortBreak)
    else:
        heading.config(text="Work")
        updateTimer(work)

def updateTimer(seconds):
    count_in_mins=seconds//60
    count_in_seconds=seconds%60
    if count_in_seconds<10:
        count_in_seconds=f"0{count_in_seconds}"

    canvas.itemconfig(tm, text=f"{count_in_mins}:{count_in_seconds}")

    if seconds>0:
        global timerVariable
        timerVariable=root.after(1000,updateTimer,seconds-1)
    else:
        tick.config(text=(tickmark*(count//2)))
        setTimer()


def resetTimer():
    root.after_cancel(timerVariable)
    heading.config(text="Timer")
    canvas.itemconfig(tm,text="00:00")
    tick.config(text="")
    global count
    count=0

heading=Label(text="TIMER", fg=GREEN ,bg=YELLOW,highlightthickness=0, font=(FONT_NAME,50))
heading.grid(column=1, row=0)

canvas=Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato )
tm=canvas.create_text(100,130,text="00:00",fill="white" ,font=(FONT_NAME,28,"bold"))
canvas.grid(column=1,row=1)



startbtn=Button(text="Start",highlightthickness=0, command=setTimer)
startbtn.grid(column=0,row=2)

Resetbtn=Button(text="Reset",highlightthickness=0, command=resetTimer)
Resetbtn.grid(column=2,row=2)

tickmark="✔"
tick=Label(text=tickmark,fg=GREEN)
tick.grid(row=3,column=1)
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
root.mainloop()