import sqlite3
from faker import Faker


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'/Users/mariiashemetova/Documents/Python/mariiashemetovaua' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()
        self.fake = Faker()

    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}' "
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self,product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_table_schema(self, table_name):
        query = f"PRAGMA table_info({table_name})"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def add_new_customer(self, id, name, address, city, country):
        query = f"INSERT OR REPLACE INTO customers (id, name, address, city, country) \
            VALUES ({id}, '{name}', '{address}', '{city}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()

    def add_random_customer(self):
        name = self.fake.name()
        address = self.fake.address().replace('\n', ', ')
        city = self.fake.city()
        postal_code = self.fake.postcode()
        country = self.fake.country()
        query = f"INSERT INTO customers (name, address, city, postalCode, country) \
            VALUES ('{name}', '{address}', '{city}', '{postal_code}', '{country}')"
        self.cursor.execute(query)
        self.connection.commit()


    def add_only_name_to_customers (self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        try:
            query = f"INSERT OR REPLACE INTO customers (name) VALUES('{name}')"
            self.cursor.execute(query)
            self.connection.commit()
        except sqlite3.Error as e:
            print(f"Error occurred: {e}")
            return False
        return True
    
    def get_customers_with_empty_field(self):
        query = "SELECT * FROM customers WHERE name IS NULL OR address IS NULL OR \
            city IS NULL OR postalCode IS NULL OR country IS NULL"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record