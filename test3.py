import sqlite3
import pandas as pd

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("SalesPipeline.db")
cursor = conn.cursor()

cursor.execute( '''create table users ( id integer, name text, phone int)''')

data = [(1,'rag',2345),(2,'dfg',2312),(3,'awsd',5675)]
cursor.executemany('''insert into users (id,name,phone) values(?,?,?)''',data)

# Verify data insertion
query = "SELECT * FROM users;"
result = pd.read_sql(query, conn)
print(result)

# Close the connection
conn.close()
