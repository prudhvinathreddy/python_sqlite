import sqlite3

# Connect to the database
conn = sqlite3.connect("SalesPipeline.db")

# SQL queries
queries = {
    "Pipeline Overview": """
        SELECT 
            COUNT(*) AS TotalDeals,
            SUM(DealValue) AS TotalPipelineValue,
            AVG(CloseProbability) AS AvgCloseProbability
        FROM SalesPipeline;
    """,
    "Stage-Wise Analysis": """
        SELECT 
            DealStage,
            COUNT(*) AS DealsCount,
            SUM(DealValue) AS TotalStageValue,
            AVG(CloseProbability) AS AvgStageProbability
        FROM SalesPipeline
        GROUP BY DealStage
        ORDER BY TotalStageValue DESC;
    """,
    "Forecast Accuracy": """
        SELECT 
            DealID,
            DealName,
            DealValue,
            CloseProbability,
            (DealValue * CloseProbability) AS ForecastedValue,
            Outcome
        FROM SalesPipeline
        WHERE Outcome IN ('Won', 'Lost');
    """
}

# Execute and display results
for title, query in queries.items():
    print(f"\n--- {title} ---")
    result = conn.execute(query).fetchall()
    for row in result:
        print(row)

# Close the connection
conn.close()
