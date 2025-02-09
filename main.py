import tkinter
from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = ""
marks = ""
timer_running = False

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer_running
    timer_running = False
    start_button.config(state=NORMAL)
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00", font=(FONT_NAME,28,"bold"))
    my_label.config(text="Timer", font=(FONT_NAME,"38","bold"), bg=YELLOW,fg=GREEN)
    check_mark.config(text = "")
    global reps
    global marks
    marks = ""
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps, timer_running
    if not timer_running:  # Prevent multiple clicks
        timer_running = True
        start_button.config(state=DISABLED)
    reps +=1
    timer_running = True

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        my_label.config(text="Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        my_label.config(text="Break",fg=PINK)
        count_down(short_break_sec)
    else:
        my_label.config(text="Work",fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer = window.after(1000, count_down,count-1)
    else:
        start_timer()
        if reps % 2 == 0:
            global marks
            marks+="✓"
            check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady=50, bg=YELLOW)

my_label = tkinter.Label(text="Timer", font=(FONT_NAME,"38","bold"), bg=YELLOW,fg=GREEN)
my_label.grid(row= 0, column = 1, padx=20,pady=10)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(103,130,text="00:00", fill="white", font=(FONT_NAME,28,"bold"))
canvas.grid(row= 1, column = 1, padx=20,pady=10)


start_button = tkinter.Button(text="Start", font=("",12,"bold"),fg="green", bg="#FFD95F", command=start_timer)
start_button.grid(row=2,column=0,padx=0,pady=10)


check_mark = tkinter.Label(font=("",25,""), bg=YELLOW, fg=GREEN)
check_mark.grid(row=2,column=1, padx=0,pady=10)

reset_button = tkinter.Button(text="Reset", font=("",12,"bold"), fg=RED, bg="#FFD95F", command=reset_timer)
reset_button.grid(row=2,column=2,padx=0,pady=10)


window.mainloop()
