import sqlite3
import pandas as pd

# Load the CSV file into a DataFrame
csv_file = "SalesPipelineData.csv"  # Update the path if needed
df = pd.read_csv(csv_file)

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect("SalesPipeline.db")

# Create a table and insert data into the database
df.to_sql("SalesPipeline", conn, if_exists="replace", index=False)

# Verify data insertion
query = "SELECT * FROM SalesPipeline LIMIT 5;"
result = pd.read_sql(query, conn)
print(result)

# Close the connection
conn.close()
