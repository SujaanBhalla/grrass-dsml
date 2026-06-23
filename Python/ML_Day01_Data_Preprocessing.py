# ==========================================================
# Day 15 - Data Preprocessing Practice
# Author : Sujaan Bhalla
# ==========================================================
# # data pre processing
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

#one hot encoding
import pandas as pd
data = {
    "colours": ["red" "violet", " lavender"]
}

df = pd.DataFrame(data)
print("original data")
print(df)

encoded_df= pd.get_dummies(df,columns=['colours'])

print("after one hot encoding")
print(encoded_df)

