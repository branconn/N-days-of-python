from tkinter import *


def calc():
    miles = float(entry.get())
    km = round((miles * 1.609), 1)
    out_label.config(text=km)


window = Tk()
window.minsize(width=200, height=100)
window.config(padx=20, pady=10)
window.title("Mile to Km Converter")

# Input (0,1)
entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=1)

# Miles (0,2)
m_label = Label(text="Miles")
m_label.grid(row=0, column=2)
# is equal to (1,0)
eq_label = Label(text="is equal to")
eq_label.grid(row=1, column=0)

# output label (1,1)
out_label = Label(text="0")
out_label.grid(row=1, column=1)

# Km (1,2)
km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# button (2,1)
button = Button(text="Calculate", command=calc)
button.grid(row=2, column=1)

window.mainloop()
