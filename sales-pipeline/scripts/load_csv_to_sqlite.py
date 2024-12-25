import sqlite3
import pandas as pd

# Load CSV data
csv_path = "../data/SalesPipelineData.csv"
df = pd.read_csv(csv_path)

# Connect to SQLite database
conn = sqlite3.connect("../SalesPipeline.db")
df.to_sql("SalesPipeline", conn, if_exists="replace", index=False)

print("Data uploaded successfully!")

conn.close()
