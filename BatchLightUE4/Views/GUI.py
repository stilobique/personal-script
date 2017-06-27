import tkinter as tk
import tkinter.messagebox as msg
from BatchLightUE4.Models.DB import levels_dict, levels_rendering
from BatchLightUE4.Controllers.BuildLightUE4 import perforcecheckout, buildmap

# --------
# UI
# --------
class UIBuildMap(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.env_names = levels_dict
        self.buttons = {}
        self.value_checkbox = [0]
        for i in levels_dict.keys():
            self.value_checkbox.append(i)
        self.initialize()

    def initialize(self):
        self.grid()

        tk.Button(self, text=u'Select All', command=self.SelectAll).grid(
            column=0, row=0, padx=5, pady=5, sticky='EW')
        tk.Button(self, text=u'Unselect All',
                  command=self.UnSelectAll).grid(column=1, row=0, padx=5,
                                                 pady=5, sticky='EW')

        frame_lvl = tk.LabelFrame(self,
                                  text="All Levels",
                                  padx=5,
                                  pady=5)
        frame_lvl.grid(columnspan=2)

        self.labelVariable = tk.StringVar()
        label = tk.Label(self, textvariable=self.labelVariable, anchor='w')
        label.grid(sticky='EW')

        tk.Label(frame_lvl, text='---- Gymnasium', anchor='w').grid(
            columnspan=2, sticky='EW')

        env_names = self.env_names
        for cle, level in env_names.items():
            self.value_checkbox[cle] = tk.BooleanVar(self, '0')
            self.buttons[cle] = tk.Checkbutton(frame_lvl, text=level,
                                                variable=self.value_checkbox[cle],
                                                anchor='w')
            self.buttons[cle].grid(columnspan=2, sticky='EW')

            if level[0] == 'GYM02':
                tk.Label(frame_lvl, text='---- Stadium', anchor='w').grid(
                    columnspan=2, sticky='EW')

            if level[0] == 'STA09':
                tk.Label(frame_lvl, text='---- Training Cour',
                         anchor='w').grid(
                    columnspan=2, sticky='EW')

        # ------------------------------------------------
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

        tk.Button(self,
                  text=u'Build Light',
                  command=self.OnButtonClick).grid(columnspan=2,
                                                   sticky='EW',padx=5, pady=5,)


    def SelectAll(self):
        for cle in self.buttons.keys():
            self.buttons[cle].select()
        self.labelVariable.set("Select all Levels")

    def UnSelectAll(self):
        for cle in self.buttons.keys():
            self.buttons[cle].deselect()
        self.labelVariable.set("Clear list selection")

    def OnButtonClick(self):
        text = ""
        for key, value in self.buttons.items():
            check = self.value_checkbox[key].get()
            if check is True:
                levels_rendering.append(key)
                nbr = len(levels_rendering)
                text = "Build "
                text = text + str(nbr) + " level(s)"
            elif len(levels_rendering) == 0:
                text = "Empty Choice"

        print(levels_rendering)
        self.labelVariable.set(text)
        if msg.askyesno('Launch Build', 'Lancement du calcul ?'):
            # perforcecheckout()
            buildmap(levels_rendering)