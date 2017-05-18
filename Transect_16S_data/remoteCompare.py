import time
import pandas as pd
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
import deepLearningTest
import paramSVR
from sklearn import preprocessing

py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')

# py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')

if __name__ == '__main__':
    funNum = 3  # the number of function for deep learning method 1:normal,2:more neurons 3: more layers
    typeTrainDB = 3  # 1: only OTUs 2: only easy_get para 3: OUT + easy_get
    start = time.time()
    # targetNormal = True  # the target is normalized or not

    isRegression = False
    isCheckPara = False
    targetNormal = isCheckPara
    if typeTrainDB == 1:
        figureTitle = "The reliability of SVR, Random Forest and NN. Use OTU only"
    elif typeTrainDB == 2:
        figureTitle = "The reliability of SVR, Random Forest and NN. Use Easy-get parameters only"
    elif typeTrainDB == 3:
        figureTitle = "The reliability of SVR, Random Forest and NN. Use both OTU and Easy parameters"
    targetList = ['salinity']
    # targetList = ['salinity', 'Depth', 'Temperature', 'O2', 'PO4', 'SiO2', 'NO2', 'NO3']

    iteraNum = 1  # the number of iteration
    dataFile = [600]  # the max percentage of zeors
    # dataFile = [990, 970, 950, 900, 850,800,750]
    # dataFile = [900, 850, 800, 750]
    # dataFile = [1000, 2000, 3000, 4000, 5000]
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    lableList = []  # the target's name
    finalErrorRF = []  # Random forest
    finalErrorSVR = []  # SVR
    finalErrorNN = []  # Deep learning

    # regression analysis for each parameters
    if isCheckPara:
        if isRegression:
            iteraNum = 1
            target = targetList[0]
            for fileName in dataFile:
                if typeTrainDB == 1:
                    trainData = pd.read_excel(
                        './Training Data/newWaterSamples_%d.xlsx' % fileName)
                elif typeTrainDB == 2:
                    trainData = pd.read_excel(
                        './Training Data/easy_get_para.xlsx')
                elif typeTrainDB == 3:
                    trainData = pd.read_excel(
                        './Training Data/OTUwithEasyPara_%d.xlsx' % fileName)  # Use easy parameters as training data
                normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3
                subCol = fillByKnn.loc[:, target]
                if targetNormal:
                    subCol = preprocessing.MinMaxScaler().fit_transform(subCol)
                # Comparing different algorithms
                # 1. SVR
                testSVR, predSVR = paramSVR.supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                print("This is svr : ", testSVR)
                print("SVR Part DONE!")
                # 2. RF
                testRF, predRF = paramSVR.randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                print("This is rf error: ", testRF)
                print("RF Part DONE!")

        else:
            # compare the accuracy between SVR, RF and DeepLearning based on the same data size
            for fileName in dataFile:  # for each data size, how the error for all para at the same time.
                if typeTrainDB == 1:
                    trainData = pd.read_excel(
                        './Training Data/newWaterSamples_%d.xlsx' % fileName)
                elif typeTrainDB == 2:
                    trainData = pd.read_excel(
                        './Training Data/easy_get_para.xlsx')
                elif typeTrainDB == 3:
                    trainData = pd.read_excel(
                        './Training Data/OTUwithEasyPara_%d.xlsx' % fileName)  # Use easy parameters as training data
                normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3
                for i in range(len(targetList)):
                    lableList += iteraNum * [str(targetList[i])]
                    errorRF = []
                    errorSVR = []
                    errorNN = []
                    errorELM = []
                    subCol = fillByKnn.loc[:, targetList[i]]

                    # Normalized target value
                    if targetNormal:
                        subCol = preprocessing.MinMaxScaler().fit_transform(subCol)
                    print("This is target variable: ", targetList[i])
                    print("This is normalized subCol: ", subCol)
                    # Comparing different algorithms
                    # 1. SVR
                    errorSVR = paramSVR.supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                    # errorSVR = supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                    print("This is svr error: ", errorSVR)
                    print("SVR Part %d DONE!" % (i + 1))
                    finalErrorSVR.extend(errorSVR)
                    # 2. RF
                    errorRF = paramSVR.randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                    # errorRF = randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                    print("This is rf error: ", errorRF)
                    print("RF Part %d DONE!" % (i + 1))
                    finalErrorRF.extend(errorRF)

                    # 3. DeepLearning
                    if not targetNormal:
                        y = subCol.values
                        # if not use normalized target variables
                        errorNN = deepLearningTest.deepLearning(normalized_trainData, y, iteraNum, funNum)
                    # Using normalized target variables
                    else:
                        errorNN = deepLearningTest.deepLearning(normalized_trainData, subCol, iteraNum, funNum)
                    print("This is Deep Learning error: ", errorNN)
                    print("DL Part %d DONE!" % (i + 1))
                    finalErrorNN.extend(errorNN)
                noneZero = str((1000 - fileName) / 10) + "%"
                title = "The RMSE of SVR/RF/DL based on the size of nonZero : %s" % noneZero
                print("This is categories: ", list(set(lableList)))

                if typeTrainDB == 2:
                    temp1 = list(set(lableList))
                    x_axis_name = [(temp1.index(p) + 1) for p in temp1]
                else:
                    x_axis_name = sorted(list(set(lableList)), reverse=True)
                writer1 = pd.ExcelWriter('./Training Data/remoteResultForPlot_DataSize_%d.xlsx' % fileName)
                pd.DataFrame(lableList).to_excel(writer1, 'sheet1')
                pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
                pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
                pd.DataFrame(finalErrorNN).to_excel(writer1, 'sheet4')
                pd.DataFrame(x_axis_name).to_excel(writer1, 'sheet5')
                pd.DataFrame(fileName).to_excel(writer1, 'sheet6')
                writer1.save()
        end = time.time()
        print("Time: %d seconds " % int((end - start)))
    else:
        for i in range(len(targetList)):  # for each parameter, it will draw a figure
            subCol = fillByKnn.loc[:, targetList[i]]
            if targetNormal:
                subCol = preprocessing.MinMaxScaler().fit_transform(subCol)
            # print("This is subCol: ", subCol)
            for fileName in dataFile:  # in each figure, the algorithms' error will be compared based on the different data size
                lableList += iteraNum * [str(fileName / 1000.0)]
                errorNN = []
                errorRF = []
                errorSVR = []
                if typeTrainDB == 1:
                    trainData = pd.read_excel(
                        './Training Data/newWaterSamples_%d.xlsx' % fileName)
                elif typeTrainDB == 2:
                    trainData = pd.read_excel(
                        './Training Data/easy_get_para.xlsx')
                elif typeTrainDB == 3:
                    trainData = pd.read_excel(
                        './Training Data/OTUwithEasyPara_%d.xlsx' % fileName)  # Use easy parameters as training data

                # Three options!!!! For preprocessing normalization
                # normalized_trainData = preprocessing.normalize(trainData) #1
                # normalized_trainData = preprocessing.scale(trainData) #2
                normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3

                # print("This is trainData:",trainData)
                errorSVR = paramSVR.supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                # errorSVR = supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                print("This is svr error: ", errorSVR)
                print("SVR Part %d DONE!" % (dataFile.index(fileName) + 1))
                finalErrorSVR.extend(errorSVR)

                errorRF = paramSVR.randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                # errorRF = randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                print("This is rf error: ", errorRF)
                print("RF Part %d DONE!" % (dataFile.index(fileName) + 1))
                finalErrorRF.extend(errorRF)

                if not targetNormal:
                    y = subCol.values
                    # if not use normalized target variables
                    errorNN = deepLearningTest.deepLearning(normalized_trainData, y, iteraNum, funNum)
                # Using normalized target variables
                else:
                    errorNN = deepLearningTest.deepLearning(normalized_trainData, subCol, iteraNum, funNum)
                print("This is Deep Learning error: ", errorNN)
                print("DL Part %d DONE!" % (i + 1))
                finalErrorNN.extend(errorNN)
            if typeTrainDB == 2:
                temp1 = list(set(lableList))
                x_axis_name = [(temp1.index(p) + 1) for p in temp1]
            else:
                x_axis_name = sorted(list(set(lableList)), reverse=True)

            writer1 = pd.ExcelWriter('./Training Data/remoteResultForPlot_%s.xlsx' % targetList[i])
            pd.DataFrame(lableList).to_excel(writer1, 'sheet1')
            pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
            pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
            pd.DataFrame(finalErrorNN).to_excel(writer1, 'sheet4')
            pd.DataFrame(x_axis_name).to_excel(writer1, 'sheet5')
            pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
            writer1.save()
