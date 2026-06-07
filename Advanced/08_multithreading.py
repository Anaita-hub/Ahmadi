# ============================================================
# Advanced Lesson 6: Data Analysis with Pandas
# Instructor: Anaita Ahmadi | GEO Organization
# ============================================================

# Install first: pip install pandas matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PART 1: Creating DataFrames
# ============================================================

# --- From a dictionary ---
data = {
    "Name":    ["Fatima", "Maryam", "Zahra", "Sara", "Layla", "Noor"],
    "Age":     [22, 24, 21, 23, 25, 20],
    "Grade":   [90, 85, 95, 88, 72, 91],
    "City":    ["Kabul", "Herat", "Mazar", "Kabul", "Kandahar", "Herat"],
    "Passed":  [True, True, True, True, False, True],
}

df = pd.DataFrame(data)
print("=== Full DataFrame ===")
print(df)

print("\n=== Basic Info ===")
print(df.info())
print("\n=== Statistics ===")
print(df.describe())

# ============================================================
# PART 2: Selecting & Filtering
# ============================================================

print("\n=== Select one column ===")
print(df["Name"])

print("\n=== Select multiple columns ===")
print(df[["Name", "Grade"]])

print("\n=== Filter: Grade >= 90 ===")
top = df[df["Grade"] >= 90]
print(top)

print("\n=== Filter: City is Kabul ===")
kabul = df[df["City"] == "Kabul"]
print(kabul)

print("\n=== Filter: Passed AND Grade > 85 ===")
filtered = df[(df["Passed"] == True) & (df["Grade"] > 85)]
print(filtered)

# ============================================================
# PART 3: Adding & Modifying Columns
# ============================================================

df["Grade_Letter"] = df["Grade"].apply(
    lambda g: "A" if g >= 90 else ("B" if g >= 80 else "C")
)
df["Age_Group"] = df["Age"].apply(lambda a: "Senior" if a >= 24 else "Junior")

print("\n=== With new columns ===")
print(df[["Name", "Grade", "Grade_Letter", "Age_Group"]])

# ============================================================
# PART 4: Grouping & Aggregation
# ============================================================

print("\n=== Average grade by city ===")
print(df.groupby("City")["Grade"].mean().round(1))

print("\n=== Count students per city ===")
print(df.groupby("City")["Name"].count())

print("\n=== Multiple aggregations ===")
print(df.groupby("City")["Grade"].agg(["mean", "min", "max"]).round(1))

# ============================================================
# PART 5: Sorting & Ranking
# ============================================================

print("\n=== Sorted by Grade (descending) ===")
print(df.sort_values("Grade", ascending=False)[["Name", "Grade", "City"]])

df["Rank"] = df["Grade"].rank(ascending=False).astype(int)
print("\n=== With rank ===")
print(df[["Name", "Grade", "Rank"]].sort_values("Rank"))

# ============================================================
# PART 6: Handling Missing Data
# ============================================================

import numpy as np
df_missing = df.copy()
df_missing.loc[1, "Grade"] = None
df_missing.loc[3, "City"] = None

print("\n=== Missing values ===")
print(df_missing.isnull().sum())

df_missing["Grade"].fillna(df_missing["Grade"].mean(), inplace=True)
df_missing["City"].fillna("Unknown", inplace=True)
print("\n=== After filling missing values ===")
print(df_missing[["Name", "Grade", "City"]])

# ============================================================
# PART 7: Simple Visualization
# ============================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart
df.sort_values("Grade", ascending=False).plot(
    kind="bar", x="Name", y="Grade", ax=axes[0],
    color="steelblue", edgecolor="black", legend=False
)
axes[0].set_title("Student Grades")
axes[0].set_xlabel("Student")
axes[0].set_ylabel("Grade")
axes[0].set_ylim(0, 105)
axes[0].axhline(y=90, color="red", linestyle="--", label="A threshold")
axes[0].legend()

# Pie chart
city_counts = df["City"].value_counts()
axes[1].pie(city_counts, labels=city_counts.index, autopct="%1.0f%%", startangle=90)
axes[1].set_title("Students by City")

plt.tight_layout()
plt.savefig("student_analysis.png", dpi=150)
plt.show()
print("\nChart saved as student_analysis.png")

# ============================================================
# Practice Exercise:
# 1. Load a CSV file of your own data and explore it
# 2. Find the top 3 students in each city
# 3. Calculate pass rate per city and visualize it
# ============================================================
