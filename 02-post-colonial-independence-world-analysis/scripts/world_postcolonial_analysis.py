import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ---------------------------
# Step 0: Set visuals folder
# ---------------------------
visuals_folder = r"C:\Users\zayna\OneDrive\Documents\GitHub\portfolio\02-post-colonial-independence-world-analysis\visuals"
os.makedirs(visuals_folder, exist_ok=True)

# ---------------------------
# Step 1: Load CSVs
# ---------------------------

df_two = pd.read_csv(
    r"C:\Users\zayna\OneDrive\Documents\GitHub\portfolio\02-post-colonial-independence-world-analysis\data\indep_summary.csv",
    header=None,
    names=['indep_category', 'num_countries', 'avg_lifeexp', 'min_lifeexp',
           'max_lifeexp', 'avg_gnp', 'min_gnp', 'max_gnp', 'avg_gnp_per_capita']
)

df_one = pd.read_csv(
    r"C:\Users\zayna\OneDrive\Documents\GitHub\portfolio\02-post-colonial-independence-world-analysis\data\step2_combined.csv",
    header=None,
    names=['indep_category', 'continent', 'region', 'num_per_category', 'num_countries_in_continent', 'top_continent_flag']
)

# ---------------------------
# Step 2: Clean column names
# ---------------------------
df_two.columns = df_two.columns.str.strip().str.lower()
df_one.columns = df_one.columns.str.strip().str.lower()

# ---------------------------
# Step 3: Category-level bar charts
# ---------------------------

# Average GDP per category
plt.figure(figsize=(8,5))
sns.barplot(data=df_two, x='indep_category', y='avg_gnp', color='steelblue')
plt.title("Average GDP by Independence Category")
plt.xlabel("Independence Category")
plt.ylabel("Average GDP")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "avg_gdp_by_category.png"))
plt.close()

# Average Life Expectancy per category
plt.figure(figsize=(8,5))
sns.barplot(data=df_two, x='indep_category', y='avg_lifeexp', color='seagreen')
plt.title("Average Life Expectancy by Independence Category")
plt.xlabel("Independence Category")
plt.ylabel("Average Life Expectancy")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "avg_lifeexp_by_category.png"))
plt.close()

# Number of countries per continent per category
continent_counts = df_one.groupby(['indep_category', 'continent'])['num_per_category'].sum().reset_index()
plt.figure(figsize=(10,6))
sns.barplot(data=continent_counts, x='indep_category', y='num_per_category', hue='continent')
plt.title("Number of Countries per Continent by Independence Category")
plt.xlabel("Independence Category")
plt.ylabel("Number of Countries")
plt.legend(title="Continent")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "countries_per_continent_by_category.png"))
plt.close()

# Number of countries per region per category
region_counts = df_one.groupby(['indep_category', 'region'])['num_per_category'].sum().reset_index()
plt.figure(figsize=(12,6))
sns.barplot(data=region_counts, x='indep_category', y='num_per_category', hue='region')
plt.title("Number of Countries per Region by Independence Category")
plt.xlabel("Independence Category")
plt.ylabel("Number of Countries")
plt.legend(title="Region", bbox_to_anchor=(1.05,1), loc='upper left')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig(os.path.join(visuals_folder, "countries_per_region_by_category.png"))
plt.close()
