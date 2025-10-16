import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = json.load(open('drug-event-0012-of-0031.json'))
TDS = pd.DataFrame(data["results"])

print(TDS["sender"][0]["senderorganization"])
counter = 0

#to convert data in "sender" into indices/an index
for idx, sender in enumerate(TDS["sender"]):
    print(f"{idx}: {sender['senderorganization']}")

#irrelevant...only prints names in console
for i in TDS["sender"]:
    print(i["senderorganization"])
    counter += 1

#out of 1199 data samples, the graphs will be more readable with a much smaller amount of samples taken randomly
random_sample = TDS.sample(50)


#The following code is a prototype and does not work yet...
#printing a histograph showing the tendecy of how long the trial took to show serious conditions according to the different companies
sns.histplot(data=random_sample, x="receivedate", y="serious", palette="Set1")
plt.show()



#find a way to access senderorganization and create charts without the error 
#FIX= changed print(i[counter]) to print(i["senderorganization]) since counter cannot be used on a dictionnary
#find a way fpor the computer to ignore all dictionarries that don't include "senderotgnization"
#sns.countplot(data=TDS, x=TDS["primarysourcecountry"].sample(20))