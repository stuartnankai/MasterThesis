import pandas as pd
import os.path

df = pd.read_excel('../Training Data/mergeOTU_split_unclassified_removed.xlsx')
dflist = pd.read_excel('../Training Data/watersamplelist.xlsx')

print("This is : ", df.shape)

levelList = [2, 3, 4, 5, 6]
# targetLevel = 3
sampleList = dflist.columns.tolist()

# print("This is sample list: ", sampleList )

"Generating file"
isdelete = True  # delete the otu if smaller than minNum
# isdelete = False
iscombine = True
# for splitLevel in levelList:
#
#     gg = df.groupby("taxnonmy%d" % splitLevel).sum()
#     print("This is : ", gg.shape)
#
#     writer = pd.ExcelWriter('../Training Data/OTUmergedByLevel%d.xlsx' %splitLevel)
#
#     gg.to_excel(writer, 'sheet1')
#
#     writer.save()
#
for level in levelList:


    # isdelete = False
    minNum = 10  #
    waterSample = list(df.columns.values)
    waterSample = waterSample[7:]
    waterSample.insert(0, 'class')
    # print("This is water: ", waterSample )
    targetName = 'taxnonmy' + str(level)
    preLevel = 'taxnonmy' + str(level - 1)
    aftLevel = 'taxnonmy' + str(level + 1)
    nameList = df[targetName].values.tolist()
    # print("This is namelist length: ", len(nameList) )
    indexset = list(set(nameList))
    # print("This is indexset: ", indexset )
    # indexset.remove('unclassified')
    prenameList = df[preLevel].values.tolist()
    index = []
    checkList = ['unclassified', 'uncultured']
    for j in range(len(indexset)):
        index.append(j)
    newDf = pd.DataFrame()

    tempPostion = []
    unclassPosition = []
    for item in indexset:
        if item not in checkList:
            for i in range(len(nameList) - 1):
                if nameList[i] == item:
                    tempPostion.append(i)
                    if i + 1 == len(nameList) - 1:
                        tempPostion.append(i + 1)
                        tempFile = df.iloc[tempPostion]
                        tempGroup = tempFile.groupby(targetName).sum()
                        tempGroup['class'] = item
                        cols = tempGroup.columns.tolist()
                        cols = cols[-1:] + cols[:-1]
                        indexdf = tempGroup[cols]
                        # indexdf.name = indexset.index(item)
                        tempDF = pd.DataFrame(indexdf.values, columns=waterSample)
                        # tempDF.name = item
                        newDf = pd.concat([newDf, tempDF])
                        tempPostion = []
                    elif nameList[i + 1] != item:
                        tempFile = df.iloc[tempPostion]
                        tempGroup = tempFile.groupby(targetName).sum()
                        tempGroup['class'] = item
                        cols = tempGroup.columns.tolist()
                        cols = cols[-1:] + cols[:-1]
                        indexdf = tempGroup[cols]
                        # indexdf.name = indexset.index(item)
                        tempDF = pd.DataFrame(indexdf.values, columns=waterSample)
                        # tempDF.name = item
                        newDf = pd.concat([newDf, tempDF])
                        tempPostion = []
        else:  # item is unclassified
            if prenameList[
                i] not in checkList:  # if prename is still unclassified, skip it. Otherwise, use the pre-name
                unclassPosition.append(i)
                if i + 1 == len(nameList) - 1:
                    unclassPosition.append(i + 1)
                    tempFile = df.iloc[unclassPosition]
                    tempGroup = tempFile.groupby(preLevel).sum()
                    tempGroup['class'] = prenameList[i]
                    cols = tempGroup.columns.tolist()
                    cols = cols[-1:] + cols[:-1]
                    indexdf = tempGroup[cols]
                    # indexdf.name = indexset.index(item)
                    tempDF = pd.DataFrame(indexdf.values, columns=waterSample)
                    # tempDF.name = item
                    newDf = pd.concat([newDf, tempDF])
                    tempPostion = []
                elif nameList[i + 1] != 'unclassified':
                    if prenameList[i] not in checkList:
                        tempFile = df.iloc[unclassPosition]
                        tempGroup = tempFile.groupby(preLevel).sum()
                        tempGroup['class'] = prenameList[i]
                        cols = tempGroup.columns.tolist()
                        cols = cols[-1:] + cols[:-1]
                        indexdf = tempGroup[cols]
                        # indexdf.name = indexset.index(item)
                        tempDF = pd.DataFrame(indexdf.values, columns=waterSample)
                        # tempDF.name = item
                        newDf = pd.concat([newDf, tempDF])
                        tempPostion = []

    newDf = (newDf.groupby(['class']).sum()).T
    newDf.drop([x for x in newDf.index.tolist() if x not in sampleList], inplace=True)

    if isdelete:
        threshold = minNum
        newDf.drop([col for col, val in newDf.sum().iteritems() if val < threshold], axis=1, inplace=True)
    else:
        minNum = 0

    if iscombine:
        easyPara = pd.read_excel('../Training Data/easy_get_para.xlsx')
        # combineDF = pd.merge(newDf,easyPara,how='outer')
        combineDF = pd.concat([newDf, easyPara], axis=1)
        print("This is combineDF: ", combineDF)
        if not os.path.exists(
                        '../Training Data/OTUmergedByLevel%d_transpose_isdeleted_%s_threshold_%d_with_Easy_Get.xlsx' % (
                        level, str(isdelete), minNum)):
            writer = pd.ExcelWriter(
                '../Training Data/OTUmergedByLevel%d_transpose_isdeleted_%s_threshold_%d_with_Easy_Get.xlsx' % (
                    level, str(isdelete), minNum))
            combineDF.to_excel(writer, 'sheet1')
            writer.save()
        print("Subclass %d is done!!!!" %level )
    else:
        print("This is newdf: ", newDf.head)
        print("This is : ", newDf.shape)
        if not os.path.exists('../Training Data/OTUmergedByLevel%d_transpose_isdeleted_%s_threshold_%d.xlsx' % (
        level, str(isdelete), minNum)):
            writer = pd.ExcelWriter('../Training Data/OTUmergedByLevel%d_transpose_isdeleted_%s_threshold_%d.xlsx' % (
            level, str(isdelete), minNum))
            newDf.to_excel(writer, 'sheet1')
            writer.save()
        print("Subclass %d is done!!!!" % level)


    # # print("This is target level: ", df[targetName].values.tolist())
    # # print("This is previous level: ", df[preLevel] )
    # tempPos = []
    # unclassPos= []
    # startPoint = 0
    # notSaved = True
    # newDF = pd.DataFrame(columns=waterSample,index=indexset)
    # # newDF.drop('unclassified', inplace=True)
    # tempName = ''
    #
    # for i in range(len(df)):
    #     if nameList[i] != 'unclassified':
    #         tempName = nameList[i]
    #         print("This is temp Name: ", tempName)
    #         tempPos.append(i)
    #         if i < len(df)-1:
    #             if nameList[i + 1] != tempName:
    #                 tempdf = df.iloc[tempPos]
    #                 print("This is temp df: ", tempdf)
    #                 tempGroup = tempdf.groupby(targetName).sum()
    #                 # tempGroup['class'] = tempName
    #                 cols = tempGroup.columns.tolist()
    #                 # cols = cols[-1:] + cols[:-1]
    #                 indexdf = tempGroup[cols]
    #                 print("This is temp group : ", indexdf)
    #                 # indexeddf = tempGroup.set_index(['1'])
    #                 # newDF = pd.concat([newDF, indexdf],ignore_index=True)
    #                 # newDF.append(indexdf,ignore_index=True)
    #                 newDF.loc[tempName]= indexdf.values
    #                 tempPos = []
    #                 tempName = ''
    #         else:
    #             tempdf = df.iloc[tempPos]
    #             print("This is temp df: ", tempdf)
    #             tempGroup = tempdf.groupby(targetName).sum()
    #             # tempGroup['class'] = tempName
    #             cols = tempGroup.columns.tolist()
    #             # cols = cols[-1:] + cols[:-1]
    #             indexdf = tempGroup[cols]
    #             print("This is temp group : ", indexdf)
    #             # indexeddf = tempGroup.set_index(['1'])
    #             # newDF = pd.concat([newDF, indexdf],ignore_index=True)
    #             # newDF.append(indexdf,ignore_index=True)
    #             newDF.loc[tempName] = indexdf.values
    #             tempPos = []
    #             tempName = ''
    #             tempdf = None
    #     elif prenameList[i] not in indexset:
    #         # tempdf = None
    #         unclassPos.append(i)
    #         checkitem = nameList[i]
    #         print("This is !!!!!!!!!!!!!!!!!: ", checkitem)
    #         if i< len(df)-1:
    #             if nameList[i+1] != 'unclassified':
    #                 tempdf_unclass = df.iloc[unclassPos]
    #                 # tempdf_unclass = df.iloc[unclassPos[0]:unclassPos[-1],:]
    #                 print("This is temp unclass: ", tempdf_unclass )
    #                 newIndex = prenameList[i]
    #                 # newDF.drop('unclassified', inplace=True)
    #                 indexset.append(newIndex)
    #                 # indexset.remove('unclassified')
    #                 newDF = newDF.reindex(indexset)
    #                 print("This is temp df: ", tempdf_unclass)
    #                 tempGroup = tempdf_unclass.groupby(preLevel).sum()
    #                 # tempGroup['class'] = tempName
    #                 cols = tempGroup.columns.tolist()
    #                 # cols = cols[-1:] + cols[:-1]
    #                 indexdf = tempGroup[cols]
    #                 print("This is temp group : ", indexdf)
    #                 # indexeddf = tempGroup.set_index(['1'])
    #                 # newDF = pd.concat([newDF, indexdf],ignore_index=True)
    #                 # newDF.append(indexdf,ignore_index=True)
    #
    #                 newDF.loc[newIndex] = indexdf.values
    #                 # newDF.append(indexdf,index)
    #                 unclassPos = []
    #                 tempName = ''
    #         else:
    #             tempdf_unclass = df.iloc[unclassPos]
    #             # tempdf_unclass = df.iloc[unclassPos[0]:unclassPos[-1],:]
    #             print("This is temp unclass: ", tempdf_unclass)
    #             newIndex = prenameList[i]
    #             # newDF.drop('unclassified', inplace=True)
    #             indexset.append(newIndex)
    #             # indexset.remove('unclassified')
    #             newDF = newDF.reindex(indexset)
    #             print("This is temp df: ", tempdf_unclass)
    #             tempGroup = tempdf_unclass.groupby(preLevel).sum()
    #             # tempGroup['class'] = tempName
    #             cols = tempGroup.columns.tolist()
    #             # cols = cols[-1:] + cols[:-1]
    #             indexdf = tempGroup[cols]
    #             print("This is temp group : ", indexdf)
    #             # indexeddf = tempGroup.set_index(['1'])
    #             # newDF = pd.concat([newDF, indexdf],ignore_index=True)
    #             # newDF.append(indexdf,ignore_index=True)
    #
    #             newDF.loc[newIndex] = indexdf.values
    #             # newDF.append(indexdf,index)
    #             unclassPos = []
    #             tempName = ''
    #

    # finalData = newDF
    # elif prenameList[i] != 'unclassified':
    #     tempName = prenameList[i]
    #     tempPos.append(i)
    #     if prenameList[i + 1] != tempName:
    #         tempdf = df.iloc[tempPos]
    #         tempGroup = tempdf.groupby(preLevel).sum()
    #         # tempGroup.set_index([prenameList[i]])
    #         newDF = pd.concat([newDF, tempGroup])
    #         tempPos = []

# for i in range(len(df) - 1):
#     if nameList[i] != 'unclassified':
#         if notSaved:
#             tempName = nameList[i]
#             tempdf = df.iloc[startPoint:i,:]
#             # newDF.append(tempdf,ignore_index=True)
#             newDF = pd.concat([newDF,tempdf])
#             print("This is temp df: ", newDF)
#             notSaved = False
#         tempPos.append(i)
#         if nameList[i + 1] != 'unclassified':  # find the last one.
#             startPoint = i+1
#             notSaved = True
#             temp11 = df.iloc[tempPos]
#             print("This is 11: ", temp11)
#             temp1 = temp11.groupby(preLevel).sum()
#             newDF= pd.concat([newDF,temp1])
#             print("This is temp1: ", temp1 )
#             # # df = df[df[targetName] != 'unclassified']
#             # print("This is tempPos: ", tempPos)
#             # df.drop(df.index[tempPos], inplace=True)
#             # print("This is shape of df: ", df.shape)
#             # df.append(temp1)
#             tempPos = []
#
