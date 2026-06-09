# ==========================================================
# GRRAS Solutions - DSML with AI
# Author : Sujaan Bhalla
# Day 09 : Pandas Operations
# ==========================================================

# ==========================================================
# Create DataFrame
# ==========================================================

# 1. DataFrame for List (1D) -> Pandas Series

# 2. List -> Indexing Name (Pandas DataFrame)

# 3. DataFrame for Dictionary


# ==========================================================
# Import Pandas Package
# ==========================================================

import pandas as pd

# #1d-> method series 
# #example1.
# df = pd.Series((10,20,30))
# print(df)

# #dict 
# example1.2
# import pandas as pd 
# l = ((10,20,30))
# df = pd.series(data = l) 
# print(df)

# # example 2
# d = {"name" : "sujaan", "age" : " 18","rollno.":"91"}
# df = pd.Series(data=d, index = ["name","age","rollno."])
# print(df)
# #string is object why? 

# dict = {"name" : ["sujaan" , "emily" , "gabriel" , "garret" , "hannah" ]
#         , "roll_no":[1,2,3,4,5]
    
#         }
# df = pd.DataFrame(data=dict)
# print(df)

#csv
import pandas as pd
url = "https://raw.githubusercontent.com/sujaanbhalla/
df = pd.read_csv(url)
print(df)





#0 is row or column seres 1d