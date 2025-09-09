SET @current_year = 2025;


SELECT Name, Continent, Region, Population, GNP, LifeExpectancy, IndepYear, 
	@current_year - IndepYear AS years_since_Indep,
    CASE
		WHEN @current_year - IndepYear <= 50 THEN 'Newly Independent'
        WHEN @current_year - IndepYear BETWEEN 50 AND 100 THEN 'Middle-aged Independence'
        ELSE 'Older Independent'
	END AS indep_category
FROM country
WHERE IndepYear IS NOT NULL
	AND name NOT IN ('United Kingdom', 'United States', 'France', 'Spain', 'Portugal', 'Germany', 'Denmark', 'Sweden', 
						'Netherlands', 'Italy', 'Belgium', 'Japan', 'Israel');

SELECT indep_category,
	COUNT(*) AS num_per_category,
	AVG(LifeExpectancy) AS avg_lifeexp,
    MIN(LifeExpectancy) AS min_lifeexp,
    MAX(LifeExpectancy) AS max_lifeexp,
    AVG(gnp) AS avg_gnp,
    MIN(gnp) AS min_gnp,
    MAX(gnp) AS max_gnp
FROM (
	SELECT name,
		@current_year - IndepYear AS years_since_Indep,
    CASE
		WHEN @current_year - IndepYear <= 50 THEN 'Newly Independent'
        WHEN @current_year - IndepYear BETWEEN 50 AND 100 THEN 'Middle-aged Independence'
        ELSE 'Older Independent'
	END AS indep_category,
		LifeExpectancy,
		gnp
	FROM country
	WHERE IndepYear IS NOT NULL
		AND name NOT IN ('United Kingdom','United States','France','Spain',
                       'Portugal','Germany','Denmark','Sweden',
                       'Netherlands','Italy','Belgium','Japan','Israel')
) as t 	
GROUP BY indep_category;



