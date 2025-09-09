-- Set the reference year
SET @current_year = 2025;

-- Step 0: Create a categorized temp table
DROP TEMPORARY TABLE IF EXISTS categorized;

CREATE TEMPORARY TABLE categorized AS
SELECT name,
       continent,
       region,
       population,
       gnp,
       lifeexpectancy,
       IndepYear,
       @current_year - IndepYear AS years_since_indep,
       CASE
           WHEN @current_year - IndepYear <= 50 THEN 'Newly Independent'
           WHEN @current_year - IndepYear BETWEEN 50 AND 100 THEN 'Middle-aged Independent'
           ELSE 'Older Independent'
       END AS indep_category
FROM country
WHERE IndepYear IS NOT NULL
  AND name NOT IN ('United Kingdom','United States','France','Spain',
                   'Portugal','Germany','Denmark','Sweden',
                   'Netherlands','Italy','Belgium','Japan','Israel');

-- ✅ Step 1: Summary stats for life expectancy and GDP
SELECT indep_category,
       COUNT(*) AS num_countries,
       AVG(lifeexpectancy) AS avg_lifeexp,
       MIN(lifeexpectancy) AS min_lifeexp,
       MAX(lifeexpectancy) AS max_lifeexp,
       AVG(gnp) AS avg_gnp,
       MIN(gnp) AS min_gnp,
       MAX(gnp) AS max_gnp,
       AVG(gnp / NULLIF(population,0)) AS avg_gnp_per_capita
FROM categorized
GROUP BY indep_category
ORDER BY FIELD(indep_category, 'Newly Independent', 'Middle-aged Independent', 'Older Independent');

-- ✅ Step 2a: Continent frequency
SELECT indep_category,
       continent,
       COUNT(*) AS num_countries
FROM categorized
GROUP BY indep_category, continent
ORDER BY indep_category, num_countries DESC;

-- ✅ Step 2b: Region frequency
SELECT indep_category,
       region,
       COUNT(*) AS num_countries
FROM categorized
GROUP BY indep_category, region
ORDER BY indep_category, num_countries DESC;

-- ✅ Step 2c: Top continent per category
WITH ranked AS (
    SELECT indep_category,
           continent,
           COUNT(*) AS num_countries,
           ROW_NUMBER() OVER (PARTITION BY indep_category ORDER BY COUNT(*) DESC) AS rn
    FROM categorized
    GROUP BY indep_category, continent
)
SELECT indep_category, continent, num_countries
FROM ranked
WHERE rn = 1;
