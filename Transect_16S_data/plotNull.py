import pandas as pd
import numpy as np
import plotly.plotly as py
import seaborn as sns
import matplotlib.pyplot as plt
from plotly.graph_objs import *

py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')

# file = pd.read_csv('./Training Data/Data_all_2016_metadata.txt',delim_whitespace=True)
# checkindex = pd.read_excel('./Training Data/watersamplelist.xlsx')
# indexList = checkindex.columns.tolist()
# # print("This is  : ", indexList)
# # print("This is file: ", file )
# # tempfile = file.ix[indexList]
# tempfile = file[file['Lib'].isin(indexList)]
# print("This is tempfile: ",tempfile)
# header = list(tempfile)
# header = header[1:]
# print("This is : ", header)
# df = tempfile.isnull().sum().tolist()
# df = df[1:]
# print("This is number of null: ", df )
# tempList = []
# for i in range(len(df)):
#     name = 'trace' + str(i+1)
#     print("This is name: ", name )
#     name = {
#         "x": [header[i]],
#         "y": [df[i]],
#         "opacity": 0.75,
#         # "text": [header[i]],
#         "type": "bar",
#         # "uid": "c31830",
#     }
#     tempList.append(name)
#
# data = Data(tempList)
# layout = {
#   # "title": "The situation of missing data existing in the metadata",
#   "xaxis": {"title": "Water parameters"},
#   "yaxis": {"title": "The number of missing value"}
# }
# fig = Figure(data=data, layout=layout)
# plot_url = py.plot(fig)
# xaxis = []
# yaxis = []
# xaxis = header
# tempData = pd.DataFrame(
#     {'Ratio': header,
#      'Total Num': df,
#      })
# print(tempData)
# sns.set(style="white")
# ax = sns.barplot(x="Ratio", y="Total Num", data=tempData,order=xaxis)
# ax.set(xlabel='Water parameters', ylabel='The number of missing value')
# for item in ax.get_xticklabels():
#     item.set_rotation(-60)
# fig = ax.get_figure()
# fig.savefig("Ratio of null.png")
# plt.show()
#

"""Plot zero for each coloumn in OTUs dataset"""

file = pd.read_csv('./Training Data/Data_all_2016_otus.txt', delim_whitespace=True)

df = file.drop('Taxonomy', 1)
print(df)
header = list(df)
checkindex = pd.read_excel('./Training Data/watersamplelist.xlsx')
indexList = checkindex.columns.tolist()
lengthList = len(indexList)

dropList = [i for i in header if i not in checkindex]
# print("This is droplist: ", dropList)
newdf = df.drop(dropList, axis=1)

countNum = (newdf == 0).astype(int).sum(axis=1)
rationNum = countNum / lengthList
print("This is countNum: ", rationNum.values)
# ratio = [1, 0.999, 0.995, 0.990, 0.985, 0.980, 0.975]
ratio = [0,0.005, 0.01, 0.02, 0.03, 0.05, 0.1, 0.2, 0.25]
otuSize = []
xaxis = []
yaxis = []
xaxis = ratio
for n in ratio:
    tempList = [j for j in rationNum.values if j <= (1.0-n)]
    yaxis.append(len(tempList))
tempData = pd.DataFrame(
    {'Ratio': xaxis,
     'Total Num': yaxis,
     })
print(tempData)
sns.set(style="white")
ax = sns.barplot(x="Ratio", y="Total Num", data=tempData,order=xaxis)
ax.set(xlabel='The proportion of non-zero for each OTU', ylabel='The size of OTUs dataset')
fig = ax.get_figure()
# fig.savefig("Ratio of zeros.png")
plt.show()





# header = list(tempfile)
# header = header[1:]
# print("This is : ", header)
# df = tempfile.isnull().sum().tolist()
# df = df[1:]
# print("This is number of null: ", df )
#
# tempList = []
# for i in range(len(ratio)):
#     name = 'trace' + str(i + 1)
#     print("This is name: ", name)
#     name = {
#         "x": [ratio[i]],
#         "y": [otuSize[i]],
#         # "opacity": 0.35,
#         # "text": [header[i]],
#         "type": "histogram",
#         # "uid": "c31830",
#     }
#     tempList.append(name)
#
#
# data = Data(tempList)
# # trace1 = {
# #     "x": ratio,
# #     "y": otuSize,
# #     "marker": {"color": ["#A6CEE3", "#1F78B4", "#B2DF8A", "#33A02C", "#FB9A99", "#E31A1C", "#FDE725", "#9FDA3A"]},
# #     "name": "data",
# #     "type": "histogram"
# # }
#
#
# # data = Data([trace1])
# layout = {
#     # "title": "The situation of missing data existing in the metadata",
#     "xaxis": {"title": "The proportion of non-zero for each OTU"},
#     "yaxis": {"title": "The size of OTUs dataset"}
# }
#
#
# fig = Figure(data=data, layout=layout)
# plot_url = py.plot(fig)
