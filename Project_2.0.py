############## DELIVRABLE - 2 ##############

# Names: Ilinca A., Rose B., Lauralie T.
# Date: 16/10/25

# Importing modules:

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Importing Dataset to program:
data = json.load(open('drug-event-0012-of-0031.json'))
df = pd.json_normalize(data['results'])

# Remove those with empty values
df_cleaned = df.dropna(subset=['patient.patientweight'])

# Force the result to be numerica data
weight = pd.to_numeric(df_cleaned["patient.patientweight"].sample(100))


# Define number of bins based on min and max weight found
num_bins = 10
min_weight = weight.min()
max_weight = weight.max()
bins = np.linspace(min_weight, max_weight, num_bins + 1)


# Plot histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=weight, bins=bins, kde=False)
plt.title('Histogram of Patient Weights with Custom Bins')
plt.xlabel('Patient Weight (kg)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
