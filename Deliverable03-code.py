""" Ilinca Alecsndru
    Rose Baqeri
    Lauralie Tremblay """
    
    ## DELIVERABLE 03 
    
    
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


    
# 2. PRELIMINARY STEPS

# a) Initial data inspection



# b) Handle duplicate entries



# c) Identify and manage missing values



# d) Correct data types and formats: 
    
    
    