import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Step 1: Load CSVs
# ---------------------------
works = pd.read_csv(r"C:\Users\zayna\OneDrive\Documents\GitHub\portfolio\01-ao3-archive-warnings-analysis\data\works.csv", header=None)
work_tag = pd.read_csv(r"C:\Users\zayna\OneDrive\Documents\GitHub\portfolio\01-ao3-archive-warnings-analysis\data\work_tag.csv", header=None)
tags = pd.read_csv(r"C:\Users\zayna\OneDrive\Documents\GitHub\portfolio\01-ao3-archive-warnings-analysis\data\tags.csv", header=None)

# ---------------------------
# Step 2: Name columns
# ---------------------------
works.columns = ['work_id', 'creation_date', 'language', 'restricted', 'complete', 'word_count', 'tag_ids']
work_tag.columns = ['work_id', 'tag_id']
tags.columns = ['tag_id', 'type', 'name', 'canonical', 'approx_count', 'merger_id']

# ---------------------------
# Step 3: Filter only ArchiveWarnings
# ---------------------------
archive_warning_names = [
    'Major Character Death',
    'Graphic Depictions Of Violence',
    'Rape/Non-Con',
    'Underage',
    'No Archive Warnings Apply',
    'Choose Not To Use Archive Warnings'
]

archive_warnings = tags[
    (tags['type'] == 'ArchiveWarning') &
    (tags['name'].isin(archive_warning_names))
][['tag_id', 'name']]

# ---------------------------
# Step 4: Merge work_tag with archive warnings
# ---------------------------
work_warnings = work_tag.merge(archive_warnings, on='tag_id', how='inner')

# ---------------------------
# Step 5: Summary statistics
# ---------------------------
total_works = works['work_id'].nunique()
works_with_warnings = work_warnings['work_id'].nunique()

print(f"Total works: {total_works}")
print(f"Works with at least one archive warning: {works_with_warnings}")
print(f"Percentage: {works_with_warnings/total_works:.2%}")

# Count per warning
warning_summary = work_warnings.groupby('name').agg(total_works=('work_id', 'nunique')).reset_index()
warning_summary['percent_of_all_works'] = warning_summary['total_works'] / total_works * 100
warning_summary = warning_summary.sort_values('total_works', ascending=False)

print(warning_summary)

# ---------------------------
# Step 6: Visualization
# ---------------------------
plt.figure(figsize=(10,6))
plt.bar(warning_summary['name'], warning_summary['total_works'], color='skyblue')
plt.title("Number of Works per Archive Warning")
plt.xlabel("Archive Warning")
plt.ylabel("Number of Works")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig(r"C:\Users\zayna\OneDrive\Documents\GitHub\portfolio\01-ao3-archive-warnings-analysis\visuals\num_of_works.png")
plt.show()

plt.figure(figsize=(10,6))
plt.bar(warning_summary['name'], warning_summary['percent_of_all_works'], color='salmon')
plt.title("Percentage of Works per Archive Warning")
plt.xlabel("Archive Warning")
plt.ylabel("Percentage of All Works")
plt.xticks(rotation=30, ha='right')
plt.tight_layout()
plt.savefig(r"C:\Users\zayna\OneDrive\Documents\GitHub\portfolio\01-ao3-archive-warnings-analysis\visuals\percent_of_all_works.png")
plt.show()
