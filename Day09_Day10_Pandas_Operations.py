# ==========================================================
# GRRAS Solutions - DSML with AI
# Author : Sujaan Bhalla
# Day 09 & Day10: Pandas Operations
# ==========================================================

#dataframme creating file
import pandas as pd
dict = {
    "name": ["sujaan", "emily", "gabriel", "garret", "hannah"],
    "roll_no": [1, 2, 3, 4, 5]
}
df = pd.DataFrame(data=dict)
print(df)


#csv file import
import pandas as pd
url = "https://raw.githubusercontent.com/SujaanBhalla/grrass-dsml/main/Python/data%201.csv"
df = pd.read_csv(url)
print(df)

#json import of the file:
import pandas as pd
url = "https://raw.githubusercontent.com/SujaanBhalla/grrass-dsml/main/Python/data%201.json"
df = pd.read_json(url, lines=True)
print(df)

# ==========================================================
# Basic DataFrame Understanding
# ==========================================================

#First 5 Rows
print(df.head())

# Last 5 Rows
print(df.tail())

# Shape of DataFrame
print(df.shape)

# Information about Dataset
print(df.info())

# Statistical Summary
print(df.describe())

#get single column data(increment)
df["Increment"] = df["Salary"] * 0.10
print(df)

#get single column data (marks)
df["Name"]
df["Salary"]= df["Marks"] + 100
df["Salary"] = [100,200,300,400,500,600]
print(df)

#update the column
df["Increment"] = df["Salary"] * 0.10
df["Salary"] = df["Salary"] + df["Increment"]
print(df)

# ==========================================================
# Rename Column
# ==========================================================

# Rename the "Name" column to "Employee_Name"
df = df.rename(columns={"Name": "Employee_Name"})
print(df)

