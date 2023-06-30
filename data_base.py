import psycopg2 as pg
import psycopg2.extras


class DataBase:
    def __init__(self):
        fine = True
        try:
            self.connection = pg.connect(
                host='localhost',
                database='hotel',
                user='postgres',
                password='123')
            self.cur = self.connection.cursor()

        except pg.OperationalError:
            print('connection error')
            fine = False

        finally:
            if fine:
                print('start\n\n')

    def insert_new_customer(self, first_name, last_name):
        postgres_query = (' INSERT INTO customers(first_name, last_name)'
                          ' VALUES (%s,%s)')
        record_to_insert = (first_name, last_name)
        self.cur.execute(postgres_query, record_to_insert)
        self.connection.commit()

    def fetch_all_customers(self):
        self.cur.execute('SELECT * FROM customers')
        self.connection.commit()
        result = self.cur.fetchall()
        print('id', ' imie', '  nazwisko')
        for row in result:
            print(str(row)[1:-1])

    def delete_customer(self, customer_id: int):
        postgres_query = 'DELETE FROM customers WHERE id = (%s)'
        record_to_delete = (customer_id,)
        self.cur.execute(postgres_query, record_to_delete)
        self.connection.commit()

    def insert_new_accommodation(self, arrival_date, departure_date, customer_id, room_number):
        postgres_query = (' INSERT INTO accommodations(arrival_date, departure_date,customer_id, room_number)'
                          ' VALUES (%s,%s,%s,%s)')
        record_to_insert = (arrival_date, departure_date, customer_id, room_number)
        self.cur.execute(postgres_query, record_to_insert)
        self.connection.commit()

    def get_free_rooms(self, start, end):
        self.cur.execute('SELECT room_number FROM rooms')
        self.connection.commit()
        rooms = self.cur.fetchall()
        postgres_query = ('SELECT room_number, count(*) FROM accommodations'
                          ' WHERE arrival_date BETWEEN (%s) AND (%s)'
                          ' OR departure_date BETWEEN (%s) AND (%s)'
                          ' GROUP BY room_number'
                          )
        dates = (start, end, start, end)
        self.cur.execute(postgres_query, dates)
        a = self.cur.fetchall()[0]
        self.connection.commit()
        for room in rooms:
            free = True
            room = room[0]
            for i in a:
                if a[0] == int(room) and a[1] == 1:
                    free = False
                    break
            if free:
                print(room)


