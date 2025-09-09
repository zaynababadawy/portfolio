# 🌍 Post-Colonial Independence and Socio-Economic Patterns

## 📌 Project Overview
As a **junior data analyst**, I explored how the **age of independence** of countries relates to key socio-economic indicators, focusing on **life expectancy** and **Gross National Product (GNP)**.  

The central question:  
👉 *Do countries that gained independence more recently differ socio-economically from those with older independence histories?*

To answer this, I:  
- Categorized countries into **Newly Independent** (≤50 years), **Middle-aged Independent** (51–100 years), and **Older Independent** (>100 years).  
- Excluded historically dominant global powers (e.g., UK, US, France, Spain, Portugal, Germany, Japan, etc.) to focus on post-colonial nations.  
- Used **SQL** to clean, transform, and summarize the dataset.  
- Used **Python (Pandas, Matplotlib, Seaborn)** to create insightful visualizations.  

---

## 📂 Data
The project is based on the classic **World Database (country table)**, with additional CSV outputs from SQL queries:

- `indep_summary.csv` → Summary of socio-economic indicators per independence category.  
- `step2_combined.csv` → Continent and region-level breakdown of independence categories.  

---

## 🛠️ Methodology

### 🔹 SQL Analysis
1. **Categorization by independence year**  
   ```sql
   CASE
       WHEN @current_year - IndepYear <= 50 THEN 'Newly Independent'
       WHEN @current_year - IndepYear BETWEEN 51 AND 100 THEN 'Middle-aged Independent'
       ELSE 'Older Independent'
   END AS indep_category
   ```

2. **Summary statistics**  
   - Average, min, and max values of **Life Expectancy** and **GNP**  
   - GNP per capita (normalized by population)

3. **Geographical patterns**  
   - Distribution by **continent** and **region**  
   - Most common continent per independence category

---

### 🔹 Python Visualizations
I used **Pandas** to load the CSV outputs from SQL, and **Seaborn/Matplotlib** to visualize patterns.

- 📊 **Average GDP by Independence Category**  
- 📊 **Average Life Expectancy by Independence Category**  
- 📊 **Number of Countries per Continent by Category**  
- 📊 **Number of Countries per Region by Category**  

All charts are saved in the [`visuals/`](visuals) folder.  

---

## 📈 Key Insights
- **Life Expectancy**: Older independent countries tend to show higher average life expectancy compared to newly independent ones.  
- **GNP**: Significant disparities exist, with older independent nations generally having stronger economies.  
- **Geography**: Africa and Asia dominate the “Newly Independent” category, reflecting the wave of decolonization in the mid-20th century.  

---

## 📁 Project Structure
```
02-post-colonial-independence-world-analysis/
│
├── data/
│   ├── indep_summary.csv
│   ├── step2_combined.csv
│   ├── world.sql
│
├── scripts/
│   ├── indep_categories.sql
│   ├── summaries.sql
│   ├── world_postcolonial_analysis.py
|
├── visuals/
│   ├── avg_gdp_by_category.png
│   ├── avg_lifeexp_by_category.png
│   ├── countries_per_continent_by_category.png
│   ├── countries_per_region_by_category.png
│
└── README.md
```

---

## 🚀 Tools & Skills Demonstrated
- **SQL**: Data categorization, summary statistics, temporary tables, CTEs  
- **Python (Pandas, Seaborn, Matplotlib)**: Data wrangling and visualization  
- **Data Storytelling**: Linking independence history with socio-economic outcomes  

---

## 🔮 Next Steps
- Explore **education levels** and **healthcare access** as additional indicators.  
- Conduct **time-series analysis** for countries with available historical data.  
- Apply **clustering techniques** to group countries by multi-dimensional socio-economic similarities.  

---

✍️ *Authored by Zaynab (Junior Data Analyst)*  
