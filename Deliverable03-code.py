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

    
# 2. PRELIMINARY STEPS

# a) Initial data inspection

print(df.head())

print(df.shape())

print(df.info())

print(df.describe())





# b) Handle duplicate entries

print(df.duplicated().sum())

df = df.drop_duplicates()

print(df.duplicated().sum())   



# c) Identify and manage missing values

for col in df.columns:
    print(col, df[col].isnull().sum())
    
    ## we dicided to not use option a ; (drop rows with missing values), because our dataset contains reports about drug dafety. dropping rows would mean deleting real events/information.
    ## We instead decided to use options b and c and filli in numerical missing values with mean/median and categorical missing values with strings.

# numeric    
for col in df.columns:
    if df[col].dtype != 'object':   #'object' refers to the empty empty spaces
        df[col] = df[col].fillna(df[col].median())

#justification : The numerical variables in this dataset (ex// patient age & weight) are very skewed and contain outliers. Because the mean is very sensitive to extreme values, it would not represent the middle tendency accurately. so, we chose to fill numerical missing values using the median.

# categorical        
for col in df.columns:
    if df[col].dtype == 'object':   
        df[col] = df[col].fillna("Unknown")
        
#justification : replaced with “Unknown” so we can still analyze the reports (they remain complete)

# d) Correct data types and formats: 
    
num_cols = ['patient.patientonsetage', 'patient.patientweight','serious','seriousnessdeath','seriousnesslifethreatening','seriousnesshospitalization','seriousnessdisabling','seriousnesscongenitalanomaly','seriousnessother']

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')


date_cols = ['transmissiondate', 'receivedate', 'receiptdate']

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')
    
categorical_cols = ['primarysourcecountry','occurcountry','reporttype','primarysource.qualification','sender.sendertype','receiver.receivertype','patient.patientsex']

for col in categorical_cols:
    df[col] = df[col].astype('object')
    
    
    
# 3. UNIVARIATE NON-GRAPHICAL EDA

    # MEAN
    
    
    # MEDIAN
    
    
    # MODE
    
    
    # STANDARD DEVIATION
    
    
    # VARIANCE
    
    
    # SKEWNESS
    
    
    # JURTOSIS
    
    
    # QUARTILES
    
    
    # FREQUANCY COUNTS 
    
    
    # PROPRTION
    
    
    # MODE (MOST FREQUENT CATEGORY AND THE NUMBER OF UNIQUE CATEGORIES)
    
    
# 4. UNIVARIATE GRAPHICAL EDA

    # a) Custom and appropriate number of bins
    
    
    
    # b) Conditioning on other variables
    
    
    
    # c) Stacked histogram
    
    
    
    # d) Dodge bars
    
    
    
    # e) Normalized histogram statistics
    
    
    
    # f) Kernel density estimation (choosing the smoothing bandwidth)
    
    
    
    # g) Empirical cumulative distributions
    
    
    
    
 # ===========================   
        
    # a) What is the distribution of the variable? (is the data normally distributed, skewed, bimodal, etc?)
    
    
    # b) Are there any outliers? (are there extreme values that fall outside the typical range?)
    
    
    # c) What is the spread and central tendency? (where is the median? How spread out is the data?)
    
    
    # d) Is the data symmetric or skewed? (is the data skewed left or right?)
    
    
    # e) How frequent are certain ranges of values? (which value ranges are most common?) 
    
    








    
