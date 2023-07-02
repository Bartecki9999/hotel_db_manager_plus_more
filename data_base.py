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

    def insert_new_customer(self, first_name, last_name, pesel):
        postgres_query = (' INSERT INTO customers(first_name, last_name, pesel)'
                          ' VALUES (%s,%s,%s)')
        record_to_insert = (first_name, last_name, pesel)
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

    def insert_new_accommodation(self, arrival_date, departure_date, customer_id, room_number, paid):
        postgres_query = (' INSERT INTO accommodations(arrival_date, departure_date,customer_id, room_number, paid)'
                          ' VALUES (%s,%s,%s,%s,%s)')
        record_to_insert = (arrival_date, departure_date, customer_id, room_number, paid)
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

    def get_name_by_id(self, id: int):
        self.cur.execute('SELECT first_name, last_name FROM customers WHERE id = (%s)', str(id))
        self.connection.commit()
        result = self.cur.fetchall()
        print(result)

    def get_closest_arrivals(self):
        self.cur.execute('SELECT cast(arrival_date as text), cast(departure_date as text),'
                         ' first_name, last_name, room_number, cast(paid as text)'
                         ' FROM accommodations INNER JOIN customers on customers.id = accommodations.customer_id'
                         ' WHERE arrival_date - CURRENT_DATE >= 0'
                         ' ORDER BY arrival_date - CURRENT_DATE'
                         ' LIMIT 16')
        self.connection.commit()
        result = self.cur.fetchall()
        return result

    def is_customers_in_db(self, pesel: str):
        postgres_query = 'SELECT COUNT(*) FROM customers WHERE pesel = (%s)'
        data = (pesel, )
        self.cur.execute(postgres_query, data)
        self.connection.commit()
        result = self.cur.fetchall()
        return int(result[0][0])

    def get_id_by_pesel(self, pesel):
        postgres_query = 'SELECT id FROM customers WHERE pesel = (%s)'
        data = (pesel,)
        self.cur.execute(postgres_query, data)
        self.connection.commit()
        result = self.cur.fetchall()
        return result[0]


#DataBase().insert_new_accommodation('2023-10-27', '2023-10-28', )

