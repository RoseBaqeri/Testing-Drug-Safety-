############## DELIVRABLE - 2 ##############

# Names: Ilinca A., Rose B., Lauralie T.
# Date: 17/10/25

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


### We used a random 25% sample from the dataset to make the analysis less overwhelming due to the size of indeexes in the dataset, 
# while still keeping good accuracy. 
# This sample size provides results that are generally close to what we would get from using all the data, 
# though the precision is about TWO TIMES LOWER because the sample represents only a 25% of the dataset. 
# Running the code multiple times and averaging the results could reduce the random variation and give more true results. 
# Overall, this approach gave us reliable results and the more times we repeated it, 
# the closer our averages became to the true values of the full dataset.




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
# helps identify if certain weight groups are more succeptible than others to reactions

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
# helps identify if certain age groups are more succeptible than others to reactions

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

# lets us know be able to visualize the protportion of severe cases from those reported

# ===================== 5. Two subplots side by side =====================

age_bins = np.linspace(age.min(), age.max(), 10)
weight_bins = np.linspace(weight.min(), weight.max(), 10)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

ax1.hist(age, bins=age_bins, color='lightblue', edgecolor='black')
ax1.set_title('Distribution of Patient Ages')
ax1.set_xlabel('Patient Age (years)')
ax1.set_ylabel('Frequency')
ax1.grid(True)


ax2.hist(weight, bins=weight_bins, color='darkred', edgecolor='black')
ax2.set_title('Distribution of Patient Weights')
ax2.set_xlabel('Patient Weight (kg)')
ax2.set_ylabel('Frequency')
ax2.grid(True)


fig.suptitle('Patient Age and Weight Distributions (Two Subplots Side by Side)')
plt.tight_layout()
plt.show()

#this figure contains two subplots side by side. to the left: histogram of patient ages. to the right: histogram of patient weights.
#this helps visualize how these two key variables are distributed within the dataset.

# ===================== 4. Multiple arrays in one plot (different colours & line styles =====================

x = np.arange(len(age))

age_smooth = pd.Series(age).rolling(window=10).mean()
weight_smooth = pd.Series(weight).rolling(window=10).mean()

plt.figure(figsize=(10, 6))
plt.plot(x, age_smooth, color='green', linestyle='-', label='Average Patient Age')
plt.plot(x, weight_smooth, color='pink', linestyle='--', label='Average Patient Weight')

plt.title('Comparison of Patient Age and Weight Trends')
plt.xlabel('Sample Index')
plt.ylabel('Value')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

#this plot compares two different numeric variables from the dataset - patient age and patient weight.
#Both are plotted on the same axes with distinct colours and line styles to highlight their differences.







