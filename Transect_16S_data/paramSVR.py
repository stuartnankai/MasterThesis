import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.svm import SVR
from sklearn.decomposition import KernelPCA
from sklearn.ensemble import RandomForestRegressor
from sklearn import datasets, linear_model
from sklearn.model_selection import GridSearchCV
from sklearn import preprocessing, decomposition
from sklearn.model_selection import train_test_split
import plotly.plotly as py
from plotly.graph_objs import *
import reduceDim
import pymrmr


# py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')


def plotFigure(y_pred, y_test):
    plt.figure()
    plt.plot(range(len(y_pred)), y_pred, 'b', label="predict")
    plt.plot(range(len(y_pred)), y_test, 'r', label="test")
    plt.legend(loc="upper right")
    plt.xlabel("the number of samples")
    plt.ylabel('value of RMSE')
    plt.show()


def featureExtraction(trainData, testData, numFeature, isKernel, kernelFunc):
    print("PCA is running....")
    if isKernel:
        print("This is Kernel PCA: ", kernelFunc)
        "kernel : linear | poly | rbf | sigmoid | cosine | precomputed"
        pca = KernelPCA(n_components=numFeature, kernel=kernelFunc, fit_inverse_transform=True, gamma=0.001)

    else:
        pca = decomposition.PCA(n_components=numFeature)
        print("This is the ratio of features", sum(pca.explained_variance_ratio_))
    X_train_pca = pca.fit_transform(trainData)
    X_test_pca = pca.transform(testData)

    print("PCA DONE!!!!!!")
    return X_train_pca, X_test_pca


def supportVectorM(data, target, iterNum, isNormal, isRegression, isPCA, n_components, normalMethod, testSize,
                   isKernel, kernelFunc):
    y = target
    svrList = []
    # print("This is data: ", data)
    # print("This is target : ", target)
    if normalMethod == 1:
        sc = preprocessing.Normalizer()
    elif normalMethod == 2:
        sc = preprocessing.StandardScaler()
    elif normalMethod == 3:
        sc = preprocessing.MinMaxScaler()
    for j in range(iterNum):
        X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=testSize)

        # sc.fit(X_train)
        X_train_std = sc.fit_transform(X_train)
        X_test_std = sc.transform(X_test)
        if isPCA:
            # X_train, X_test = featureExtraction(X_train_std, X_test_std, n_components, isKernel, kernelFunc)
            X_train, X_test = reduceDim.featureExtraction(X_train_std, X_test_std, n_components)
            # print("This is the size of input by using PCA: ", len(X_train[0]))
        else:
            print("Not use PCA...", )

            X_train = X_train_std
            X_test = X_test_std
            # print("This is the size of input: ", len(X_train[0]))

        C_range = np.logspace(-1, 4, num=12)
        gamma_range = np.logspace(-4, 4, num=12)  # best 0.1/1
        svr_rbf = GridSearchCV(SVR(kernel='rbf'), cv=5,
                               param_grid={"C": C_range,
                                           "gamma": gamma_range}, n_jobs=1)
        svr_rbf.fit(X_train, y_train)
        print("The best parameters are %s with a score of %0.2f"
              % (svr_rbf.best_params_, svr_rbf.best_score_))
        # svr_rbf = SVR(kernel='rbf', C=1000.0, gamma='auto', max_iter=-1, epsilon=0.1)
        # svr_poly = SVR(kernel='poly', C=1000, degree=3)
        y_pred_temp = svr_rbf.predict(X_test)
        # print("This is temp y_pred: ", y_pred_temp )
        y_pred = []
        for t in y_pred_temp:
            if t < 0:
                y_pred.append(0)
            else:
                y_pred.append(t)
        # y_pred = svr_poly.fit(X_train, y_train).predict(X_test)
        if isRegression:
            return y_pred,y_test
        else:
            sum_mean = 0
            for i in range(len(y_pred)):
                if isNormal:
                    print("This is REAL value %.4f, ======SVR=====> PRED value: %.4f" % (y_test[i], y_pred[i]))
                    # sum_mean += (y_pred[i] - y_test[i]) ** 2  # if the target is np array

                    sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test[i]) ** 2
                else:
                    print("This is REAL value %.4f, ======SVR=====> PRED value: %.4f" % (y_test.values[i], y_pred[i]))
                    # sum_mean += (y_pred[i] - y_test.values[i]) ** 2

                    sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test.values[i]) ** 2
            sum_erro = np.sqrt(sum_mean / len(y_pred))
            svrList.append(sum_erro)
            print("This is RMSE for SVR: ", sum_erro)
            print("This is iteration num: ", j + 1)
    return svrList


def randomForest(data, target, iterNum, isNormal, isRegression, isPCA, n_components, normalMethod, testSize, isKernel,
                 kernelFunc):
    y = target
    rfList = []
    if normalMethod == 1:
        sc = preprocessing.Normalizer()
    elif normalMethod == 2:
        sc = preprocessing.StandardScaler()
    elif normalMethod == 3:
        sc = preprocessing.MinMaxScaler()
    for j in range(iterNum):
        X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=testSize)

        if normalMethod != 4:  # random forest do not need to normalization
            sc.fit(X_train)
            X_train_std = sc.transform(X_train)
            X_test_std = sc.transform(X_test)
        else:
            X_train_std = X_train
            X_test_std = X_test

        if isPCA:
            # X_train, X_test = featureExtraction(X_train_std, X_test_std, n_components, isKernel, kernelFunc)
            X_train, X_test = reduceDim.featureExtraction(X_train_std, X_test_std, n_components)
        else:
            X_train = X_train_std
            X_test = X_test_std

        # param_test1 = {'n_estimators': range(10, 201, 10), 'max_depth': range(4, 15, 1)}
        param_test1 = {'n_estimators': range(10, 201, 10)}
        regr_rf = GridSearchCV(estimator=RandomForestRegressor(),
                               param_grid=param_test1, cv=5, n_jobs=1)
        # regr_rf = RandomForestRegressor(n_estimators=numTree, max_depth=max_depth,oob_score=True)
        regr_rf.fit(X_train, y_train)
        print("The best parameters are %s with a score of %0.2f"
              % (regr_rf.best_params_, regr_rf.best_score_))
        # Predict on new data
        y_pred = regr_rf.predict(X_test)
        if isRegression:
            return y_pred,y_test
        else:
            sum_mean = 0
            for i in range(len(y_pred)):
                if isNormal:
                    print(
                        "This is REAL value %.4f, ======Random Forest=====> PRED value: %.4f" % (y_test[i], y_pred[i]))
                    # sum_mean += (y_pred[i] - y_test[i]) ** 2  # if the target is np array
                    sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test[i]) ** 2
                else:
                    print("This is REAL value %.4f, ======Random Forest=====> PRED value: %.4f" % (
                        y_test.values[i], y_pred[i]))
                    # sum_mean += (y_pred[i] - y_test.values[i]) ** 2
                    sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test.values[i]) ** 2
            sum_erro = np.sqrt(sum_mean / len(y_pred))
            rfList.append(sum_erro)
            print("This is RMSE for RF: ", sum_erro)
            print("This is iteration num: ", j + 1)
    return rfList


def linerRegression(data, target, iterNum, isNormal, isRegression, isPCA, n_components, normalMethod, testSize):
    y = target
    linearList = []
    if normalMethod == 1:
        sc = preprocessing.Normalizer()
    elif normalMethod == 2:
        sc = preprocessing.StandardScaler()
    elif normalMethod == 3:
        sc = preprocessing.MinMaxScaler()
    for j in range(iterNum):
        X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=testSize)

        sc.fit(X_train)
        X_train_std = sc.transform(X_train)
        X_test_std = sc.transform(X_test)
        if isPCA:
            X_train, X_test = featureExtraction(X_train_std, X_test_std, n_components)
            # print("This is the size of input by using PCA: ", len(X_train[0]))
        else:
            print("Not use PCA...", )

            X_train = X_train_std
            X_test = X_test_std
            # print("This is the size of input: ", len(X_train[0]))
        regr = linear_model.LinearRegression()
        regr.fit(X_train, y_train)
        y_pred_temp = regr.predict(X_test)
        y_pred = []
        for t in y_pred_temp:
            if t < 0:
                y_pred.append(0)
            else:
                y_pred.append(t)
        # y_pred = svr_poly.fit(X_train, y_train).predict(X_test)
        if isRegression:
            return y_pred
        else:
            sum_mean = 0
            for i in range(len(y_pred)):
                if isNormal:
                    print("This is REAL value %.4f, ======SVR=====> PRED value: %.4f" % (y_test[i], y_pred[i]))
                    # sum_mean += (y_pred[i] - y_test[i]) ** 2  # if the target is np array

                    sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test[i]) ** 2
                else:
                    print("This is REAL value %.4f, ======SVR=====> PRED value: %.4f" % (y_test.values[i], y_pred[i]))
                    # sum_mean += (y_pred[i] - y_test.values[i]) ** 2

                    sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test.values[i]) ** 2
            sum_erro = np.sqrt(sum_mean / len(y_pred))
            linearList.append(sum_erro)
            print("This is RMSE for SVR: ", sum_erro)
            print("This is iteration num: ", j + 1)
            # plotFigure(y_pred,y_test)
    return linearList


def comparePCA(lableList, finalErrorSVR, finalErrorRF, x_axis_name, figureTitle):
    trace1 = {
        "x": lableList,
        "y": finalErrorSVR,
        "line": {"color": "rgba(102,194,165,1)"},
        "name": "SVR",
        "type": "box",
        "xaxis": "x",
        "yaxis": "y"
    }
    trace2 = {
        "x": lableList,
        "y": finalErrorRF,
        "line": {"color": "rgba(141,160,203,1)"},
        "name": "Random Forest",
        "type": "box",
        "xaxis": "x",
        "yaxis": "y"
    }
    data = Data([trace1, trace2])
    layout = {
        "boxmode": "group",
        "margin": {
            "r": 10,
            "t": 25,
            "b": 40,
            "l": 60
        },
        "title": figureTitle,
        "xaxis": {
            "categoryarray": x_axis_name,
            "categoryorder": "array",
            "domain": [0, 1],
            # "title": targetList[i],
            "type": "category"
        },
        "yaxis": {
            "domain": [0, 1],
            "title": "RMSE-Root mean square error"
        }
    }
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)


if __name__ == '__main__':

    # dataFile = [950, 850, 750]
    dataFile = [950]
    iteraNum = 100
    targetList = ['NO3']
    # targetList = ['Temperature']
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    typeTrainDB = 7  # 1. only OTU 2. only easy-get 3. use both otu and easy get parameters, 5. use merged OTU 6. use merged OTU and easy get,7. Use MRMR feature selection
    hasSalinity = True
    # hasSalinity = False
    isRegression = False
    isCheckPara = False
    targetNormal = False
    # isRemote = True
    needNormalized = False
    isCompareMRMR = True
    isRemote = False
    isPCA = True
    "Main parameters which need to be changed"
    # isPCA = False
    # isMLE = True  # automatic pick the features
    isMLE = False
    isComparePCA = False
    isCompareNormalization = False
    isKernel = True
    # kernelFunc= 'rbf'
    kernelFunc = 'rbf'
    testSizeList = [0.1]
    normalMethod = 2  # 1, normalization, 2, scale, 3, minmaxscale
    componentsNum = 6
    targetLevel = 2
    # isdelete = False
    isdelete = True  # smaller otu is removed based on the threshold(minNum)
    # isdelete = False
    minNum = 1000  # the sum of otu should be bigger than minNum
    if not isdelete:
        minNum = 0
    if typeTrainDB == 1:
        if isPCA:
            figureTitle = "The reliability of SVR and Random Forest. Use OTU only and PCA"
        else:
            figureTitle = "The reliability of SVR and Random Forest. Use OTU only"
    elif typeTrainDB == 2:
        if isPCA:
            figureTitle = "The reliability of SVR and Random Forest. Use Easy-get parameters only and PCA"
        else:
            figureTitle = "The reliability of SVR and Random Forest. Use Easy-get parameters only"
        dataFile = [(dataFile.index(d) + 1) * 1000 for d in dataFile]
    elif typeTrainDB == 3:
        if isPCA:
            figureTitle = "The reliability of SVR and Random Forest. Use both OTU and Easy parameters and PCA"
        else:
            figureTitle = "The reliability of SVR and Random Forest. Use both OTU and Easy parameters"
    elif typeTrainDB == 4:
        figureTitle = "The reliability of SVR and Random Forest. Use original OTU and PCA"
        dataFile = [(dataFile.index(d) + 1) * 1000 for d in dataFile]
    elif typeTrainDB == 5:
        figureTitle = "The reliability of SVR, Random Forest and NN. Use merged OTU"
        if isPCA:
            figureTitle = "The reliability of SVR and Random Forest.  Use merged OTU and PCA"
    elif typeTrainDB == 6:
        figureTitle = "The reliability of SVR, Random Forest and NN. Use both merged OTU and Easy-Get"
        if isPCA:
            figureTitle = "The reliability of SVR and Random Forest.  Use both merged OTU and Easy-Get with PCA"
    elif typeTrainDB == 7:
        figureTitle = "The reliability of SVR and Random Forest.Use both merged OTU and Easy-Get with MRMR"
    for i in range(len(targetList)):
        subCol = fillByKnn.loc[:, targetList[i]]
        # print("This is target: ", subCol )
        if targetNormal:
            subCol = preprocessing.minmax_scale(subCol, axis=0)
        # print("This is subCol: ", subCol)
        tempName = ''
        lableList = []  # the target's name
        finalErrorRF = []  # Random forest
        finalErrorSVR = []  # SVR
        finalErrorLR = []
        for fileName in dataFile:
            lableList += iteraNum * [str(fileName / 1000.0)]
            errorNN = []
            errorRF = []
            errorSVR = []
            errorLR = []
            fileSize = dataFile[0]
            if typeTrainDB == 1:
                trainData = pd.read_excel(
                    './Training Data/newWaterSamples_%d.xlsx' % fileName)
                # print("This is trainData : ", trainData)
            elif typeTrainDB == 2:
                if hasSalinity:
                    trainData = pd.read_excel(
                        './Training Data/easy_get_para.xlsx')
                else:
                    trainData = pd.read_excel(
                        './Training Data/easy_get_para_no_salinity.xlsx')
                    # print("This is trainData : ", trainData)
            elif typeTrainDB == 3:
                trainData = pd.read_excel(
                    './Training Data/OTUwithEasyPara_%d.xlsx' % fileName)  # Use easy parameters as training data
                # print("This is trainData : ", trainData )
            elif typeTrainDB == 4:
                trainData = pd.read_excel(
                    './Training Data/newWaterSamples_%d.xlsx' % fileSize)  # Use easy parameters as training data
            elif typeTrainDB == 5:
                trainData = pd.read_excel(
                    './Training Data/OTUmergedByLevel%d_transpose_isdeleted_%s_threshold_%d.xlsx' % (
                        targetLevel, str(isdelete), minNum))
            elif typeTrainDB == 6:
                trainData = pd.read_excel(
                    './Training Data/OTUmergedByLevel%d_transpose_isdeleted_%s_threshold_%d_with_Easy_Get.xlsx' % (
                        targetLevel, str(isdelete), minNum))
            elif typeTrainDB == 7:
                trainData = reduceDim.buildInputData(fileName, targetList, needNormalized)
            print("This is train data size : ", trainData.shape)
            if isCompareNormalization:
                # import plotly.plotly as py
                # from plotly.graph_objs import *

                # py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
                # py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')
                compareList = [1, 2, 3]
                figureTitle = "Compare the accuracy with different normalization methods"
                lableList_NOR = []
                x_axis_name_NOR = ['Normalize', 'Scale', 'MinMaxScaler']
                for i in compareList:
                    if i == 1:
                        xname = 'Normalize'
                    elif i == 2:
                        xname = 'Scale'
                    elif i == 3:
                        xname = 'MinMaxScaler'
                    lableList_NOR += iteraNum * [xname]
                    n_components = 0.6
                    errorRF_NOR = []
                    errorSVR_NOR = []
                    errorSVR_NOR = supportVectorM(trainData, subCol, iteraNum, targetNormal, isRegression,
                                                  isPCA, n_components, i)
                    print("This is svr error: ", errorSVR_NOR)
                    print("SVR Part %d DONE!" % (compareList.index(i) + 1))
                    finalErrorSVR.extend(errorSVR_NOR)

                    errorRF_NOR = randomForest(trainData, subCol, iteraNum, targetNormal, isRegression,
                                               isPCA, n_components, i)
                    print("This is rf error: ", errorRF_NOR)
                    print("RF Part %d DONE!" % (compareList.index(i) + 1))
                    finalErrorRF.extend(errorRF_NOR)
                print("This is lableList_NOR: ", lableList_NOR)

                # comparePCA(lableList_NOR, finalErrorSVR, finalErrorRF, x_axis_name_NOR, figureTitle)
                writer1 = pd.ExcelWriter(
                    './Results/remoteResultForPlot_%s_type_%d_components_%s_size_%d_compare normalization methods.xlsx' % (
                        targetList[0], typeTrainDB, str(n_components), dataFile[0]))
                pd.DataFrame(lableList_NOR).to_excel(writer1, 'sheet1')
                pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
                pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
                pd.DataFrame(x_axis_name_NOR).to_excel(writer1, 'sheet5')
                pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
                writer1.save()
                break
            elif isComparePCA:
                print("Comparing PCA...", )
                boolList = [True, False]
                figureTitle = "Compare the accuracy with and without PCA"
                lableList_PCA = []
                x_axis_name_PCA = ['With PCA', 'Without PCA']
                for testSize in testSizeList:
                    for i in boolList:
                        if i is True:
                            xname = 'With PCA'
                        else:
                            xname = 'Without PCA'
                        lableList_PCA += iteraNum * [xname]
                        isPCA = i
                        errorRF_PCA = []
                        errorSVR_PCA = []
                        if isPCA:
                            if isMLE:
                                n_components = 'mle'
                            else:
                                n_components = componentsNum
                        "Different algorithms for regression"

                        errorSVR_PCA = supportVectorM(trainData, subCol, iteraNum, targetNormal, isRegression,
                                                      isPCA, n_components, normalMethod, testSize, isKernel, kernelFunc)
                        print("This is svr error: ", errorSVR_PCA)
                        print("SVR Part %d DONE!" % (boolList.index(i) + 1))
                        finalErrorSVR.extend(errorSVR_PCA)

                        errorRF_PCA = randomForest(trainData, subCol, iteraNum, targetNormal, isRegression,
                                                   isPCA, n_components, normalMethod, testSize, isKernel, kernelFunc)
                        print("This is rf error: ", errorRF_PCA)
                        print("RF Part %d DONE!" % (boolList.index(i) + 1))
                        finalErrorRF.extend(errorRF_PCA)

                        # errorLR_PCA = linerRegression(trainData, subCol, iteraNum, targetNormal, isRegression,
                        #                               isPCA, n_components, normalMethod, testSize)
                        # print("This is rf error: ", errorLR_PCA)
                        # print("RF Part %d DONE!" % (boolList.index(i) + 1))
                        # finalErrorLR.extend(errorLR_PCA)

                    # print("This is lableList_PCA: ", lableList_PCA)
                    # comparePCA(lableList_PCA, finalErrorSVR, finalErrorRF, x_axis_name_PCA, figureTitle)
                    if typeTrainDB == 2:
                        if hasSalinity:
                            writer1 = pd.ExcelWriter(
                                './Results/remoteResultForPlot_%s_type_%d_n_compoenet_%s_only_EasyParameters_used_including_salinity.xlsx' % (
                                    targetList[0], typeTrainDB, str(n_components)))
                        else:
                            writer1 = pd.ExcelWriter(
                                './Results/remoteResultForPlot_%s_type_%d_only_EasyParameters_used_no_salinity.xlsx' % (
                                    targetList[0], typeTrainDB))
                    if typeTrainDB == 5:
                        writer1 = pd.ExcelWriter(
                            './Results/remoteResultForPlot_%s_type_%d_only_OTU_used_testSize_%.1f_n_component_%s_merged_Level_%d_Threshold_%d.xlsx' % (
                                targetList[0], typeTrainDB, testSize, str(n_components), targetLevel, minNum))
                    if typeTrainDB == 6:
                        if isKernel:
                            writer1 = pd.ExcelWriter(
                                './Results/remoteResultForPlot_%s_type_%d_both_merged_OTU_and Easy_get_testSize_%.1f_n_component_%s_merged_Level_%d_Threshold_%d_normal_method_%d_KernelPCA_%s.xlsx' % (
                                    targetList[0], typeTrainDB, testSize, str(n_components), targetLevel, minNum,
                                    normalMethod, kernelFunc))
                        else:
                            writer1 = pd.ExcelWriter(
                                './Results/remoteResultForPlot_%s_type_%d_both_merged_OTU_and Easy_get_testSize_%.1f_n_component_%s_merged_Level_%d_Threshold_%d_normal_method_%d.xlsx' % (
                                    targetList[0], typeTrainDB, testSize, str(n_components), targetLevel, minNum,
                                    normalMethod))
                    pd.DataFrame(lableList_PCA).to_excel(writer1, 'sheet1')
                    pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
                    pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
                    pd.DataFrame(x_axis_name_PCA).to_excel(writer1, 'sheet5')
                    pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
                    writer1.save()
                    print("This is final mean SVR: ", sum(finalErrorSVR) / len(finalErrorSVR))
                    print("This is final mean RF: ", sum(finalErrorRF) / len(finalErrorRF))
                    finalErrorRF = []
                    finalErrorSVR = []
            elif isCompareMRMR:
                print("Comparing mRMR...", )
                rows, columns = trainData.shape
                isUseOriginalData = False
                tempCheck = ''
                # print("This is : ", columns)
                # numFeaList = [int(columns / 6), int(columns / 4), int(columns / 3), int(columns / 2),
                #               int(2 * columns / 3)]
                numFeaList = [int(columns / 3), int(columns / 2),
                              int(2 * columns / 3), int(3 * columns) / 4]  # The number of features we need to choose
                # numFeaList = [50, 100, 250, 500]
                # numFeaList = [5,10,30,40]
                numRFList = [600]
                # numFeaList = [10]
                # numRFList = [600]
                # iteraNum = 2
                figureTitle = "Compare the accuracy based on the number of selected features"
                lableList_mRMR = []
                x_axis_name_mRMR = []
                for numFeature in numFeaList:

                    featureList = reduceDim.featureSelection(trainData, numFeature)
                    print("This is selected features: ", featureList)
                    # featureList.append(targetList[0])
                    newTrain = trainData[featureList]
                    # print("This is new training data: ", newTrain)
                    if isUseOriginalData:  # the RF algorithm use the original data or not
                        traindataForRF = pd.read_excel(
                            './Training Data/newWaterSamples_%d_easy_get.xlsx' % numRFList[
                                numFeaList.index(numFeature)])
                        tempCheck = 'True'
                        xname = str(numFeature) + ' / ' + str(numRFList[numFeaList.index(numFeature)])
                    else:
                        traindataForRF = newTrain
                        tempCheck = 'False'
                        xname = str(numFeature) + ' / ' + str(fileName)
                    # tempRFData = traindataForRF.iloc[:, :]
                    #
                    x_axis_name_mRMR.append(xname)
                    lableList_mRMR += iteraNum * [xname]
                    # print("This is data for RF: ", traindataForRF)

                    subCol = trainData[targetList[0]]
                    # # print("This is target: ", subCol)
                    errorSVR_mRMR = supportVectorM(newTrain, subCol, iteraNum, targetNormal, isRegression,
                                                   False, 6, normalMethod, 0.1, isKernel, kernelFunc)
                    print("This is svr error: ", errorSVR_mRMR)
                    print("SVR Part %d DONE!" % (numFeaList.index(numFeature) + 1))
                    finalErrorSVR.extend(errorSVR_mRMR)

                    errorRF_mRMR = randomForest(traindataForRF, subCol, iteraNum, targetNormal, isRegression,
                                                False, 6, 4, 0.1, isKernel, kernelFunc)
                    print("This is rf error: ", errorRF_mRMR)
                    print("RF Part %d DONE!" % (numFeaList.index(numFeature) + 1))
                    finalErrorRF.extend(errorRF_mRMR)




            writer1 = pd.ExcelWriter(
                './Results/mrmrResults/remoteResultForPlot_%s_type_%d_OTUs_and_Easy_get_Size_%d_mRMR_testSize_%.1f_normal_method_%d_useOriginal_%s.xlsx' % (
                    targetList[0], typeTrainDB, fileName, testSizeList[0],
                    normalMethod, tempCheck))
            pd.DataFrame(lableList_mRMR).to_excel(writer1, 'sheet1')
            pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
            pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
            pd.DataFrame(x_axis_name_mRMR).to_excel(writer1, 'sheet5')
            pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
            writer1.save()
            # print("This is final mean SVR: ", sum(finalErrorSVR) / len(finalErrorSVR))
            # print("This is final mean RF: ", sum(finalErrorRF) / len(finalErrorRF))
            # finalErrorRF = []
            # finalErrorSVR = []

            "As backup"
            # else:
            #     if isPCA:
            #         if isMLE:
            #             n_components = 'mle'
            #         else:
            #             n_components = 0.7
            #             # normalized_trainData = reduceDim.featureExtraction(normalized_trainData, n_components)
            #     else:
            #         n_components = "No PCA"  # without using PCA
            #     # print("This is trainData:", normalized_trainData)
            #     # trainData[targetList[i]] = subCol.values  # this data will be used to test the efficiency of ELM and RF
            #     errorSVR = supportVectorM(trainData, subCol, iteraNum, targetNormal, isRegression, isPCA,
            #                               n_components)
            #     print("This is svr error: ", errorSVR)
            #     print("SVR Part %d DONE!" % (dataFile.index(fileName) + 1))
            #     finalErrorSVR.extend(errorSVR)
            #
            #     errorRF = randomForest(trainData, subCol, iteraNum, targetNormal, isRegression, isPCA,
            #                            n_components)
            #     print("This is rf error: ", errorRF)
            #     print("RF Part %d DONE!" % (dataFile.index(fileName) + 1))
            #     finalErrorRF.extend(errorRF)
            #
            # if typeTrainDB == 2 or typeTrainDB == 4:
            #     temp1 = list(set(lableList))
            #     x_axis_name = [int((temp1.index(p) + 1)) for p in temp1]
            # else:
            #     x_axis_name = sorted(list(set(lableList)), reverse=True)
            #
            # if isRemote:
            #     writer1 = pd.ExcelWriter(
            #         './Results/remoteResultForPlot_%s_type_%d_compo_%s_size_%d.xlsx' % (
            #             targetList[i], typeTrainDB, str(n_components), dataFile[0]))
            #     pd.DataFrame(lableList).to_excel(writer1, 'sheet1')
            #     pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
            #     pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
            #     pd.DataFrame(x_axis_name).to_excel(writer1, 'sheet5')
            #     pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
            #     writer1.save()
            # else:
            #     import plotly.plotly as py
            #     from plotly.graph_objs import *
            #
            #     if typeTrainDB == 2:
            #         temp1 = list(set(lableList))
            #         x_axis_name = [(temp1.index(p) + 1) for p in temp1]
            #         # lableList = x_axis_name
            #     else:
            #         x_axis_name = sorted(list(set(lableList)), reverse=True)
            #         # Draw the figure
            #     trace1 = {
            #         "x": lableList,
            #         "y": finalErrorSVR,
            #         "line": {"color": "rgba(102,194,165,1)"},
            #         "name": "SVR",
            #         "type": "box",
            #         "xaxis": "x",
            #         "yaxis": "y"
            #     }
            #     trace2 = {
            #         "x": lableList,
            #         "y": finalErrorRF,
            #         "line": {"color": "rgba(141,160,203,1)"},
            #         "name": "Random Forest",
            #         "type": "box",
            #         "xaxis": "x",
            #         "yaxis": "y"
            #     }
            #     data = Data([trace1, trace2])
            #     layout = {
            #         "boxmode": "group",
            #         "margin": {
            #             "r": 10,
            #             "t": 25,
            #             "b": 40,
            #             "l": 60
            #         },
            #         # "title": "The reliability of ELM and Random Forest",
            #         "title": figureTitle,
            #         "xaxis": {
            #             "categoryarray": x_axis_name,
            #             "categoryorder": "array",
            #             "domain": [0, 1],
            #             "title": targetList[i],
            #             "type": "category"
            #         },
            #         "yaxis": {
            #             "domain": [0, 1],
            #             "title": "RMSE-Root mean square error"
            #         }
            #     }
            #     fig = Figure(data=data, layout=layout)
            #     plot_url = py.plot(fig)
            #
            # print("This is final mean SVR: ", sum(finalErrorSVR) / len(finalErrorSVR))
            # print("This is final mean RF: ", sum(finalErrorRF) / len(finalErrorRF))
