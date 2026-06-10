# ==========================================================
# GRRAS Solutions - DSML with AI
# Author : Sujaan Bhalla
# Day 08 : Pandas Introduction
# ==========================================================

# ==========================================================
# What is Pandas?
# ==========================================================

# Pandas is a Python library used for:
# 1. Reading Data
# 2. Cleaning Data
# 3. Analyzing Data
# 4. Manipulating Data
# 5. Creating DataFrames

# ==========================================================
# Import Pandas
# ==========================================================

import pandas as pd

# ==========================================================
# Pandas Series (1D Data)
# ==========================================================

series = pd.Series([10, 20, 30])

print("Series:")
print(series)

print("\nFirst Element:")
print(series[0])

# ==========================================================
# DataFrame using Dictionary
# ==========================================================

data = {
    "name": ["dheeraj", "kunal", "praveen", "anjali", "abhishek singh"],
    "age": [20, 21, 22, 23, 30],
    "salary": [15000, 20000, 25000, 30000, 35000]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)

# ==========================================================
# Save and Load Data
# ==========================================================

# CSV Import
df = pd.read_csv("file1.csv")

# CSV Export
df.to_csv("output.csv", index=False)

# JSON Import
df = pd.read_json("file1.json")

# JSON Export
df.to_json("output.json")

# Excel Import
df = pd.read_excel("file1.xlsx", sheet_name="Sheet1")

# Excel Export
df.to_excel("output.xlsx", index=False)

# ==========================================================
# GitHub Raw URL Example
# ==========================================================

url = "https://raw.githubusercontent.com/SujaanBhalla/grrass-dsml/main/Python/data%201.csv"
df = pd.read_csv(url)
print(df)


