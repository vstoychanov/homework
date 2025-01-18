import sqlite3


def initiate_db(db_path='Products.db'):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL UNIQUE,
            email TEXT NOY NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')

    cursor.execute('DELETE FROM Products')
    all_products = [
        ('Product1', 'Description1', '100'),
        ('Product2', 'Description2', '200'),
        ('Product3', 'Description3', '300'),
        ('Product4', 'Description4', '400')
    ]
    for product in all_products:
        cursor.execute('INSERT OR IGNORE INTO Products (title, description, price) VALUES (?, ?, ?)', product)
    connection.commit()
    connection.close()


def add_user(username, email, age, db_path='Products.db'):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, 1000)', (username, email, age))
    connection.commit()
    connection.close()

def is_included(username, db_path='Products.db'):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT 1 FROM Users WHERE username = ?', (username,))
    result = cursor.fetchone()
    connection.close()
    return result is not None

def get_all_products(db_path='Products.db'):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products

initiate_db()