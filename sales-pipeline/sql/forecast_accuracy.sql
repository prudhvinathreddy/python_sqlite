-- Forecasted vs actual performance
SELECT 
    DealID,
    DealName,
    DealValue,
    CloseProbability,
    (DealValue * CloseProbability) AS ForecastedValue,
    Outcome
FROM 
    SalesPipeline
WHERE 
    Outcome IN ('Won', 'Lost');
