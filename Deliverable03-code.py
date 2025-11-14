""" Ilinca Alecsndru
    Rose Baqeri
    Lauralie Tremblay """
    
    ## DELIVERABLE 03 

# 1. POSSIBLE QUESTIONS TO ANSWER:

# 1. Does patient age influence the seriousness of adverse drug reactions?


# 2. Are there differences in the types of adverse reactions reported by males and females?


# 3. Which countries report the highest proportion of serious adverse events?


# 4. Do reporting delays differ depending on the reporter’s professional role (e.g., physician, pharmacist, consumer)?


# 5. Which drugs are most frequently associated with hospitalization or other serious outcomes?

    
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

print('PART 2 - a) ============================================================================') # used to seperate each question results, without it the reslts were kind of confusing

# print(df.head())

# print(df.shape())

# print(df.info())

# print(df.describe())





# b) Handle duplicate entries

print('PART 2 - b) ============================================================================')

# print(df.duplicated().sum())

# df = df.drop_duplicates()

# print(df.duplicated().sum())   



# c) Identify and manage missing values

print('PART 2 - c) ============================================================================')

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

    
num_cols = ['patient.patientonsetage', 'patient.patientweight','serious','seriousnessdeath','seriousnesslifethreatening','seriousnesshospitalization','seriousnessdisabling','seriousnessother']

for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')


date_cols = ['transmissiondate', 'receivedate', 'receiptdate']

for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')
    
categorical_cols = ['primarysourcecountry','occurcountry','reporttype','primarysource.qualification','sender.sendertype','receiver.receivertype','patient.patientsex']

for col in categorical_cols:
    df[col] = df[col].astype('object')
    
    
    
# 3. UNIVARIATE NON-GRAPHICAL EDA

print('PART 3 - a) ============================================================================') 

for col in num_cols:
 
    print("Column Title:", col) # let's us know what numerical column the loop is on
    print("MEAN:", df[col].mean())
    print("MEDIAN:", df[col].median())
    print("MODE:", df[col].mode()[0])
    print("SD:", df[col].std())
    print("VARIANCE:", df[col].var())
    print("SKEWNESS:", df[col].skew())
    print("KURTOSIS:", df[col].kurt())
    print("1st QUARTILE; (0.25):", df[col].quantile(0.25))
    print("2nd QUARTILE; (0.50):", df[col].quantile(0.50))
    print("3rd QUARTILE; (0.75):", df[col].quantile(0.75))
    print('------------------------------------------------------') # used to seperate each result from the loops

## 

print('PART 3 - a) ============================================================================')

for col in categorical_cols:
   
   
    print("FREQUENCY:", df[col].value_counts())
    print("PROPORTIONS:", df[col].value_counts(normalize=True))
    print("MODE: Most frequent category", df[col].mode()[0])
    print("NUMBER OF UNIQUE CATEGORIES:", df[col].nunique())
    print('------------------------------------------------------')
   
 ##
   
    
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
    
    








# 6. MULTIVRIATE GRAPHICAL EDA

# 6.1. Visualizing Statistical Relationships (5 plots):
    
    # a) A plot using Faceting feature (col parameter in the relplot() function)


    # b) A plot representing 5 variables at once (x, y, hue, size, col)
    
    
    # c) A plot using line instead of points (find a variable that makes sense emphasizing continuity and explain why)
    
    
    # d) A plot illustrating standard deviation
    
    
    # e) A plot including a linear regression
    
    
    
# 6.2. Visualizing categorical data (10 plots):
    
    #ANSWERING: Do reporting delays differ depending on the reporter’s professional role (e.g., physician, pharmacist, consumer)?
    
    # a) 1 categorical scatter plot with jitter enabled
    
sns.catplot(data = df, x = "occurcountry", y = "")
    
    # b) 1 categorical scatter plot with jitter disabled (explain your choice of variable for this one)
    
    
    # c) 1 "beeswarm" plot representing 3 variables
    
    
    # d) 1 box plot representing 3 variables
    
    
    # e) 1 box plot showing the shape of the distribution (boxenplot())
    
    
    # f) 1 split violin plot representing 3 variables with bandwidth adjusted for better visualization
    
    
    # g) 1 violin plot with scatter points inside the violin shapes
    
    
    # h) 1 bar plot representing 3 variables showing 97% confidence intervals
    
    
    # i) 1 point plot representing 3 variables showing 90% confidence intervals and lines in dashed style
    
    
    # j) 1 bar plot showing the number of observations in each category
    
    
    
# 6.3. Visualizing Bivariate Distributions (3 plots):
    
    # a) 1 "heatmap" plot representing 2 variables with colour intensity bar and adjusted bin width
    
    
    # b) 1 distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot())
    
    
    # c) 1 "heatmap" plot representing 3 variables, again of kind kde