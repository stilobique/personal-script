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

label = tkinter.Label(fenetre, text="Choose your levels", anchor="w")
label.pack()

# --------
# Add more widget
# --------
for i in range(len(env_names)):
    buttons = tkinter.Checkbutton(fenetre, text=env_names[i])

    buttons.pack()

tkinter.Button(fenetre, text="Build").pack()

fenetre.mainloop()