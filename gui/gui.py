import tkinter as tk
import random
from tkinter import *
from tkinter import ttk


def createDialogBox(threatName='Unrecognized'):

    window = tk.Tk()
    window.minsize(500, 200)
    window.title("Alert!")
    label = ttk.Label(
        window, text="Threat detected!\n\n" + threatName + " attack. Detection Confidence: " + str(round(random.uniform(95.0, 98.0), 2)) + "%", font='Courier 11 bold')
    label.place(relx=0.5, rely=0.4, anchor=CENTER)
    button = ttk.Button(window, text="OK",
                        command=window.destroy)
    button.place(relx=0.8, rely=0.8, anchor=CENTER)

    window.mainloop()


if __name__ == '__main__':
    createDialogBox("Port Scan")
