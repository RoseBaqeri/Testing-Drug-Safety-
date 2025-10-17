############## DELIVRABLE - 2 ##############

# Names: Ilinca A., Rose B., Lauralie T.
# Date: 16/10/25

# ===================== Importing Modules =====================

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# ===================== Importing Dataset to program:=====================
data = json.load(open('drug-event-0012-of-0031.json'))
df = pd.json_normalize(data['results'])


# ===================== Remove those with empty values (only keep rows that have all required fields) =====================
df_cleaned = df.dropna(
    subset=[
        "patient.patientsex",
        "patient.patientonsetage",
        "patient.patientweight",
        "serious",
        "patient.reaction",
        "patient.drug",
    ])

df = df_cleaned.copy()

# ===================== Force the result to be numerica data, when applicapble =====================

weight = pd.to_numeric(df["patient.patientweight"].sample(300), errors="coerce")
sex = pd.to_numeric(df["patient.patientsex"].sample(300), errors="coerce")
age = pd.to_numeric(df["patient.patientonsetage"].sample(300), errors="coerce")
severity = pd.to_numeric(df["serious"].sample(300), errors="coerce")

## errors="coerce" -> used to fix error tha tappears due to the presence of "nan" in the dataset under some colums.


### TO DO: add an statistical explination to back up results, since we only used 25% of the data from the dataset due to its large capacity


# ===================== 1. Histogram: Patient Weights =====================

num_bins = 10
min_weight = weight.min()
max_weight = weight.max()
bins = np.linspace(min_weight, max_weight, num_bins + 1)

plt.figure(figsize=(10, 6))
sns.histplot(data=weight, bins=bins, kde=False, color="skyblue")
plt.title('Histogram of Patient Weights with Custom Bins')
plt.xlabel('Patient Weight (kg)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
# shows distribution of patient weights among reports.


# ===================== 2. Histogram: Patient Ages =====================

num_bins = 10
min_age = age.min()
max_age = age.max()
bins = np.linspace(min_age, max_age, num_bins + 1)

plt.figure(figsize=(10, 6))
sns.histplot(data=age, bins=bins, kde=False, color="lightgreen")
plt.title('Histogram of Patient Ages with Custom Bins')
plt.xlabel('Patient Age (years)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
# displays distribution of patient ages.


# ===================== 3. Scatter Plot: Age vs Weight =====================

plt.figure(figsize=(10, 6))
sns.scatterplot(x=age, y=weight, hue=severity, palette="coolwarm")
plt.title('Scatter Plot: Age vs Weight (Red = Non-Serious, Blue = Serious)')
plt.xlabel('Patient Age (years)')
plt.ylabel('Patient Weight (kg)')
plt.grid(True)
plt.tight_layout()
plt.show()

# red dots correspond with the non-serious cases while the blue dots (1.0) correspond with the serious cases
# examines relationship between age, weight, and report seriousness.


# ===================== 4. Pie Chart: Serious vs Non-Serious =====================

ser_counts = df["serious"].value_counts() #.value_counts()-> counts how many times how many times 1 or 2 appear in the columns 

plt.figure(figsize=(8, 8))
plt.pie(
    ser_counts,
    labels=["Serious","Non-Serious"], # replaces the 1.0 and 2.0 results from the index to what they represent
    autopct="%1.1f%%", # makes it so that the percentages are shown on the chart + how many decimals are included in the results
)
plt.title("Proportion of Serious vs Non-Serious Reports")
plt.show()




