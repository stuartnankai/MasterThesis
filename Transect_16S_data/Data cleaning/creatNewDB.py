import matplotlib.pyplot as plt
import plotly.plotly as py
import plotly as pltl
from plotly.graph_objs import *
import csv
import pandas as pd

df = pd.read_excel('../Training Data/NumberNullWithNull.xlsx')
zeroNum = 0  # percentage of non zero - Upper limit
sizeNum = (1 - zeroNum) * 1000
trainData = pd.read_excel(
    '../Training Data/OTU_Transpose_by_ratio_%d.xlsx' % sizeNum)
df = df.iloc[:, :9]
print("This is df: ", df)
df_new = df.dropna()
fullWaterSample = df.loc[:, 'Lib'].tolist()
newWaterSample = df_new.loc[:, 'Lib'].tolist()
print("sampel:", fullWaterSample)
print("This is : ", newWaterSample)
deleteList = [i for i in fullWaterSample if i not in newWaterSample]

# print("This is : ", deleteList)

newdata= trainData.drop(deleteList)
writer = pd.ExcelWriter('../Training Data/newWaterSamples_%d.xlsx' %sizeNum)
newdata.to_excel(writer, 'sheet1')
writer.save()
