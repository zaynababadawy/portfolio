# AO3 Archive Warnings Analysis (2021 Snapshot)

## Overview

This project analyzes the usage of archive warnings in fanfiction works on Archive of Our Own (AO3) using a 2021 snapshot of ~600,000 works. Archive warnings are tags that signal sensitive content, allowing readers to make informed choices.

**Objective:** Identify the most and least frequently used warnings and visualize their prevalence to support moderation, improve tagging, and inform readers.

---

## Data Sources

**1. works.csv**  
- Metadata on fanfiction works  
- Columns: work_id, creation date, language, restricted flag, complete flag, word count, associated tag IDs  

**2. tags.csv**  
- Metadata on tags  
- Columns: tag_id, tag type (e.g., ArchiveWarning, Fandom), tag name, canonical flag, usage count, merger ID  

**3. work_tag.csv**  
- Joined data combining works and tags for analysis

---

## Methodology

**Tools Used:** Python, Pandas, Matplotlib, Seaborn  

**Steps:**
1. Load CSV files into Pandas DataFrames.
2. Filter tags to only include `ArchiveWarning` types.
3. Merge with `work_tag.csv` to associate warnings with works.
4. Count works per warning and calculate percentages of total works.
5. Visualize distributions using bar plots and summary charts.

---

## Key Findings

- Total works analyzed: 601,286  
- Works with at least one archive warning: 61,576 (~10.2%)  

**Most frequent archive warnings:**

| Warning Name | Total Works | % of All Works |
|-------------|-------------|----------------|
| No Archive Warnings Apply | 32,051 | 5.33% |
| Choose Not To Use Archive Warnings | 21,591 | 3.59% |
| Graphic Depictions of Violence | 5,281 | 0.88% |
| Major Character Death | 3,009 | 0.50% |
| Rape/Non-Con | 1,650 | 0.27% |
| Underage | 1,XXX | X% |

**Observations:**
- Most works either do not use explicit warnings or authors choose not to specify them.
- Sensitive content like violence and major character death is more frequently tagged than other categories.
- Multiple warnings can appear in a single work, indicating overlapping sensitive content.

---

## Visualizations

All figures are saved in the [`visuals`](visuals) folder. Example plots include:

- Bar charts of archive warning frequency  
- Distribution of works with multiple warnings  

![Example Bar Chart](visuals/bar_chart_example.png)

---

## Recommendations

1. Encourage authors to apply accurate archive warnings.  
2. Educate authors on the importance of content warnings for reader safety.  
3. Focus moderation and reader guidance on works with higher-risk warnings.  
4. Repeat analysis with updated datasets to track changes in tagging trends.  

---

## Appendix: Python Code Snippets

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSVs
works = pd.read_csv('data/works.csv', header=None)
tags = pd.read_csv('data/tags.csv', header=None)
work_tag = pd.read_csv('data/work_tag.csv', header=None)

# Rename columns appropriately
works.columns = ['work_id','date','language','restricted','complete','word_count','tag_ids']
tags.columns = ['tag_id','tag_type','tag_name','canonical','usage_count','merger_id']
work_tag.columns = ['work_id','tag_id']

# Filter ArchiveWarnings
archive_warning_names = [
    'Major Character Death',
    'Graphic Depictions of Violence',
    'Rape/Non-Con',
    'Underage',
    'No Archive Warnings Apply',
    'Choose Not To Use Archive Warnings'
]
archive_warnings = tags[tags['tag_name'].isin(archive_warning_names)][['tag_id','tag_name']]

# Join work_tag with archive warnings
work_warnings = work_tag[work_tag['tag_id'].isin(archive_warnings['tag_id'])]

# Count total works per warning
warning_summary = work_warnings.merge(archive_warnings, on='tag_id') \
                               .groupby('tag_name')['work_id'] \
                               .nunique().reset_index() \
                               .rename(columns={'work_id':'total_works'})
