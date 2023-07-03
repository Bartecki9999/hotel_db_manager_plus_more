import tkinter as tk
import tkinter.font as font
from gui.new_booking import booking_window
from data_base import DataBase
from tkinter import messagebox
from time import sleep

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

        def new_book_panel():
            a = tk.Label(text='imie:', background='#D3D3D3')
            a.place(x=240, y=60)
            a = tk.Entry()
            a.place(x=300, y=60)

            b = tk.Label(text='nazwisko:', background='#D3D3D3')
            b.place(x=240, y=80)
            b = tk.Entry()
            b.place(x=300, y=80)

            c = tk.Label(text='pesel:', background='#D3D3D3')
            c.place(x=240, y=100)
            c = tk.Entry()
            c.place(x=300, y=100)

            d = tk.Label(text='data przyj:', background='#D3D3D3')
            d.place(x=240, y=120)
            d = tk.Entry()
            d.place(x=300, y=120)

            e = tk.Label(text='data wyj:', background='#D3D3D3')
            e.place(x=240, y=140)
            e = tk.Entry()
            e.place(x=300, y=140)

            f = tk.Label(text='nr pokoju:', background='#D3D3D3')
            f.place(x=240, y=160)
            f = tk.Entry()
            f.place(x=300, y=160)

            g = tk.Label(text='opłacona:', background='#D3D3D3')
            g.place(x=240, y=180)
            var1 = tk.IntVar()
            g = tk.Checkbutton(variable=var1, onvalue=1, offvalue=0)
            g.place(x=300, y=180)

            def save_data():
                if DataBase().is_customers_in_db(c.get()):
                    DataBase().insert_new_accommodation(d.get(), e.get(), DataBase().get_id_by_pesel(c.get()),
                                                        f.get(), str(var1.get()))
                else:
                    DataBase().insert_new_customer(a.get(), b.get(), c.get())
                    save_data()
                    messagebox.showinfo(message='pierwsza rezerwacja tego klienta')

            save_button = tk.Button(text='         zapisz         ', command=save_data)
            save_button.place(x=325, y=180)

        self.new_booking = tk.Button(text='   nowa rezerwacja   ', font=self.my_font, command=new_book_panel)
        self.new_booking.grid(row=1, column=0)

        self.free_rooms = tk.Button(text='      wolne pokoje      ', font=self.my_font, command=booking_window)
        self.free_rooms.grid(row=3, column=0)

        self.free_rooms = tk.Button(text='wyszukaj rezerwacje', font=self.my_font, command=booking_window)
        self.free_rooms.grid(row=5, column=0)

        def refresh_panel():
            upcoming_bookings()

        refresh_button = tk.Button(text='↻', command=refresh_panel)
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

            paid = tk.Label(text='oplacona.')
            paid.grid(row=1, column=12)

            r = DataBase().get_closest_arrivals()
            for i in range(len(r)):
                z = 0
                for j in range(len(r[i])):
                    z += 2
                    if r[i][j] == 'true':
                        tk.Label(text='TAK').grid(column=z, row=2+i)
                    elif r[i][j] == 'false':
                        tk.Label(text='NIE').grid(column=z, row=2 + i)
                    else:
                        tk.Label(text=r[i][j]).grid(column=z, row=2 + i)

        back()
        upcoming_bookings()
        self.root.mainloop()


if __name__ == '__main__':
    Window('hotel', '1000x600', is_resize=False)
