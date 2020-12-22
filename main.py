from tkinter import Tk, Button, Canvas, Label, PhotoImage
import winsound
import sys
import os
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
reps = 1


# ---------------------------- Helper Function -------------------------- #

def raise_above_all():
    """
    pop up in front of all window screens
    """
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """
    Reset the timer
    """
    global reps
    reps = 1
    window.after_cancel(timer)
    header.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="I <3 you", fill=RED)
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    """
    Start the timer
    """
    global reps
    if reps ^ 1 != reps+1:  # odds time
        # working time
        header['fg'] = GREEN
        header['text'] = "Working"
        count_down(25*60)
    elif reps == 8:
        header.config(text="Long Break", fg=RED)
        count_down(20*60)
    else:
        header.config(text="Break", fg=PINK)
        count_down(5*60)
        check_mark['text'] += "✔"
    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """
    It's a final count down.
    Counting down time
    """
    global timer
    minutes = count//60
    if minutes < 10:
        minutes = f"0{minutes}"
    second = count % 60
    if second < 10:
        second = "0" + str(second)

    # print(f"minutes: {minutes}, second: {second}")
    canvas.itemconfig(timer_text, text=f"{minutes}:{second}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        for _ in range(3):
            winsound.Beep(3500, 100)
        start_timer()
        raise_above_all()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer text label
header = Label(text="Timer", font=(FONT_NAME, 24, "bold"), fg=GREEN, highlightthickness=0, bg=YELLOW)
header.grid(row=0, column=1)

# tomato
canvas = Canvas(width=208, height=224, bg=YELLOW, highlightthickness=0)
# read img in tk
path = resource_path("C:/StudyingandExaminations/Python/100Days project/Day28/Pomodoro/img/tomato.png")
print(path)
img_tomato = PhotoImage(file=path)
canvas.create_image(101, 112, image=img_tomato)
timer_text = canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
canvas.grid(row=1, column=1)

# start button
start_button = Button(text="Start", font=(FONT_NAME, 10, "normal"), command=start_timer)
start_button.grid(row=2, column=0)
# reset button
reset_button = Button(text="Reset", font=(FONT_NAME, 10, "normal"), command=reset_timer)
reset_button.grid(row=2, column=2)

# Check mark text Label
check_mark = Label(text="", fg=GREEN, font=(FONT_NAME, 10, "bold"), highlightthickness=0, bg=YELLOW)
check_mark.grid(row=3, column=1)

#
window.mainloop()
