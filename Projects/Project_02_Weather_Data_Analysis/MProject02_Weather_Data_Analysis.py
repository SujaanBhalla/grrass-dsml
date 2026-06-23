# ==========================================================
# GRRAS Solutions - DSML with AI
# Author : Sujaan Bhalla
# Project 02 - Weather Data Analysis
# ==========================================================

import pandas as pd 
import matplotlib.pyplot as plt

# ==========================================================
# 1. Load Dataset
# ==========================================================

url = ""
df = pd.read_json(url)

print("Original Dataset")
print(df)

# ==========================================================
# 2. Data Cleaning
# ==========================================================

# Remove Row Index 2
df.drop(2, inplace=True)

# Fill Missing Humidity Values with Mean
df["humidity_pct"].fillna(
    df["humidity_pct"].mean(),
    inplace=True
)

# ==========================================================
# 3. Feature Engineering
# ==========================================================

# Celsius to Fahrenheit

df["fahrenhiet"] = (
    df["temperature_c"]* 1.8
) + 32

print("\n Updated Dataset")
print(df)

# ==========================================================
# 4. Data Visualization
# ==========================================================

fig, aux = plt.subplots(2,2, figsize=(10,8))

# ----------------------------------------------------------
# Temperature Chart
# ----------------------------------------------------------

aux[0][0].plot(
    df["day"]
    df["temperature_c"]
    marker = "o"
)

aux[0][0].set_title("Temperature (Celsius)")
aux[0][0].set_xlabel("Days")
aux[0][0].set_ylabel("Temperature")

# ----------------------------------------------------------
# Humidity Chart
# ----------------------------------------------------------

aux[0][1].plot(
    df["day"],
    df["humidity_pct"],
    marker="o"
)

aux[0][1].set_title("Humidity")
aux[0][1].set_xlabel("Days")
aux[0][1].set_ylabel("Humidity %")

# ----------------------------------------------------------
# Fahrenheit Chart
# ----------------------------------------------------------

aux[1][0].plot(
    df["day"],
    df["fahrenheit"],
    marker="o"
)

aux[1][0].set_title("Temperature (Fahrenheit)")
aux[1][0].set_xlabel("Days")
aux[1][0].set_ylabel("Fahrenheit")

# ----------------------------------------------------------
# Weather Condition Chart
# ----------------------------------------------------------

aux[1][1].plot(
    df["day"]
    df["condition"]
)

aux[1][1].set_title("Weather Conditions")
aux[1][1].set_xlabel("Days")
aux[1][1].set_ylabel("Condition")

# ==========================================================
# 5. Display Charts
# ==========================================================

plt.tight_layout()
plt.show()