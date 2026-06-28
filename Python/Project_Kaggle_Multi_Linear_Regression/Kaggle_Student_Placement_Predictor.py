#import libraries 

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#Read Dataset

url = "https://raw.githubusercontent.com/SujaanBhalla/grrass-dsml/refs/heads/main/Python/Project_Kaggle_Multi_Linear_Regression/student_placement_dataset.csv"
df = pd.read_csv(url)
print("Dataset")
print(df.head())

print("\n Columns")
print(df.columns)

#input features
X = df[[
    "cgpa",
    "internships_count",
    "projects_count",
    "certifications_count",
    "coding_skill_score",
    "aptitude_score",
    "communication_skill_score",
    "logical_reasoning_score",
    "hackathons_participated",
    "github_repos",
    "linkedin_connections",
    "mock_interview_score",
    "attendance_percentage",
    "backlogs",
    "extracurricular_score",
    "leadership_score",
    "sleep_hours",
    "study_hours_per_day"
]]

y = df["salary_package_lpa"]

#train test split
X_train, X_test, y_train , y_test = train_test_split(
    X,
    y,
    test_size = 0.2, 
    random_state = 3
)

#model training
model = LinearRegression()
model.fit(X_train, y_train)
print("Model Trained Successfully")

#Prediction
new_data = pd.DataFrame({
    "cgpa":[8.5],
    "internships_count":[2],
    "projects_count":[5],
    "certifications_count":[3],
    "coding_skill_score":[90],
    "aptitude_score":[85],
    "communication_skill_score":[80],
    "logical_reasoning_score":[82],
    "hackathons_participated":[2],
    "github_repos":[6],
    "linkedin_connections":[500],
    "mock_interview_score":[88],
    "attendance_percentage":[90],
    "backlogs":[0],
    "extracurricular_score":[70],
    "leadership_score":[65],
    "sleep_hours":[7],
    "study_hours_per_day":[5]
})

prediction = model.predict(new_data)
print("Predicted Package(LPA)")
print(prediction[0])

#seaborn 
sns.pairplot(
    df[[
        "cgpa",
        "coding_skill_score",
        "apitude_score",
        "salary_package_lpa"
    ]]
)
plt.show()

sns.heatmap(
    df[[
        "cgpa",
        "coding_skill_score",
        "aptitude_score",
        "salary_package_lpa"
    ]].corr(),
    annot = True
)

plt.show()

sns.scatterplot(
    x="cgpa",
    y="salary_package_lpa",
    data=df
)

plt.show()

sns.scatterplot(
    x="coding_skill_score",
    y= "salary_package_lpa",
    data=df
)

plt.show()

#Dump Model 
joblib.dump(
    model,
    "student_placement_model.joblib"

)

print("Model Saved Successfully")