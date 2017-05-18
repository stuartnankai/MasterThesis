import csv

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pandas import ExcelWriter
from sklearn import datasets
from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier


data = pd.read_table('Data_all_2016_metadata.txt', delim_whitespace=True, index_col=0)
print("The size of metadata (water samples): ", len(data))
nullNum = list(data.isnull().sum())
ratioNull = dict()
parametersList = list(data)
# print(parametersList)
for i in range(len(parametersList)):
    ratioNull[parametersList[i]] = nullNum[i]
# print(ratioNull)
# with open('ratioNull.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in ratioNull.items():
#        writer.writerow([key, value])
tempData = pd.DataFrame(
    {'Number of Null': nullNum,
     'Param': parametersList,
     })
newData = data.iloc[:,:-4]
newData.__delitem__('Chla_Picoeuk.')
newData.__delitem__('NH4')
# newData.fillna(newData.mean(),inplace=True)
print(newData)
# sns.set(style="white")
# ax = sns.barplot(x="Param", y="Number of Null", data=tempData, order=parametersList)
# ax.set_xticklabels(labels=parametersList,rotation=90)
# fig = ax.get_figure()
# fig.savefig("NumberNull.png")
# plt.show()

writer = ExcelWriter('NumberNullWithNull.xlsx')
newData.to_excel(writer,'Sheet1')
writer.save()

