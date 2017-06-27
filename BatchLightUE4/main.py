
from BatchLightUE4.Views.GUI import main_tk


class BatchBuildSetup:
    def __init__(self):
        self.nom = 'Build Light Batch'

app_name = BatchBuildSetup().nom

if __name__ == "__main__":
    app = main_tk(None)
    app.title(app_name)
    app.mainloop()
