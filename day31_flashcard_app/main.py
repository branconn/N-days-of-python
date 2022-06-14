from tkinter import *
from word_smith import Words
BACKGROUND_COLOR = "#B1DDC6"

words = Words()
word_set = words.current()
word_fr = word_set["French"]
word_en = word_set["English"]


def change_it():
    word_pair = words.cycle()
    word_french = word_pair["French"]
    canvas.itemconfig(img_id, image=img_f)
    canvas.itemconfig(label_id, text="French", fill="black")
    canvas.itemconfig(f_word_id, text=word_french, fill="black")
    nope.grid_forget()
    yep.grid_forget()
    window.after(3000, flip)


def remove_it():
    if words.exile():
        change_it()
    else:
        canvas.itemconfig(label_id, text="You finished all words!")
        canvas.itemconfig(f_word_id, text="Congratulations")
    canvas.itemconfig(count_id, text=f"{words.num_words}/{words.num_tot} words left")


def flip():
    word_pair = words.current()
    word_english = word_pair["English"]
    canvas.itemconfig(img_id, image=img_e)
    canvas.itemconfig(label_id, text="English", fill="white")
    canvas.itemconfig(f_word_id, text=word_english, fill="white")
    nope.grid(row=1, column=0)
    yep.grid(row=1, column=1)


window = Tk()
window.title("Language Flash Card")
window.geometry("900x726")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

window.after(3000, flip)

# 2 row, 2 column layout
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
img_f = PhotoImage(file="./images/card_front.png")
img_e = PhotoImage(file="./images/card_back.png")

# Canvas
french_flipper = True
img_id = canvas.create_image(400, 263, image=img_f)
count_id = canvas.create_text(400, 20, text=f"{words.num_words}/{words.num_tot} words left")
label_id = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
f_word_id = canvas.create_text(400, 263, text=word_fr, font=("Arial", 60, "bold"))

canvas.grid(row=0, column=0, columnspan=2)

# Buttons
no_img = PhotoImage(file="./images/wrong.png")
nope = Button(image=no_img, highlightthickness=0, command=change_it)
# nope.grid(row=1, column=0)
# nope.grid_forget()

yes_img = PhotoImage(file="./images/right.png")
yep = Button(image=yes_img, highlightthickness=0, command=remove_it)
# yep.grid(row=1, column=1)


# leave this at the end
window.mainloop()
