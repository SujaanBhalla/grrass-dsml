## ==========================================================
# GRRAS Solutions - DSML with AI
# Author : Sujaan Bhalla
# Day 09 & Day 10 & Day 11: Pandas Operations
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
# import pandas as pd

data = {
    "Emp_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Amit", "Riya", "Raj", "Sara", "John", "Neha"],
     "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
"Salary": [50000, 45000, 60000, 55000, 48000, 52000],
"Experience": [2, 3, 5, 4, 1, 3]
}

df = pd.DataFrame(data)

print(df)
print(df.loc[0, "name"])
print(df.loc[2,"Salary"])
print(df.loc[1:3,["Name","Salary"]])
print(df.loc[2, 1])
print(df.iloc[2, 1])
print(df.iloc[0:3,1:4])

df2 = df.drop("Salary",axis=1)
print(df2)

import pandas as pd

df = pd.read_json("student-data (1).json")

print(df)


# # print(df.loc[0])
# print(df.loc[0],[1])
# print("\n", df.loc[])
#filter 1
print("filter1")
print(df[df["english"] ==95])
print("filter2")
#filter 2
print(df[df["maths"] < 60])
print("Filter 3")
#filter 3
print(df[df["physics"]<=56])
#math 
#names 
print("name")
print(df[(df["maths"]> 90) & (df["english"]> 90) & (df["gender"] == "Male")])

import pandas as pd

# Read JSON file
df = pd.read_json("student-data.json")

# ==========================
# Display Dataset
# ==========================
print("Original DataFrame:\n")
print(df)

# ==========================
# Basic Information
# ==========================
print("\nFirst 5 Rows:")
print(df.head())

print("\nLast 5 Rows:")
print(df.tail())

print("\nShape:")
print(df.shape)

# ==========================
# loc Examples
# ==========================
print("\nFirst Student:")
print(df.loc[0])

print("\nFirst Student Name:")
print(df.loc[0, "name"])

print("\nRajesh Maths Marks:")
print(df.loc[1, "maths"])

print("\nFirst 3 Students (Name & Physics):")
print(df.loc[0:2, ["name", "physics"]])

# ==========================
# iloc Examples
# ==========================
print("\nFirst Row:")
print(df.iloc[0])

print("\nSecond Row, First Column:")
print(df.iloc[1, 0])

print("\nFirst 3 Rows, First 2 Columns:")
print(df.iloc[0:3, 0:2])

# ==========================
# Drop Column
# ==========================
print("\nWithout Gender Column:")
df2 = df.drop("gender", axis=1)
print(df2)

# ==========================
# Filtering
# ==========================
print("\nStudents with English = 95:")
print(df[df["english"] == 95])

print("\nStudents with Maths < 60:")
print(df[df["maths"] < 60])

print("\nStudents with Physics <= 56:")
print(df[df["physics"] <= 56])

print("\nFemale Students:")
print(df[df["gender"] == "Female"])

print("\nMale Students:")
print(df[df["gender"] == "Male"])

print("\nMale Students with Maths > 90 and English > 90:")
print(
    df[
        (df["gender"] == "Male")
        & (df["maths"] > 90)
        & (df["english"] > 90)
    ]
)

# ==========================
# Select Columns
# ==========================
print("\nName Column:")
print(df["name"])

print("\nName and Maths Columns:")
print(df[["name", "maths"]])

