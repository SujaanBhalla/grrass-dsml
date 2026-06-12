
# # ==========================================================
# # GRRAS Solutions - DSML with AI
# # Author : Sujaan Bhalla
# # Day 12 - Pandas Data Manipulation
# # ==========================================================
import pandas as pd 
# # Read the JSON file 
df = pd.read_json("student-data.json")
print(df)
# # ==========================================================
# # 1. Sorting Data
# # ==========================================================
# print("Sorting")
# print("Ascending order")
# # Sort in Ascending Order (Default)
# # sort_values()
# df.sort_values("english",inplace=True)
# print(df)

# # # Sort in Descending Order
# print("Descending")
# # ascending=False
# df.sort_values("english",ascending=False,inplace=True)
# print(df)

# # Sort by Single Column
# print("Sort by Single Column")
# #using by
# print("using by ascending by default")
# df.sort_values(by="english")
# print(df)

# # Sort by Single Column (English - Descending)
# print("Sort by Single Column (English - Descending)")
# print(df.sort_values(by="english", ascending=False))

# # Sort by Single Column (Maths)
# print("Sort by Single Column (Maths)")
# print(df.sort_values(by="maths"))

# # Sort by Single Column (Physics)
# print("Sort by Single Column (Physics)")
# print(df.sort_values(by="physics"))

# # Sort by Multiple Columns
# print("Sort by Multiple Columns")
# # Sort by English (Highest → Lowest)
# # If English marks are equal, sort by Maths (Lowest → Highest)
# print("english(descending) maths(ascending)")
# print(df.sort_values(by=['english','maths'],ascending=[False,True]))
# #sorting on name:
# print("sorting on name")
# print(df.sort_values("name"))

# print("making all letter short in name")
# df['name'] = df['name'].str.lower()
# print(df)
# print("name in ascending order by default")
# print(df.sort_values("name"))


# # ==========================================================
# # 2. Add New Column
# # ==========================================================

# # Create a New Column
#add column total = physicss  + math + en
df["total"] = df["physics"] + df['maths'] + df['english']
print(df)


# # Calculate a New Column from Existing Columns

# # Add Constant Values to a Column


# # ==========================================================
# # 3. Update Existing Column
# # ==========================================================

# # Update Entire Column

# # Update Selected Rows

# # Update Values using loc

# # Update Values using iloc


# # ==========================================================
# # 4. Add New Row
# # ==========================================================

# # Add Single Row
print("Add Single Row")
df.loc[14] = ["Emily","Female",80,90,87,257]
print(df)

# # Add Multiple Rows

# # Concatenate DataFrames


# # ==========================================================
# # 5. Update Existing Row
# # ==========================================================

# # Update Row using loc

# # Update Specific Cell

# # Update Multiple Columns in One Row


# # ==========================================================
# # 6. Delete / Drop Columns
# # ==========================================================

# # Drop Single Column
print("Drop Single Column")
print(df.drop("total",axis=1))


# # Drop Multiple Columns

# # Drop with axis=1


# # ==========================================================
# # 7. Delete / Drop Rows
# # ==========================================================

# # Drop Single Row
# print("Drop Single Row")
# print(df.drop(14,axis=0))


# # Drop Multiple Rows
# print("Drop Multiple Rows")

# # Drop by Index

# # Drop with inplace=True


# # ==========================================================
# # 8. Missing Values
# # ==========================================================

# # Create Missing Values

# # Find Missing Values
# # isnull()

# # Count Missing Values
# # isnull().sum()

# # Check if Any Missing Values Exist
# # isnull().any()

# # Check Non-Missing Values
# # notnull()

# # Fill Missing Values
# # fillna()

# # Drop Missing Values
# # dropna()


# ==========================================================
# Date
# ==========================================================
df.drop([6,7,8,9,10,11,12,13,14], inplace=True)

df["doj"] = [
    "2025-01-01",
    "2025-01-02",
    "2025-01-03",
    "2025-01-04",
    "2025-01-05",
    "2025-01-06"
]

# Check data type before conversion
print("Check data type before conversion")
print(df["doj"].dtype)

# Convert string to datetime
print("Convert string to datetime")
df["doj"] = pd.to_datetime(df["doj"])

# Check data type after conversion
print("Check data type after conversion")
print(df["doj"].dtype)

# Extract Year
print("Extract Year")
print(df["doj"].dt.year)

# Extract Month
print("Extract Year")
print(df["doj"].dt.month)

# Extract Day
print("Extract Day")
print(df["doj"].dt.day)

# Extract Day Name
print("Extract Day Name")
print(df["doj"].dt.day_name())

# Extract Month Name
print("Extract Month Name")
print(df["doj"].dt.month_name())

# Add 20 days to each date using unit='D'
print("Add 20 days to each date using unit='D'")
print(df["doj"] + pd.to_timedelta(20,unit="D"))

# Add 20 days using a string format
print("Add 20 days using a string format")
print(df["doj"] + pd.to_timedelta("20 days"))

# ==========================================================
# 9. Practice with student-data.json
# ==========================================================

# Sort Physics Marks (Low → High)

# Sort Physics Marks (High → Low)

# Sort Maths Marks (Ascending)

# Sort English Marks (Descending)

# Add Total Marks Column

# Add Average Marks Column

# Update Arun's Physics Marks

# Update Rajesh's English Marks

# Add a New Student

# Delete a Student

# Delete Gender Column

# Find Missing Values

# Fill Missing Values

# Remove Rows Having Missing Values


# ==========================================================
# 10. Revision Questions
# ==========================================================

# Q1. Sort students by Maths in descending order.

# Q2. Sort students by English in ascending order.

# Q3. Add a column named "Total".

# Q4. Add a column named "Percentage".

# Q5. Update Gowri's English marks to 99.

# Q6. Delete the "gender" column.

# Q7. Delete the first row.

# Q8. Count missing values in each column.

# Q9. Fill missing values with 0.

# Q10. Remove rows containing missing values.

