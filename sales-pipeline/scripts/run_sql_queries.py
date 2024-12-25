import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("../SalesPipeline.db")

# List of SQL scripts
sql_scripts = {
    "Pipeline Overview": "../sql/pipeline_overview.sql",
    "Stage-Wise Analysis": "../sql/stage_wise_analysis.sql",
    "Forecast Accuracy": "../sql/forecast_accuracy.sql",
}

for name, path in sql_scripts.items():
    with open(path, 'r') as file:
        query = file.read()
        print(f"\n--- {name} ---")
        result = conn.execute(query).fetchall()
        for row in result:
            print(row)

conn.close()
