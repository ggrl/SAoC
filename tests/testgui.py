import tkinter as tk

from tkinter import ttk

def funktion1():

    print("Funktion 1")

def funktion2():

    print("Funktion 2")

def funktion3():

    print("Funktion 3")

def funktion4():

    print("Funktion 4")

root = tk.Tk()

root.title("Auswahl")

root.attributes("-topmost", True)

root.resizable(False, False)

optionen = {

    "Option 1": ("Button 1", funktion1),

    "Option 2": ("Button 2", funktion2),

    "Option 3": ("Button 3", funktion3),

    "Option 4": ("Button 4", funktion4),

}

auswahl = ttk.Combobox(

    root,

    values=list(optionen.keys()),

    state="readonly",

    width=15

)

auswahl.pack(padx=10, pady=10)

button = tk.Button(root, width=15)

def auswahl_geaendert(event=None):

    name, funktion = optionen[auswahl.get()]

    button.config(

        text=name,

        command=funktion

    )

    button.pack(pady=(0, 10))

auswahl.bind("<<ComboboxSelected>>", auswahl_geaendert)

root.mainloop()