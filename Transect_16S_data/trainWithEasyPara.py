import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns


fileList = [960]
paraData = pd.read_excel("./Training Data/NumberNullWithNull.xlsx")
for fileName in fileList:
    otuData = pd.read_excel('./Training Data/newWaterSamples_%d.xlsx' % fileName)
    new_paraData = paraData.drop('Synechococcus',axis = 1)
    new_paraData = new_paraData.drop('Tbact',axis = 1)
    new_paraData = new_paraData.dropna()
    new_paraData = new_paraData.set_index('Lib')
    paraList = ['Depth', 'Temperature','Latitude','Longitude' ]
    for i in paraList:
        otuData[i] = new_paraData[i]
    print("This is OTU: " , otuData )
    writer = pd.ExcelWriter('./Training Data/OTUwithEasyPara_%d.xlsx' % fileName)
    otuData.to_excel(writer, 'sheet1')
    writer.save()