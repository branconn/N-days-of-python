# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random as r
import pyperclip
import json


# ---------------------------- SAVE PASSWORD ------------------------------- #
P_PATH = "../ignore/not_passwords.json"


def search():
    user_w = entry_w.get()
    try:
        with open(P_PATH, mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Uh-oh", message="You haven't saved any passwords yet")
    else:
        if user_w in data:
            pw = data[user_w]["password"]
            em = data[user_w]["email"]
            messagebox.showinfo(title=user_w, message=f"Email: {em}\nPassword: {pw}")
        else:
            messagebox.showerror(title="Uh-oh", message=f"You have no password for {user_w}\n(case-sensitive)")


def generate():
    num_letts = 12
    num_caps = 1
    num_spec = 2
    num_digs = 2
    letters = "qwertyuiopasdfghjklzxcvbnm"
    special = "!@#$%&"
    password = ""
    for _ in range(num_letts):
        password += r.choice(letters)
    for _ in range(num_caps):
        password += r.choice(letters).upper()
    for _ in range(num_spec):
        password += r.choice(special)
    for _ in range(num_digs):
        password += str(r.randint(0, 9))
    pw = [char for char in password]
    r.shuffle(pw)
    password = "".join(pw)
    entry_p.delete(0, 'end')
    entry_p.insert(0, password)


def add():
    user_w = entry_w.get()
    user_e = entry_e.get()
    user_p = entry_p.get()

    if user_p == "" or user_e == "" or user_w == "":
        messagebox.showinfo(title="Uh-oh", message="One of your entries is blank.")
    else:
        new_data = {
            user_w: {
                "email": user_e,
                "password": user_p,
            }
        }
        try:
            with open(P_PATH, mode="r") as file:
                # new_line = f"{user_w} | {user_e} | {user_p}\n"
                # json.dump(new_data, file, indent=4)
                data = json.load(file)  # converts to a python dict
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)  # updating old with new
        finally:
            with open(P_PATH, mode="w") as file:
                json.dump(data, file, indent=4)  # saving updated data
            pyperclip.copy(user_p)
            # messagebox.showinfo(title="Yay!", message="Entry saved.\nPassword copied to clipboard")
            entry_p.delete(0, END)
            entry_w.delete(0, END)


def clear_contents():
    user_p = entry_p.get()
    if user_p == "clear contents":
        is_ok = messagebox.askokcancel(title="Confirmation",
                                       message="Are you sure you want to delete all passwords?"
                                               "\nThis cannot be undone.")
        if is_ok:
            # with open("not_passwords.txt", mode="w") as file:
            #     file.write("")
            data = {}
            with open(P_PATH, mode="w") as file:
                json.dump(data, file)
            messagebox.showinfo(message="Them shits deleted")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
# 5 row, 3 column layout
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0, columnspan=3)

gen_p = ""

# Labels
label_w = Label(text="Website:", pady=5)
label_w.grid(row=1, column=0)

label_e = Label(text="Email/Username:", pady=5)
label_e.grid(row=2, column=0)

label_p = Label(text="Password:", pady=5)
label_p.grid(row=3, column=0)

# Entries
entry_w = Entry(width=33)
entry_w.grid(row=1, column=1)

entry_e = Entry(width=53)
entry_e.insert(0, string="test@email.com")
entry_e.grid(row=2, column=1, columnspan=2)

entry_p = Entry(width=33)
entry_p.grid(row=3, column=1)

# Buttons
button_generate = Button(text="Search", command=search, width=15)
button_generate.grid(row=1, column=2)

button_generate = Button(text="Generate Password", command=generate, width=15)
button_generate.grid(row=3, column=2)

button_add = Button(text="Add", width=45, command=add)
button_add.grid(row=4, column=1, columnspan=2)

button_clear = Button(text="☠", command=clear_contents)
button_clear.grid(row=4, column=0)

# leave at the end:
window.mainloop()
