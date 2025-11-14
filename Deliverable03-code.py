""" Ilinca Alecsndru
    Rose Baqeri
    Lauralie Tremblay """
    
    ## DELIVERABLE 03 

# 1. POSSIBLE QUESTIONS TO ANSWER:

# 1. Does patient age influence the seriousness of adverse drug reactions?
    #see pt4
# 2. How do patient weight distributions differ between patients who experienced serious vs. non-serious reactions?
    #see pt4
    
# 3. Are certain types of serious outcomes (hospitalization, life-threatening events, death) reported more frequently in specific countries?
# 4. Do reporting delays differ depending on the reporter’s professional role (e.g., physician, pharmacist, consumer)?
# 5. Are there differences in the types of adverse reactions reported by males and females?

#<<<<<<< HEAD
  
# 3. Are certain types of serious outcomes (hospitalization, life-threatening events, death) reported more frequently in specific countries?
# 4. Do reporting delays differ depending on the reporter’s professional role (e.g., physician, pharmacist, consumer)?
# 5. Are there differences in the types of adverse reactions reported by males and females?

#==========
    # ===================== Importing Modules =====================

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


    # ===================== Importing Dataset to program:=====================
data = json.load(open('drug-event-0012-of-0031.json'))
df = pd.json_normalize(data['results'])

# =============================================================================================================================================================================================       
    
# 2. PRELIMINARY STEPS

# a) Initial data inspection

print('PART 2 - a) ============================================================================') # used to seperate each question results, without it the reslts were kind of confusing

print('HEAD:', df.head())
print('------------------------------------------------------')

print("SHAPE:", df.shape)
print('------------------------------------------------------')

print("INFO:", df.info())
print('------------------------------------------------------')

print('DESCRIBE:', df.describe())
print('------------------------------------------------------')


# b) Handle duplicate entries

print('PART 2 - b) ============================================================================')

### due to the nature of the json file i could not run the code without cleaning the df, instead of dropping the rows with missing values, i decided to remove the columns that all the column that we won't be using for outr analysis, preventing any errors that might come from them. i found the df.drop(column='') function for this

df = df.drop(columns=['safetyreportversion','transmissiondateformat','receivedateformat','receiptdateformat','sender.senderorganization','receiver.receiverorganization','companynumb','authoritynumb','fulfillexpeditecriteria','primarysource.literaturereference','patient.summary.narrativeincludeclinical','duplicate','reportduplicate.duplicatesource',
    'reportduplicate.duplicatenumb','reportduplicate','patient.reaction','patient.drug'])

#there already was a a column in our dataset mentioning if the case was a duplicate, but i decided to ignore it in favor of folowing the instructions.
#<<<<<<< HEAD

print('DUPLICATED SUM:', df.duplicated().sum())
print('------------------------------------------------------')

df = df.drop_duplicates()

print("DF after duplicates dropped", df.duplicated().sum())   
#=======

print('DUPLICATED SUM:', df.duplicated().sum())
print('------------------------------------------------------')

df = df.drop_duplicates()

print("DF after duplicates dropped", df.duplicated().sum())   


# c) Identify and manage missing values

print('PART 2 - c) ============================================================================')

for col in df.columns:
    print(col, df[col].isnull().sum())
    
    ## we dicided to not use option a ; (drop rows with missing values), because our dataset contains reports about drug safety. dropping rows would mean deleting real events/information.
    ## We instead decided to use options b and c and fill in numerical missing values with mean/median and categorical missing values with strings.

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
    
    
# =============================================================================================================================================================================================           
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
    print('------------------------------------------------------') # used to sepperate each result from the loops

## used a loop beaucause of the many numerical columns. added titles for clarity in results. 

print('PART 3 - a) ============================================================================')

for col in categorical_cols:
   
   
    print("FREQUENCY:", df[col].value_counts())
    print("PROPORTIONS:", df[col].value_counts(normalize=True))
    print("MODE: Most frequent category", df[col].mode()[0])
    print("NUMBER OF UNIQUE CATEGORIES:", df[col].nunique())
    print('------------------------------------------------------')
   
   
#<<<<<<< HEAD
 # =============================================================================================================================================================================================       
#=======
    
# =============================================================================================================================================================================================       
# 4. UNIVARIATE GRAPHICAL EDA

df.loc[df['patient.patientonsetage'] > 100, 'patient.patientonsetage'] = df['patient.patientonsetage'].median()

## after running the original code i noticed that the generated graphs were very dispered and had big extremeties, so i printed : print(sorted(df['patient.patientonsetage'].dropna().unique())) and receive the following floats above 100.0:
# np.float64(219.0), np.float64(504.0), np.float64(618.0), np.float64(828.0), np.float64(849.0), np.float64(902.0), np.float64(937.0)]
# considering that they are unrealistic, i decided to replace any result above 100 with the median, and basically consider it unknown or errors in result imput.
# df. loc is a function i found in pandas that lets you select rows and/or assign new values using conditions.

num_cols_for_histogram = ['patient.patientonsetage', 'patient.patientweight'] #the rest of the numerical values in our dataset are binary (1/2) and when trying to plot them as histograms, the plots didn't tell us much.

df['patient.patientsex'] = df['patient.patientsex'].replace({1: 'Male',2: 'Female',})

df['serious'] = df['serious'].replace({1: 'Non-Serious',2: 'Serious'})

# because of the binary nature of the results in the columns for severity and patient sex, i replaced the 1 and 2 with what they each represent, this way, when looking at the plots, we will know.

for col in num_cols_for_histogram:
    
    # a) Custom number of bins
    sns.histplot(data=df, x=col, bins=20) # more bins so we can see the variations if any, more clearly
    plt.title(col + " : Histogram (20 bins)") #using col, "" would give me an error so I had to use col + ""
    plt.show()
    
    # b) Conditioning on other variables (by sex)
    sns.histplot(data=df, x=col, hue='patient.patientsex', bins=10)
    plt.title(col + " : Histogram by Sex")
    plt.show()
    
    # c) Stacked histogram
    sns.histplot(data=df, x=col, hue='patient.patientsex',
                 multiple="stack", bins=10)
    plt.title(col + " : Stacked Histogram by Sex")
    plt.show()
    
    # d) Dodge bars
    sns.histplot(data=df, x=col, hue='patient.patientsex', multiple="dodge", bins=10)
    plt.title(col + " : Dodge Histogram by Sex")
    plt.show()
    
    # e) Normalized histogram statistics
    sns.histplot(data=df, x=col, bins=10, stat="density")
    plt.title(col + " : Normalized Histogram statistics")
    plt.show()
    
    # f) Kernel density estimation (KDE) with chosen bandwidth
    sns.displot(data=df, x=col, hue='serious', kind='kde', bw_adjust=0.6 ) # 0.6 bandwith shows the trend clearly but still with some precision
    plt.title(col + " : KDE by severity (bw_adjust = 0.6)")
    plt.show()
    
    # g) Empirical cumulative distributions (ECDF)
    sns.displot(data=df,hue='serious', x=col, kind='ecdf')
    plt.title(col + " : ECDF by severity")
    plt.show()
    
   # Questions answered in the document *** 
    
 # ===========================   
#<<<<<<< HEAD
           
# 5. MULTIVARIATE NON-GRAPHICAL EDA

    # a, b)
    sex_report = pd.crosstab(df["patient.patientsex"], df["reporttype"], normalize="index")*100
    
    primarysource = pd.crosstab(df["primarysourcecountry"], df["primarysource.qualification"], normalize="index")*100
    
    sender_receiver = pd.crosstab(df["sender.sendertype"], df["receiver.receivertype"], normalize="index")*100

    # c) 
    sex_report_country = pd.crosstab([df["patient.patientsex"], df["reporttype"]], df["primarysourcecountry"], normalize="index")*100
    #this table shows how the combination of patient sex and report type varies across different countries






# 6. MULTIVARIATE GRAPHICAL EDA

# 6.1. Visualizing Statistical Relationships (5 plots):

    
    # a) A plot using Faceting feature (col parameter in the relplot() function)
    sns.relplot(data=df, x='patient.patientonsetage', y='patient.patientweight', hue='serious', col='patient.patientsex', kind='scatter')
    plt.suptitle("Age vs Weight by Sex and Seriousness", y=1.1)

    # b) A plot representing 5 variables at once (x, y, hue, size, col)
    sns.relplot(data=df, x='patient.patientonsetage', y='patient.patientweight', hue='serious', size='seriousnesshospitalization', col='patient.patientsex', kind='scatter')
    plt.suptitle("Age-Weight-Seriousness-Hospitalization by Sex", y=1.1)
    
    # c) A plot using line instead of points (find a variable that makes sense emphasizing continuity and explain why)
    sns.lineplot(data=df, x="patient.patientonsetage", y="patient.patientweight", errorbar=None)
    plt.xlabel("Patient Onset Age")
    plt.ylabel("Patient Weight")
    plt.title("Mean Patient Weight Across Age (Continuous Relationship)")
    #Weight and age are both continuous variables and the only two variables in the dataset that arent binary.
    #A line plot emphasizes how weight changes progressively with age
    
    # d) A plot illustrating standard deviation
    sns.pointplot(data=df, x='patient.patientsex', y='patient.patientweight', errorbar="sd")
    plt.xlabel("Patient Sex")
    plt.ylabel("Patient Weight")
    plt.title("Mean Weight by Sex with SD Error Bars", y=1.1)
    
    # e) A plot including a linear regression
    sns.lmplot(data=df, x='patient.patientonsetage', y='patient.patientweight', hue="serious")
    plt.title("Linear Regression: Age vs Weight by Seriousness", y=1.1)
    
    
# 6.2. Visualizing categorical data (10 plots):
    
    #ANSWERING:  Do reporting delays differ depending on the reporter’s professional role (e.g., physician, pharmacist, consumer)??
    
reduced_dataset = df.sample(1000)
# There were too many points to plot. A reduced amount of random results from the dataset had to be used.
# Similarly, the size of the points had to be modified and reduced for the same reason. This allowed a great number of results to remain shown on the plot.
    
    
    # a) 1 categorical scatter plot with jitter enabled
df["receivedate"] = pd.to_datetime(df["receivedate"])

sns.catplot(data=reduced_dataset, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5", "Unknown"], s=3)
plt.title("Scatter Plot: Reporter Qualification vs Time Report Received")

    # b) 1 categorical scatter plot with jitter disabled (explain your choice of variable for this one)
sns.catplot(data=reduced_dataset, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5", "Unknown"], jitter=False, s=3)
plt.title("Scatter Plot: Reporter Qualification vs Time Report Received, no jitter")

# Since primarysource.qualification is seperated into 6 categories, using a categorical scatter plot is the best way to visually understand which reporter's professional role took more time sending their reults. 
# Whith jitter=False, the data is organized in a single clustered line per primarysource.qualification category and, therefore, a trend can be more easily established.


    # c) 1 "beeswarm" plot representing 3 variables
sns.catplot(data=reduced_dataset, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5", "Unknown"], kind="swarm", s=3)
plt.title("Scatter Beeswarm Plot: Reporter Qualification vs Time Report Received")


    # d) 1 box plot representing 3 variables
sns.catplot(data=reduced_dataset, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5"], kind="box", s=1)
plt.title("Box Plot: Reporter Qualification vs Time Report Received")

    # e) 1 box plot showing the shape of the distribution (boxenplot())
sns.catplot(data=reduced_dataset.query("primarysource.qualification != unknown"), x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5"], kind="box", s=1)
plt.title("Box Plot showing distribution shape: Reporter Qualification vs Time Report Received")    


    # f) 1 split violin plot representing 3 variables with bandwidth adjusted for better visualization
sns.catplot(data=reduced_dataset, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5"], kind="violin", s=1, bw=0.5)
plt.title("Box Plot showing distribution shape: Reporter Qualification vs Time Report Received") 
    
    # g) 1 violin plot with scatter points inside the violin shapes
    
    
    # h) 1 bar plot representing 3 variables showing 97% confidence intervals
    
    
    # i) 1 point plot representing 3 variables showing 90% confidence intervals and lines in dashed style
    
    
    # j) 1 bar plot showing the number of observations in each category
    
    
    
# 6.3. Visualizing Bivariate Distributions (3 plots):
    
    # a) 1 "heatmap" plot representing 2 variables with colour intensity bar and adjusted bin width
    
    
    # b) 1 distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot())
    
    
    # c) 1 "heatmap" plot representing 3 variables, again of kind kde
