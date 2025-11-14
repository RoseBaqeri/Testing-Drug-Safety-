import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


    # ===================== Importing Dataset to program:=====================
data = json.load(open('drug-event-0012-of-0031.json'))
df = pd.json_normalize(data['results'])

df = df.drop(columns=['safetyreportversion','transmissiondateformat','receivedateformat','receiptdateformat','sender.senderorganization','receiver.receiverorganization','companynumb','authoritynumb','fulfillexpeditecriteria','primarysource.literaturereference','patient.summary.narrativeincludeclinical','duplicate','reportduplicate.duplicatesource',
    'reportduplicate.duplicatenumb','reportduplicate','patient.reaction','patient.drug'])







# 6.2. Visualizing categorical data (10 plots):
    
    #ANSWERING:  Do reporting delays differ depending on the reporter’s professional role (e.g., physician, pharmacist, consumer)??
    
    # a) 1 categorical scatter plot with jitter enabled
df["receivedate"] = pd.to_datetime(df["receivedate"])

sns.catplot(data = df, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5", "Unknown"], s=1)
    
    # b) 1 categorical scatter plot with jitter disabled (explain your choice of variable for this one)
sns.catplot(data = df, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5", "Unknown"], jitter=False, s=1)
    
# Since primarysource.qualification is seperated into 6 categories, using a categorical scatter plot is the best way to visually understand which reporter's professional role took more time sending their reults. 
# Whith jitter=False, the data is organized in a single clustered line per primarysource.qualification category and, therefore, a trend can be more easily established.


    # c) 1 "beeswarm" plot representing 3 variables
sns.catplot(data = df, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5", "Unknown"], kind="swarm", s=1, hue="serious")
    
    # d) 1 box plot representing 3 variables
Countries = df.groupby('occurountry')
['seious'].value_counts().unstack()
print(Countries)
# If the box plot does not represent the previous data chosen properly, then the amount of serious cases per country can be compared instead. 


sns.catplot(data = df, x = "primarysource.qualification", y = "receivedate", order=["1", "2", "3", "4", "5", "Unknown"], kind="box")
    
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