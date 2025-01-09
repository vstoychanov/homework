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
    all_products = [
        ('Product1', 'Description1', '100'),
        ('Product2', 'Description2', '200'),
        ('Product3', 'Description3', '300'),
        ('Product4', 'Description4', '400')
    ]
    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?,?,?)', all_products)
    connection.commit()
    connection.close()

initiate_db()

def get_all_products(db_path='Products.db'):
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    connection.close()
    return products