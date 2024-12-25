import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("../SalesPipeline.db")

# Query and export results
query = "SELECT * FROM SalesPipeline"
df = pd.read_sql(query, conn)
df.to_csv("../data/SalesPipelineExport.csv", index=False)

print("Exported results to CSV!")

conn.close()
