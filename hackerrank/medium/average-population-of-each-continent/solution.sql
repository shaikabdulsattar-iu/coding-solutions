SELECT 
    COUNTRY.Continent,
    CASE 
        WHEN AVG(CITY.Population) >= 0 
        THEN TRUNCATE(AVG(CITY.Population), 0)
    END
FROM CITY
JOIN COUNTRY ON CITY.CountryCode = COUNTRY.Code
GROUP BY COUNTRY.Continent;
