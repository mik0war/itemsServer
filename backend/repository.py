import psycopg2

from app_types import Item, Characteristic


def get_connection():
    connection = psycopg2.connect(host='localhost',
                                  port=5432,
                                  database='item_db',
                                  user='postgres',
                                  password='123')

    return connection


def get_items():
    con = get_connection()
    cursor = con.cursor()

    cursor.execute('SELECT id, name, count FROM item')

    items = cursor.fetchall()

    items = [Item(*i).__dict__ for i in items]

    return items

def get_characteristic(id):
    con = get_connection()
    cursor = con.cursor()

    cursor.execute('SELECT category, value FROM characteristic WHERE item_id = %s', [id])

    items = cursor.fetchall()

    items = [Characteristic(*i).__dict__ for i in items]

    return items