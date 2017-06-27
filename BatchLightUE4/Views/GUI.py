import tkinter as tk
import tkinter.messagebox as msg
from BatchLightUE4.Models.DB import levels_dict
from BatchLightUE4.Controllers.BuildLightUE4 import perforcecheckout, buildmap

# --------
# UI
# --------
class main_tk(tk.Tk):
    def __init__(self, parent):
        tk.Tk.__init__(self, parent)
        self.parent = parent
        self.env_names = levels_dict
        self.buttons = {}
        self.value_checkbox = [1,2,3,4,5,6,7,8,9,10,11]
        self.check_on = []
        self.check_off = []
        self.initialize()

    def initialize(self):
        self.grid()

        frame_lvl = tk.LabelFrame(self,
                                  text="All Levels",
                                  padx=10,
                                  pady=10)
        frame_lvl.grid(column=0, row=0)

        self.labelVariable = tk.StringVar()
        label = tk.Label(self, textvariable=self.labelVariable,
                         anchor='w',
                         fg='white',
                         bg='blue')
        label.grid(sticky='EW')

        env_names = self.env_names
        for cle, level in env_names.items():
            self.value_checkbox[cle] = tk.BooleanVar(self, '0')
            self.buttons[cle] = tk.Checkbutton(frame_lvl, text=level,
                                                variable=self.value_checkbox[cle],
                                                anchor='w')
            self.buttons[cle].grid(columnspan=2, sticky='EW')

        # ------------------------------------------------
        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

        separator = tk.Label(self)
        separator.grid()

        separator = tk.Label(self)
        separator.grid()

        btn_select_all = tk.Button(self,
                                   text=u'Select All',
                                   command=self.SelectAll)
        btn_select_all.grid(column=0)
        btn_unselect_all = tk.Button(self,
                                     text=u'Unselect All',
                                     command=self.UnSelectAll)
        btn_unselect_all.grid()

        button = tk.Button(self,
                           text=u'Build Light',
                           command=self.OnButtonClick)
        button.grid()


    def SelectAll(self):
        for cle in self.buttons.keys():
            self.buttons[cle].select()

    def UnSelectAll(self):
        for cle in self.buttons.keys():
            self.buttons[cle].deselect()

    def OnButtonClick(self):
        self.labelVariable.set("You click the button")

        for key, value in self.buttons.items():
            check = self.value_checkbox[key].get()
            if check is True:
                print("Key Valid", key)
            else:
                print("Key Non Valid, don't rendering", key)
            # if value[str(key)].get():
            #     print("Cle Get", key)
            # if levels_dict.get(cle) == self.buttons.get(cle):
            #     print("Level > ", levels_dict.get(cle))
            #     print("Buton > ", self.buttons.get(cle))

        # if msg.askyesno('Launch Build', 'Lancement du calcul ?'):
        #     perforcecheckout()
        #     buildmap()

    # def OnCheck(self):
    #     nbr = self
    #     print(self.buttons.keys(nbr))
    #     print("Nom variable > ", self.value_checkbox[nbr].get)
        # value = self.value_checkbox.get()
        # print(value)
        # for i in range(len(self.buttons)):
        #     print(self.buttons[i])
            # state = self.buttons[i]
            # value = state
            # print(value)
        # for key, value in self.buttons.items():
        #     if not value.get():
        #         print('trerr')
            # nbr = self.buttons[i]
            # self.labelVariable.set(str(nbr))
            # print("btn > ", nbr)
            # print("Iteration > ", i)

# main_tk(None).mainloop()