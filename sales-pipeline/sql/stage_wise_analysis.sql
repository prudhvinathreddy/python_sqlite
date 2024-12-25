-- Analysis of deals by stage
SELECT 
    DealStage,
    COUNT(*) AS DealsCount,
    SUM(DealValue) AS TotalStageValue,
    AVG(CloseProbability) AS AvgStageProbability
FROM 
    SalesPipeline
GROUP BY 
    DealStage
ORDER BY 
    TotalStageValue DESC;
