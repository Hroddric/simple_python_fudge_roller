#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
import random as r


root = Tk()
root.title("Simple fudge dice roller")

def roll_dice():
    try:
        number_of_dice = int(numberOfDice.get())
        results = []
        value_sum = 0

        for i in range(number_of_dice):
            result = r.randint(-1,1)
            if result == -1:
                results.append("[-]")
            elif result == 0:
                results.append("[ ]")
            elif result == 1:
                results.append("[+]")
            value_sum += result

        resultLabel = Label(root, text=str(results))
        resultLabel.grid(row=1, column=0, columnspan=2)
        totalLabel = Label(root, text="TOTAL: " + str(value_sum))
        totalLabel.grid(row=2, column=0, columnspan=2)
    except:
        messagebox.showerror("Arguments missing", "Please insert number of dice to be rolled")

numberOfDice = Entry(root)
rollButton = Button(root, text="Roll dice", command=roll_dice)

numberOfDice.grid(row=0, column=0)
rollButton.grid(row=0, column=1)

root.mainloop()