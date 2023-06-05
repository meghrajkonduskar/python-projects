from tkinter import *
import datetime

# constants
FONT = ('Courier', 10, 'normal')
BACKGROUND_COLOR = "lavender"

# initializing window
window = Tk()
window.geometry("250x350")
window.title("Age Calculator")
window.config(background="lavender")


def calculate():
    """This function takes inputs from the entry fields and returns age."""

    # get input from entry fields
    name = name_entry.get().title()
    year = year_entry.get()
    month = month_entry.get()
    date = date_entry.get()

    # check for valid inputs
    if name.isalpha() and year.isdigit() and month.isdigit() and date.isdigit():
        today = datetime.date.today()
        age = today.year - int(year)
        if today.month < int(month) or today.month == int(month) and today.day < int(date):
            age -= 1
        result.config(text=f"{name}'s age is {age}", foreground='green')
    else:
        result.config(text="Invalid inputs!", foreground='red')


# Name Label
name_label = Label(text="Name:", padx=10, pady=20, font=FONT, background=BACKGROUND_COLOR)
name_label.grid(row=0, column=0)

# Name Entry
name_entry = Entry(font=FONT)
name_entry.grid(row=0, column=1)

# Year Label
year_label = name_label = Label(text="Year:", padx=10, pady=20, font=FONT, background=BACKGROUND_COLOR)
year_label.grid(row=1, column=0)

# Year Entry
year_entry = Entry(font=FONT)
year_entry.grid(row=1, column=1)

# Month Label
month_label = Label(text="Month:", padx=10, pady=20, font=FONT, background=BACKGROUND_COLOR)
month_label.grid(row=2, column=0)

# Month Entry
month_entry = Entry(font=FONT)
month_entry.grid(row=2, column=1)

# Date Label
date_label = Label(text="Date:", padx=10, pady=20, font=FONT, background=BACKGROUND_COLOR)
date_label.grid(row=3, column=0)

# Date Entry
date_entry = Entry(font=FONT)
date_entry.grid(row=3, column=1)

# Submit Button
submit = Button(text="Submit", command=calculate)
submit.grid(row=4, column=0, columnspan=2)

# Label to display result.
result = Label(text="Please enter your details", font=FONT, background=BACKGROUND_COLOR, pady=20)
result.grid(row=5, columnspan=2)

window.mainloop()
