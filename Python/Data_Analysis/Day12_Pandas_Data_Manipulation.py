# ==========================================================
# GRRAS Solutions - DSML with AI
# Author : Sujaan Bhalla
# Day 12 - Pandas Data Manipulation
# ==========================================================

import pandas as pd
import numpy as np

# ==========================================================
# Read JSON File
# ==========================================================

df = pd.read_json("student-data.json")

print("Original Data")
print(df)

# ==========================================================
# 1. Sorting Data
# ==========================================================

print("\nSort by English (Ascending)")
print(df.sort_values(by="english"))

print("\nSort by English (Descending)")
print(df.sort_values(by="english", ascending=False))

print("\nSort by Maths")
print(df.sort_values(by="maths"))

print("\nSort by Physics")
print(df.sort_values(by="physics"))

print("\nSort by Multiple Columns")
print(df.sort_values(
    by=["english", "maths"],
    ascending=[False, True]
))

# ==========================================================
# 2. Add New Column
# ==========================================================

df["total"] = (
    df["physics"] +
    df["maths"] +
    df["english"]
)

print("\nTotal Marks Added")
print(df)

# ==========================================================
# 3. Add New Row
# ==========================================================

print("\nAdd Single Row")

df.loc[14] = [
    "Emily",
    "Female",
    80,
    90,
    87,
    257
]

print(df)

# ==========================================================
# 4. Drop Column
# ==========================================================

print("\nDrop Total Column")

print(
    df.drop("total", axis=1)
)

# ==========================================================
# 5. Missing Values
# ==========================================================

print("\nCreate Missing Value")

df.loc[4, "marks"] = np.nan

print(df)

# Check Missing Values
print("\nNull Values")

print(df.isnull())

# Count Missing Values
print("\nNull Count")

print(df.isnull().sum())

# Check Any Missing Value
print("\nAny Null Value")

print(df.isnull().any())

# ==========================================================
# Fill Missing Values
# ==========================================================

df["marks"] = df["marks"].fillna(100)

print("\nFill Missing Marks with 100")

print(df)

# ==========================================================
# Mean Filling
# ==========================================================

df.loc[2, "marks"] = np.nan

df["marks"] = df["marks"].fillna(
    df["marks"].mean()
)

print("\nFill Missing Marks with Mean")

print(df)

# ==========================================================
# Date Handling
# ==========================================================

df.drop(
    [6,7,8,9,10,11,12,13,14],
    inplace=True
)

df["doj"] = [
    "2025-01-01",
    "2025-01-02",
    "2025-01-03",
    "2025-01-04",
    "2025-01-05",
    "2025-01-06"
]

print("\nBefore Conversion")
print(df["doj"].dtype)

df["doj"] = pd.to_datetime(df["doj"])

print("\nAfter Conversion")
print(df["doj"].dtype)

# ==========================================================
# Date Functions
# ==========================================================

print("\nYear")
print(df["doj"].dt.year)

print("\nMonth")
print(df["doj"].dt.month)

print("\nDay")
print(df["doj"].dt.day)

print("\nDay Name")
print(df["doj"].dt.day_name())

print("\nMonth Name")
print(df["doj"].dt.month_name())

# ==========================================================
# Date Arithmetic
# ==========================================================

print("\nAdd 20 Days")

print(
    df["doj"] +
    pd.to_timedelta(20, unit="D")
)

print(
    df["doj"] +
    pd.to_timedelta("20 days")
)

# ==========================================================
# Practice Questions
# ==========================================================

# Sort Physics Marks (Low → High)
# Sort Physics Marks (High → Low)
# Sort Maths Marks (Ascending)
# Sort English Marks (Descending)

# Add Total Marks Column
# Add Average Marks Column

# Update Arun's Physics Marks
# Update Rajesh's English Marks

# Add New Student
# Delete Student

# Delete Gender Column

# Find Missing Values
# Fill Missing Values
# Remove Rows Having Missing Values

# ==========================================================
# End of Program
# ==========================================================