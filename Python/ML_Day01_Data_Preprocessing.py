# ==========================================================
# Day 15 - Data Preprocessing Practice
# Author : Sujaan Bhalla
# ==========================================================
# ==========================================================

# data pre processing
# import pandas as pd
# import numpy as np

# #create Dataset
# data= {
#        "Name": ["emily","selviy","gabriel","alfy","riya"],
#        "Age": [20, np.nan, 22, 21, 23],
#        "Marks": [99,95,96,97,np.nan]
# }

# df = pd.DataFrame(data)

# print("Orginal Data")
# print(df)

# print("\nMissing Values")
# print(df.isnull())

# print("\nCount Missing Values")
# print(df.isnull().sum())

# print("\nDrop Rows Having Missing Values")
# print(df.dropna())

# import pandas as pd 
# from sklearn.preproessing import LabelEncoder
# data = { "Gender": ["male", "female","male","female","male"]
# }

# df = pd.DataFrame(data)
# print("Original Data")
# print(df)

# #create encoder object
# le = LabelEncoder()

# #apply encoding
# df["Gender"] = le.fit_transform(df["Gender"])

# print("\nEncoded Data")
# print(df)

# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# data = {
#     "App": ["WhatsApp", "Telegram", "Instagram", "WhatsApp"]
# }

# df = pd.DataFrame(data)

# le = LabelEncoder()

# df["App"] = le.fit_transform(df["App"])

# print(df)

# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# data = {
#     'Name':['Ram','Kamal','Ajay','Neetu','Kavi','Sapu'],
#     'Age':[25,None,32,20,21,22],
#     'Salary':[5000,6000,None,7000,8000,9000],
#     'Gender':['male','male','male',None,'female','female']
# }

# df = pd.DataFrame(data)

# print("Original DataFrame")
# print(df)

# le = LabelEncoder()

# df_label = df.copy()

# df_label["Gender"] = df_label["Gender"].fillna("Unknown")

# df_label["Gender"] = le.fit_transform(df_label["Gender"])

# print("\nAfter Label Encoding")
# print(df_label)

# import pandas as pd
# from sklearn.preprocessing import LabelEncoder

# data = {
#     'Name':['Ram','Kamal','Ajay','Neetu','Kavi','Sapu'],
#     'Age':[25,None,32,20,21,22],
#     'Salary':[5000,6000,None,7000,8000,9000],
#     'Gender':['male','male','male','female','female','female']
# }

# df = pd.DataFrame(data)

# print("original dataframe")
# print(df)

# # Label Encoder
# le = LabelEncoder()

# df_label = df.copy()

# df_label['Gender_encoder'] = le.fit_transform(df_label['Gender'])
# print("After Label encoding")
# print(df_label)

# #one hot encoding
# import pandas as pd
# data = {
#     "colours": ["red" "violet", " lavender"]
# }

# df = pd.DataFrame(data)
# print("original data")
# print(df)

# encoded_df= pd.get_dummies(df,columns=['colours'])

# print("after one hot encoding")
# print(encoded_df)


# # handle missing values

# import pandas as pd
# import numpy as np
# import sklearn

# from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import OneHotEncoder

# # ==========================================================
# # Dataset
# # ==========================================================

# data = {
#     "colours": ["red", "green", "lavender", np.nan]
# }

# df = pd.DataFrame(data)

# print("\nhandle missing value")
# print(df)

# # ==========================================================
# # Handle Null Values
# # ==========================================================

# print("\nhandle null values")

# df.dropna(inplace=True)

# print(df)

# # ==========================================================
# # Label Encoding
# # ==========================================================

# print("\nlabel encoding")

# print("method 1")

# le = LabelEncoder()

# df['color_encoder'] = le.fit_transform(df['colours'])

# print(df)

# print("\nmethod 2")

# df['color_encoder2'] = LabelEncoder().fit_transform(df['colours'])

# print(df)

# print("\nmethod 3")

# df['color_encoder3'] = sklearn.preprocessing.LabelEncoder().fit_transform(
#     df['colours']
# )

# print(df)

# # ==========================================================
# # Drop Label Encoded Columns
# # ==========================================================

# print("\nbefore drop")

# print(df)

# df.drop(
#     ['color_encoder', 'color_encoder2', 'color_encoder3'],
#     axis=1,
#     inplace=True
# )

# print("\nafter drop")

# print(df)

# # ==========================================================
# # One Hot Encoding using Pandas
# # ==========================================================

# print("\nusing pandas")

# encoded_df = pd.get_dummies(
#     df,
#     columns=['colours']
# )

# print(encoded_df)

# # ==========================================================
# # One Hot Encoding using Sklearn
# # ==========================================================

# print("\using sklearn")

# encoder = OneHotEncoder()

# encoded = encoder.fit_transform(
#     df[['colours']]
# )

print(encoded.toarray())

#missing values , label encoding , one hot encoding 
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "age": [10, 20, 30, 40, np.nan],
    "gender": ["male", "female", "others", "female", np.nan],
    "name": ["gabriel", "emily", "karan", "camibble", "selviye"]
}

df = pd.DataFrame(data)

# Handle missing values in age
df["age"] = df["age"].fillna(df["age"].mean())

# Show gender column without NaN
print(df["gender"].dropna())

print("\nUpdated DataFrame")
print(df)

print("label encoding")
le = LabelEncoder()
df["gender1"] = le.fit_transform(df["gender"])
print(df)

print("one hot encoding")
print("using sk learn")
oe = OneHotEncoder()
oe_e = oe.fit_transformer(df["gender"])
print(oe_e.toarray())

print("using pandas")
oe = pd.get_dummies(df, 
                    df[["gender"]])
print(oe) 

import numpy as np
import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

# ==========================================================
# Create Dataset
# ==========================================================

data = {
    "age": [10, 20, 30, 40, np.nan],
    "gender": ["male", "female", "others", "female", np.nan],
    "name": ["gabriel", "emily", "karan", "camibble", "selviye"]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# ==========================================================
# Handle Missing Values
# ==========================================================

print("\nHandle Missing Values")

# Fill age with mean
df["age"] = df["age"].fillna(df["age"].mean())

# Fill gender with mode
df["gender"] = df["gender"].fillna(df["gender"].mode()[0])

print(df)

# ==========================================================
# Label Encoding
# ==========================================================

print("\nLabel Encoding")

le = LabelEncoder()

df["gender_encoded"] = le.fit_transform(df["gender"])

print(df)

# ==========================================================
# One Hot Encoding using Sklearn
# ==========================================================

print("\nOne Hot Encoding using Sklearn")

encoder = OneHotEncoder()

encoded = encoder.fit_transform(df[["gender"]])

print(encoded.toarray())

# ==========================================================
# One Hot Encoding using Pandas
# ==========================================================

print("\nOne Hot Encoding using Pandas")

encoded_df = pd.get_dummies(
    df,
    columns=["gender"]
)

print(encoded_df)

