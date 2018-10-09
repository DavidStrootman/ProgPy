import config
from nsapi import NSApi
from tkinter import *
from tkinter.messagebox import showinfo
import dateutil.parser


class App:
    def __init__(self, root):
        # Setup NSApi
        self.api = NSApi(config.NSAPI_USERNAME, config.NSAPI_PASSWORD)

        # Load stations
        self.stations = self.api.get_stations()

        # Setup Tkinter
        self.root = root
        root.title("NS Vertrektijden")
        root.resizable(False, False)

        Label(master=root, text="Vertrekstation").grid(row=0, column=0, pady=4)

        self.txtVertrekstation = Entry(master=root)
        self.txtVertrekstation.grid(row=0, column=1, pady=4)

        Button(master=root, text="Toon tijden", command=self.update_timetable).grid(
            row=0, column=2, pady=4
        )
        Label(master=root, text="Vertrektijden", font="Helvetica 18 bold").grid(
            row=1, column=0, pady=4
        )

        self.lblTijd1 = Label(master=root)
        self.lblTijd1.grid(row=2, column=0, pady=4)
        self.lblTijd2 = Label(master=root)
        self.lblTijd2.grid(row=3, column=0, pady=4)
        self.lblTijd3 = Label(master=root)
        self.lblTijd3.grid(row=4, column=0, pady=4)
        self.lblTijd4 = Label(master=root)
        self.lblTijd4.grid(row=5, column=0, pady=4)
        self.lblTijd5 = Label(master=root)
        self.lblTijd5.grid(row=6, column=0, pady=4)

    def update_timetable(self):
        def get_time_string(str):
            dt = dateutil.parser.parse(str)
            return dt.strftime("%H:%M")

        entryText = self.txtVertrekstation.get()
        if entryText not in self.stations:
            showinfo("Error", "Dit station bestaat niet!")
            return

        tijden = self.api.actuele_vertrektijden(entryText)
        x = tijden["ActueleVertrekTijden"]["VertrekkendeTrein"]

        self.lblTijd1.config(text=get_time_string(x[0]["VertrekTijd"]))
        self.lblTijd2.config(text=get_time_string(x[1]["VertrekTijd"]))
        self.lblTijd3.config(text=get_time_string(x[2]["VertrekTijd"]))
        self.lblTijd4.config(text=get_time_string(x[3]["VertrekTijd"]))
        self.lblTijd5.config(text=get_time_string(x[4]["VertrekTijd"]))


def main():
    root = Tk()
    app = App(root)

    # Start Tkinter main loop
    root.mainloop()


if __name__ == "__main__":
    main()
