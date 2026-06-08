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
# df = pd.read_csv("file1.csv")

# CSV Export
# df.to_csv("output.csv", index=False)

# JSON Import
# df = pd.read_json("file1.json")

# JSON Export
# df.to_json("output.json")

# Excel Import
# df = pd.read_excel("file1.xlsx", sheet_name="Sheet1")

# Excel Export
# df.to_excel("output.xlsx", index=False)

# ==========================================================
# GitHub Raw URL Example
# ==========================================================

# url = "https://raw.githubusercontent.com/username/repository/main/file1.csv"
# df = pd.read_csv(url)

# ==========================================================
# Basic DataFrame Understanding
# ==========================================================

# First 5 Rows
# print(df.head())

# Last 5 Rows
# print(df.tail())

# Shape of DataFrame
# print(df.shape)

# Information about Dataset
# print(df.info())

# Statistical Summary
# print(df.describe())

# ==========================================================
# Column Operations
# ==========================================================

# Select a Column
# print(df["name"])

# Add a New Column
# df["city"] = ["Jaipur", "Delhi", "Mumbai", "Pune", "Kota"]

# Delete a Column
# df = df.drop("city", axis=1)

# ==========================================================
# Row Operations
# ==========================================================

# Label Based Access
# print(df.loc[0, "name"])

# Index Based Access
# print(df.iloc[1])

# ==========================================================
# Filter DataFrame
# ==========================================================

# Age Greater Than 22
# print(df[df["age"] > 22])

# ==========================================================
# Sorting
# ==========================================================

# Sort by Age
# print(df.sort_values("age"))

# ==========================================================
# Topics Covered Today
# ==========================================================

# ✅ Pandas Introduction
# ✅ Series
# ✅ DataFrame
# ✅ CSV Import / Export
# ✅ JSON Import / Export
# ✅ Excel Import / Export
# ✅ GitHub Raw URL Dataset
# ✅ head()
# ✅ tail()
# ✅ shape
# ✅ info()
# ✅ describe()
# ✅ Column Operations
# ✅ Row Operations
# ✅ Filtering
# ✅ Sorting

# ==========================================================
# Upcoming Topics
# ==========================================================

# Working with Date Values
# Handling Missing Values
# Aggregation and GroupBy
# Concatenate DataFrames
# Merge DataFrames (Joins)