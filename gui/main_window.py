import tkinter as tk
import tkinter.font as font
from new_booking import NewBookingWindow


class Window:
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
        self.my_font = font.Font(family='Helvetica', size=12)

        self.new_booking = tk.Button(text='nowa rezerwacja', font=self.my_font, command=NewBookingWindow)
        self.new_booking.place(x='10', y='10')



        self.root.mainloop()


if __name__ == '__main__':
    Window('hotel', '1000x600', is_resize=False)
