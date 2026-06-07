import sqlite3
import os

from src.product import Product
from src.user import User


class DatabaseManager:

    def __init__(self):

        os.makedirs("database", exist_ok=True)

        self.db_path = "database/ecommerce.db"

        self.connection = sqlite3.connect(
            self.db_path,
            check_same_thread=False
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    def create_tables(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            category TEXT,
            price REAL,
            rating REAL
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY,
            name TEXT
        )
        """)

        self.connection.commit()

    def get_next_product_id(self):

        self.cursor.execute(
            "SELECT MAX(product_id) FROM products"
        )

        result = self.cursor.fetchone()[0]

        return 101 if result is None else result + 1

    def get_next_user_id(self):

        self.cursor.execute(
            "SELECT MAX(user_id) FROM users"
        )

        result = self.cursor.fetchone()[0]

        return 1 if result is None else result + 1

    def insert_product(
        self,
        product_id,
        name,
        category,
        price,
        rating
    ):

        self.cursor.execute("""
        INSERT OR REPLACE INTO products
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            product_id,
            name,
            category,
            price,
            rating
        ))

        self.connection.commit()

    def insert_user(
        self,
        user_id,
        name
    ):

        self.cursor.execute("""
        INSERT OR REPLACE INTO users
        VALUES (?, ?)
        """,
        (
            user_id,
            name
        ))

        self.connection.commit()

    def load_products(self):

        self.cursor.execute(
            "SELECT * FROM products"
        )

        rows = self.cursor.fetchall()

        products = {}

        for row in rows:

            products[row[0]] = Product(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )

        return products

    def load_users(self):

        self.cursor.execute(
            "SELECT * FROM users"
        )

        rows = self.cursor.fetchall()

        users = {}

        for row in rows:

            users[row[0]] = User(
                row[0],
                row[1]
            )

        return users

    def close(self):

        self.connection.close()