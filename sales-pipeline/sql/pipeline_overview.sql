SELECT 
COUNT(*) AS TotalDeals,
SUM(DealValue) AS TotalPipelineValue,
AVG(CloseProbability) AS AvgCloseProbability
FROM
SalesPipeline;