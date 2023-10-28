import sqlite3
import datetime


# def get_timestamp(y, m, d):
#     return datetime.datetime.timestamp(datetime.datetime(y, m, d))


# def get_date(tmstmo):
#     return datetime.datetime.fromtimestamp(tmstmo).date()

# with sqlite3.connect("/Users/nikolay/Documents/efrsb_parcer/database.sqlite") as db:
#     cursor = db.cursor()
#     query = """CREATE TABLE IF NOT EXISTS payments(
#     id INTEGER,
#     anount REAL,
#     payment_date INTEGER,
#     expens_id INTEGER
#     )"""
#     cursor.execute(query)
#     db.commit()


with sqlite3.connect("orders.db") as db:
    cursor = db.cursor()
    cursor.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00001', 'Alex', 'Smith', 'male');""")
    db.commit()
