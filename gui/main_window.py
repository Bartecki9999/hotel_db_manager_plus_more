import tkinter as tk
import tkinter.font as font
from gui.new_booking import booking_window
from data_base import DataBase


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
        self.new_booking = tk.Button(text='   nowa rezerwacja   ', font=self.my_font, command=booking_window)
        self.new_booking.grid(row=1, column=0)

        self.free_rooms = tk.Button(text='      wolne pokoje      ', font=self.my_font, command=booking_window)
        self.free_rooms.grid(row=3, column=0)

        self.free_rooms = tk.Button(text='wyszukaj rezerwacje', font=self.my_font, command=booking_window)
        self.free_rooms.grid(row=5, column=0)

        refresh_button = tk.Button(text='↻', command=booking_window)
        refresh_button.grid(column=12, row=0)

        def back():
            for i in range(50):
                self.background = tk.Label(background='#D3D3D3', height=2, width=50)
                self.background.grid(row=i, column=1)

        def upcoming_bookings():

            arrival_date = tk.Label(text='data przyjazdu')
            arrival_date.grid(row=1, column=2)

            for i in range(1, 20):
                l = tk.Label(text='|')
                l.grid(row=i, column=3)

            departure_date = tk.Label(text='data wyjazdu')
            departure_date.grid(row=1, column=4)

            for i in range(1, 20):
                l = tk.Label(text='|')
                l.grid(row=i, column=5)

            first_name = tk.Label(text='      imie      ')
            first_name.grid(row=1, column=6)

            for i in range(1, 20):
                l = tk.Label(text='|')
                l.grid(row=i, column=7)

            last_name = tk.Label(text='    nazwisko    ')
            last_name.grid(row=1, column=8)

            for i in range(1, 20):
                l = tk.Label(text='|')
                l.grid(row=i, column=9)

            room_number = tk.Label(text=' nr. pokoju ')
            room_number.grid(row=1, column=10)

            for i in range(1, 20):
                l = tk.Label(text='|')
                l.grid(row=i, column=11)

            number_of_people = tk.Label(text='ilosc os.')
            number_of_people.grid(row=1, column=12)

            r = DataBase().get_closest_arrivals()
            for i in range(len(r)):
                z = 0
                for j in range(len(r[i])):
                    z += 2
                    l = tk.Label(text=r[i][j]).grid(column=z, row=2+i)



        back()
        upcoming_bookings()

        self.root.mainloop()


if __name__ == '__main__':
    Window('hotel', '1000x600', is_resize=False)
