
import pandas as pd

# pltl.tools.set_credentials_file(username='sunjiannankai', api_key='r8kdW8nbxiw5HJeCehBj')
# py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')

isTranspose = True
isRemovedNull = True
rationNum = 960
data = pd.read_table('Data_all_2016_otus.txt', delim_whitespace=True, index_col=0)
sampleSize = len(data.iloc[0, 1:])
otuList = data.index.values.tolist()
# print(sampleSize)
otuSize = len(data.iloc[:, 0])
ratioZero = dict()
temp = ((data == 0).astype(int).sum(axis=1)) / sampleSize
# print(temp)
for i in otuList:
    ratioZero[i] = temp[i]
print(ratioZero)
# print(len(ratioZero))
# print(((data == 0).astype(int).sum(axis=1))/sampleSize)
# with open('ratioZero.csv', 'w') as csv_file:
#     writer = csv.writer(csv_file)
#     for key, value in ratioZero.items():
#        writer.writerow([key, value])
# # xaxis = []
# # yaxis = []
# # ratio = [1, 0.999, 0.995, 0.990, 0.985, 0.980, 0.975]
# # xaxis = ratio
# # for i in ratio:
# #     tempList = [j for j in ratioZero.values() if j <= i]
# #     yaxis.append(len(tempList))
# # tempData = pd.DataFrame(
# #     {'Ratio': xaxis,
# #      'Total Num': yaxis,
# #      })
# # print(tempData)
# # sns.set(style="white")
# # ax = sns.barplot(x="Ratio", y="Total Num", data=tempData,order=xaxis)
# # fig = ax.get_figure()
# # fig.savefig("Ratio of zeros.png")
# # plt.show()
#
# # Remove the Otu if non-zero part is smaller than the threshold

writer = pd.ExcelWriter('./Training Data/OTUremove_by_ratio_%d.xlsx' % rationNum)
data_drop = data.copy()
for i in ratioZero.keys():
    if ratioZero[i] > rationNum/1000.0:  # threshold
        data_drop.drop(i, inplace=True)
data_drop.to_excel(writer, 'sheet1')
writer.save()
# Transpose
if isTranspose:
    df1 = pd.read_excel('./Training Data/OTUremove_by_ratio_%d.xlsx' % rationNum)
    df1 = df1.drop(df1.columns[1], axis=1)  # drop the class column
    df1 = df1.set_index('ID').T  # transpose the row and column
        # print(df)
    writer1 = pd.ExcelWriter('./Training Data/OTU_Transpose_by_ratio_%d.xlsx' % rationNum)
    df1.to_excel(writer1, 'sheet1')
    writer1.save()

df2 = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
df2 = df2.set_index('Lib')
indexList2 = df2.index.tolist()
df3 = pd.read_excel('./Training Data/NumberNullWithNull.xlsx')
df3 = df3.set_index('Lib')
indexList3 = df3.index.tolist()
checkList = [i for i in indexList3 if i not in indexList2]
print("This is : ", checkList)
# Remove Null from parameter DB
if isRemovedNull:
    df4 = pd.read_excel('./Training Data/OTU_Transpose_by_ratio_%d.xlsx' % rationNum)
    for i in checkList:
        df4 = df4.drop([i])
    writer2 = pd.ExcelWriter('./Training Data/newWaterSamples_%d.xlsx' % rationNum)
    df4.to_excel(writer2, 'sheet1')
    writer2.save()
    print (df4)



