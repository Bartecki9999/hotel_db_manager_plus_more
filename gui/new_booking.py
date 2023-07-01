import tkinter as tk

class NewBookingWindow:
    def __init__(self, title: str = 'Default title', size: "str XXxYY" = '10x10', is_resize: bool = False):
        self.root = tk.Tk()
        self.myTitle = title
        self.mySize = size
        self.isResize = is_resize

        self.configure_gui()
        self.make_widgets()

    def configure_gui(self):
        self.root.title(self.myTitle)
        self.root.geometry(self.mySize)
        self.root.resizable(self.isResize, self.isResize)

    def make_widgets(self):





        self.root.mainloop()


def booking_window():
    NewBookingWindow('nowa rezerwacja', '1000x600', is_resize=False)


