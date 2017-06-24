import tkinter

# --------
# Data Example
# --------

env_names = [
    'Gymnasium',
    'Stadium',
    'Training Courts'
]

# --------
# UI
# --------
fenetre = tkinter.Tk()

label = tkinter.Label(fenetre, text="Hello World")
label.pack()

# --------
# Add more widget
# --------
for i in range(len(env_names)):
    buttons = tkinter.Checkbutton(fenetre, text=env_names[i])

    buttons.pack()

fenetre.mainloop()