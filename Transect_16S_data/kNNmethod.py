import plotly.plotly as py
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
import xlwt

df = pd.read_excel('NumberNullWithNull.xlsx')
df2 = pd.DataFrame()
df_origin = df.copy()
# dfWithNull = df.iloc[:, 1:8]
# print(dfWithNull)
# tempdf = dfWithNull.iloc[:, 0:3]
# numpyMatrix = tempdf.as_matrix()
# numpyMatrix = np.delete(numpyMatrix,(87),axis=0)
# print(numpyMatrix)
# # Train NN
# neigh = NearestNeighbors(n_neighbors=1)
# neight_matrix = neigh.fit(numpyMatrix)
# # Find the nearest neighbor of [6.9525, 250, 4.1997]
# findNN = neight_matrix.kneighbors([[6.9525, 250, 4.1997]])
# print(findNN)
testList = [6.9525, 250, 4.1997, 60.2, 19.1]
### Parameters which have full data ['salinity', 'Depth', 'Temperature','Latitude', 'Longitude']
paramList = ['salinity', 'Depth', 'Temperature', 'Latitude', 'Longitude']
paramMiss = ['O2', 'PO4', 'SiO2', 'NO2', 'NO3', 'Tbact', 'Synechococcus']
for index, row in df.iterrows():
    if (df.loc[index].isnull().any()):
        df2 = df2.append(row, ignore_index=False)
        df.drop(index, inplace=True)
# print(df2)
df2_TopFive = np.array(df2[paramList])  # With NUll
df_TopFive = np.array(df[paramList])  # No Null
# print(df_TopFive)
# Train 1-NN
neigh = NearestNeighbors(n_neighbors=1)
neigh_matrix = neigh.fit(df_TopFive)
# Find the nearest neighbor for df2.TF
# for i in range(len(df2_TopFive)):
#     tryList = df2_TopFive[i].tolist()  # The sample missing data
#     findNN = neigh_matrix.kneighbors(tryList, return_distance=False)
#     checkList = df_TopFive[findNN].tolist()  # the nearest neighbor[x,x,x,x,x] for trylist
#     checkList = checkList[0][0]
#     for index, row in df.iterrows():
#         if all(row[j] in checkList for j in paramList):
#             for p in paramMiss:
#                 if not df.at[index,p]:
#                     print("XXXX",df.loc[index])
# findNN = neigh_matrix.kneighbors([[6.9525, 250, 4.1997, 60.2, 19.1]], return_distance=False)
# print(findNN)
# checkList = df_TopFive[findNN].tolist()
# checkList = checkList[0][0]
# print(checkList)
for i in range(len(df2_TopFive)):
    tryList = df2_TopFive[i].tolist()
    findNN = neigh_matrix.kneighbors(tryList, return_distance=False)
    checkList = df_TopFive[findNN].tolist()
    checkList = checkList[0][0]
    print(checkList)
    for index, row in df_origin.iterrows():
        if all(row[j] in checkList for j in paramList):  # 找到对应的完整数据 1-NN
            print("The nearest neighbor is:",df.loc[index])
            for index1, row1 in df_origin.iterrows():
                if all(row1[n] in tryList for n in paramList):  # 找到对应的缺失数据
                    # print(df_origin.loc[index1])
                    for p in paramMiss:
                        # print(df_origin.at[index1, p])
                        if np.isnan(df_origin.at[index1, p]):  # check if it nan or not
                            df_origin.at[index1, p] = df_origin.at[index, p]  # copy the value
                    # print("After copy the value from NN: ",df_origin.loc[index1])
print(type(df_origin))
writer = pd.ExcelWriter('FillByKnn.xlsx')
df_origin.to_excel(writer,'Sheet1')
writer.save()