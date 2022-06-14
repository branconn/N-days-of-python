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
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    reps = 0
    checks.config(text="")
    timer_l.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if (reps % 8 == 0) and (reps != 0):
        count_sec = long_break_sec
        timer_l.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_sec = work_sec
        timer_l.config(text="Work", fg=GREEN)
    else:
        count_sec = short_break_sec
        timer_l.config(text="Break", fg=PINK)
    count_down(count_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    mins = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = f"0{sec}"
    canvas.itemconfig(timer_text, text=f"{mins}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        reps += 1
        num_checks = math.ceil(reps / 2)
        mark = ""
        for _ in range(num_checks):
            mark += "✔"
        checks.config(text=mark)
        start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Labels
timer_l = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35))
timer_l.grid(row=0, column=1)

checks = Label(fg=GREEN)
checks.grid(row=3, column=1)

# Buttons
start_b = Button(text="Start", bg=YELLOW, command=start, highlightthickness=0)
start_b.grid(row=2, column=0)

reset_b = Button(text="Reset", bg=YELLOW, command=reset, highlightthickness=0)
reset_b.grid(row=2, column=2)

# Canvas
# canvas widget: layer things one on another
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))


canvas.grid(row=1, column=1)


window.mainloop()

