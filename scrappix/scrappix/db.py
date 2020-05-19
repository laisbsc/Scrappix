import sqlite3

"""
create a connection to the database
this should be place inside a try/catch statement
"""
try:
    conn = sqlite3.connect('amazon_data.db')
except:
    raise ValueError

# cursor implementation
cursor = conn.cursor()

# add a table to the database
cursor.execute("""CREATE TABLE amazon_search(
                    ITEM_NAME text,
                    PRICE int,
                    STOCK int,
                    IMAGE blob)""")
conn.commit()
conn.close()
