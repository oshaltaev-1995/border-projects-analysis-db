SELECT 
    СС.Название AS Сфера_сотрудничества,
    COUNT(*) AS Количество_упоминаний
FROM 
    Проект_Сфера ПС
JOIN 
    Сфера_сотрудничества СС ON ПС.Сфера_id = СС.ID
GROUP BY 
    СС.Название
ORDER BY 
    Количество_упоминаний DESC;
