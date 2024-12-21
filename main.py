
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Courier"
WORK_MIN = 50
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 40
SECOND = 1000
check_text = ""
rounds = 0
timer_function = None

from tkinter import *

# ---------------------------- TIMER RESET ------------------------------- #
def reset_clock():

    global rounds, check_text, timer_function
    rounds = 0
    check_text = ""

    root.after_cancel(timer_function)
    canvas.itemconfigure(timer, text="00:00")
    title_label.configure(text="Timer", foreground=GREEN, font=(FONT_NAME, 30, "bold"))
    check_marks.configure(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(time_left):

    global rounds, timer_function, check_text
    minute = time_left//60
    second = time_left%60

    if minute<10:
        minute = f"0{minute}"
    if second<10:
        second = f"0{second}"
    canvas.itemconfigure(timer, text=f"{minute}:{second}")

    if time_left>0:
        timer_function = root.after(SECOND, start_timer, time_left-1)
    elif rounds<8:
        start_clock()
    elif rounds==8:
        title_label.configure(text="Pomodoro Completed!", foreground=BLACK)
        rounds = 0
        check_text = ""
        check_marks.configure(text="")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_clock():
    
    global rounds, check_text

    if rounds==7:
        total_time = LONG_BREAK_MIN
        title_label.configure(text="Long Break", foreground=RED)
        check_text = check_text + "✔"
    elif rounds%2==0:
        total_time = WORK_MIN
        title_label.configure(text="Work Period", foreground=PINK)
    else:
        total_time = SHORT_BREAK_MIN
        title_label.configure(text="Short Break", foreground=RED)
        check_text = check_text + "✔"

    check_marks.configure(text=check_text)
    rounds = rounds + 1

    start_timer(total_time*60)

# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
root.title("Pomodoro App")
root.resizable(False, False)
root.config(padx=100, pady=50, bg=YELLOW)

    # ----- The label at the top
title_label = Label(text="Timer", foreground=GREEN, background=YELLOW, font=("courier", 30, "bold"), pady=5)
title_label.grid(row=0, column=1)

    # ----- The canvas with tomato image part
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image1 = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image1)
timer = canvas.create_text(100,130, text="00:00", fill=WHITE, font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)

    # ----- The buttons below the canvas
start = Button(text="Start", highlightthickness=0, command=start_clock)
start.grid(row=2, column=0)

reset = Button(text="Reset", highlightthickness=0, command=reset_clock)
reset.grid(row=2, column=2)

    # ----- The checkbutton below the buttons
check_marks = Label(text="", foreground=GREEN, background=YELLOW)
check_marks.grid(row=3, column=1)

root.mainloop()