# Day 27: Tkinter, *args, **kwargs and creating GUI programs
from tkinter import *
# NOTES:

# Advanced Python Arguments:
#   we can set default values for arguments, making them optional inputs
#   !

# *Args
def add(*args):  # position matters here
    tote = 0
    for n in args:
        tote += n
    # print(tote)


add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# **Kwargs
def calculate(n, **kwargs):
    # type(**kwargs) == Dictionary
    # for key, value in kwargs.items():
        # print(key)
        # print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)


# calculate(2, add=3, multiply=5)

# Kwarg setup in Class
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        # using get() instead of [] prevents an error and passes a None type


my_car = Car(make="Nissan", model="GTR")
# without both values this will crash if using [] in the class init


# Tkinter built-in module is for making GUIs
# !


window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)  # padding
# Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# we don't see all the options for inputs here.. why? **kwargs
my_label["text"] = "New text"
my_label.config(text="Newer text", padx=20, pady=20)
my_label.grid(column=0, row=0)  # important! Places in screen and centers as default

# Entry
user_t = Entry(width=30)
user_t.insert(0, string="Starting text")
user_t.grid(column=1, row=1)

# Inserted button (grid challenge)

new_button = Button(text="New\nButton")
new_button.grid(column=2, row=0)

# Button
def button_clicked():
    user_text = user_t.get()
    my_label.config(text=user_text)

button = Button(text="Click me", command=button_clicked)
button.grid(column=3, row=2)

# Pack
# works from left to right, top down. Imprecise

# Place
# precise positioning with x and y

# Grid
# basically bootstrap
# item.grid(column=5, row=5)
# you should still work left to right, top down

# stays at the end
window.mainloop()

