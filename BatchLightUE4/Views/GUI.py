import tkinter
import tkinter.messagebox as msg
from BatchLightUE4.Models.DB import levels_dict
from BatchLightUE4.Controllers.BuildLightUE4 import perforcecheckout, buildmap

# --------
# UI
# --------

class main_tk(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)
        self.parent = parent
        self.env_names = levels_dict
        self.buttons = {}

        self.value = []
        for i in range(levels_dict):
            name = levels_dict.values()
            self.name = tkinter.StringVar()
            self.value.append(self.name)
            print(self.name)
        self.initialize()

    def initialize(self):
        self.grid()

        frame_lvl = tkinter.LabelFrame(self,
                                       text="All Levels",
                                       padx=10,
                                       pady=10)
        frame_lvl.grid(column=0, row=0)
        env_names = self.env_names
        for cle, level in env_names.items():
            self.value = tkinter.StringVar()
            self.buttons[cle] = tkinter.Checkbutton(frame_lvl, text=level,
                                                    variable=self.value,
                                                    # state='active',
                                                    # state='disabled',
                                                    state='normal',
                                                    anchor='w',)
            self.buttons[cle].grid(columnspan=2, sticky='EW')

        self.grid_columnconfigure(0, weight=1)
        self.resizable(True, False)

        separator = tkinter.Label(self)
        separator.grid()

        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,
                              anchor='w',
                              fg='white',
                              bg='blue')
        label.grid(sticky='EW')

        separator = tkinter.Label(self)
        separator.grid()

        btn_select_all = tkinter.Button(self,
                                        text=u'Select All',
                                        command=self.SelectAll)
        btn_select_all.grid(column=0)

        btn_unselect_all = tkinter.Button(self,
                                          text=u'Unselect All',
                                          command=self.UnSelectAll)
        btn_unselect_all.grid()

        button = tkinter.Button(self,
                                text=u'Build Light',
                                command=self.OnButtonClick)
        button.grid()
        separator = tkinter.Label(self)
        separator.grid()

        # Test Zone
        self.checkstate = tkinter.StringVar()
        testcheck = tkinter.Checkbutton(self, text='Test',
                                        variable=self.checkstate,
                                        anchor='w',)
        testcheck.grid(columnspan=2, sticky='EW')
        # print(testcheck.state)
        btn_test = tkinter.Button(self,
                                        text=u'Test Checkbox',
                                        command=self.TestEvent)
        btn_test.grid(column=0)

    # Gestion All Events
    def TestEvent(self):
        text = self.checkstate.get()
        print(self.checkstate.get())
        self.labelVariable.set(text)

    def SelectAll(self):
        for cle in self.buttons.keys():
            self.buttons[cle].select()

    def UnSelectAll(self):
        for cle in self.buttons.keys():
            self.buttons[cle].deselect()

    def OnButtonClick(self):
        self.labelVariable.set("You click the button")

        for cle in levels_dict.keys():
            if levels_dict.get(cle) == self.buttons.get(cle):
                print("Level > ", levels_dict.get(cle))
                print("Buton > ", self.buttons.get(cle))

            print(self.value)
        # if msg.askyesno('Launch Build', 'Lancement du calcul ?'):
        #     perforcecheckout()
        #     buildmap()

    def OnCheck(self):
        # value = self.checkboxVariable.get()
        self.labelVariable.set("value")

# main_tk(None).mainloop()