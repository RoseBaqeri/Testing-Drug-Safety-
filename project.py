import json
import pandas as pd
import seaborn as sns

data = json.load(open('drug-event-0012-of-0031.json'))
TDS = pd.DataFrame(data["results"])

print(TDS["sender"][0]["senderorganization"])
counter = 0

for i in TDS["sender"]:
    print(i[counter])
    counter += 1


#find a way to access senderorganization and create charts without the error code
#find a way fpor the computer to ignore all dictionarries that don't include "senderotgnization"
#sns.countplot(data=TDS, x=TDS["primarysourcecountry"].sample(20))