import pandas as pd

data = {
    "name": ["dheeraj", "kunal", "praveen", "anjali", "abhishek singh"],

    "age": [20, 21, 22, 23, 24],

    "salary": [
        {"In-hand": 15000, "ctc": "1.2lpa"},
        {"In-hand": 20000, "ctc": "2.2lpa"},
        {"In-hand": 25000, "ctc": "3.2lpa"},
        {"In-hand": 30000, "ctc": "3.2lpa"},
        {"In-hand": 40000, "ctc": "4.2lpa"}
    ]
}

df = pd.DataFrame(data)

print(df)



import pandas as pd

data = {
    "name": ["dheeraj", "kunal", "praveen", "anjali", "abhishek singh"],

    "age": [20, 21],

    "salary": [
        {"In-hand": 15000, "ctc": "1.2lpa"},
        {"In-hand": 20000, "ctc": "2.2lpa"},
        {"In-hand": 25000, "ctc": "3.2lpa"},
        {"In-hand": 30000, "ctc": "3.2lpa"},
        {"In-hand": 40000, "ctc": "4.2lpa"}
    ]
}

df = pd.DataFrame(data)

# 

import pandas as pd

url = "https://raw.githubusercontent.com/sujaanbhalla/grrass-dsml/main/file1.csv"

df = pd.read_csv(url)

print(df)

