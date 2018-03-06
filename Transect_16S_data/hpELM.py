from hpelm import ELM
import pandas as pd
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
import reduceDim
import paramSVR
import numpy as np


def hpElM(data, target, iterNum, isNormal, isRegression, isPCA, n_components, normalMethod, testSize):
    print("ELM is running")
    y = target
    elmList = []
    # neuronsNum = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 200]
    neuronsNum = [5, 10, 20, 30, 40, 50, 75, 200]
    # neuronsNum = [5]

    if normalMethod == 1:
        sc = preprocessing.Normalizer()
    elif normalMethod == 2:
        sc = preprocessing.StandardScaler()
    elif normalMethod == 3:
        sc = preprocessing.MinMaxScaler()
    for j in range(iterNum):
        errorList = []
        X_train, X_test, y_train, y_test = train_test_split(data, y, test_size=testSize)

        sc.fit(X_train)
        X_train_std = sc.transform(X_train)
        X_test_std = sc.transform(X_test)
        if isPCA:
            X_train, X_test = reduceDim.featureExtraction(X_train_std, X_test_std, n_components)
            # print("This is the size of input by using PCA: ", len(X_train[0]))
        else:
            print("Not use PCA...", )
            X_train = X_train_std
            X_test = X_test_std
        # print("This is : ", X_train)
        # print("This is : ", y_train.values)

        for neuron in neuronsNum:
            elm1 = ELM(len(X_train[1]), y.shape[1])
            elm1.add_neurons(neuron, 'sigm')
            # elm1.add_neurons(neuron, 'tanh')
            # elm1.add_neurons(neuron,'rbf_l2')
            elm1.train(X_train, y_train.values, 'CV', 'OP', 'r', k=3)
            y_pred_temp = elm1.predict(X_test)
            errorPara = elm1.error(y_pred_temp, y_test.values)
            errorList.append(errorPara)
        print("This is error list: ", errorList)
        bestPos = errorList.index(min(errorList))
        bestPara = neuronsNum[bestPos]
        print("This is the best number of neuron: ", bestPara)

        elm = ELM(len(X_train[1]), y.shape[1])
        elm.add_neurons(bestPara, 'sigm')
        # elm.add_neurons(bestPara,'tanh')
        # elm.add_neurons(bestPara,'rbf_l2')
        elm.train(X_train, y_train.values, 'CV', 'OP', 'r', k=5)
        y_pred_temp = elm.predict(X_test)

        # elm.add_neurons(30, "sigm")
        # elm.add_neurons(30, "rbf_l2")
        # elm.train(X_train, y_train.values, 'CV','OP',k=5)
        #
        # # svr_rbf = SVR(kernel='rbf', C=1000.0, gamma='auto', max_iter=-1, epsilon=0.1)
        # # svr_poly = SVR(kernel='poly', C=1000, degree=3)
        # y_pred_temp = elm.predict(X_test)
        # print("This is temp y_pred: ", y_pred_temp )
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
                    print("This is REAL value %.4f, ======ELM=====> PRED value: %.4f" % (y_test[i], y_pred[i]))
                    # sum_mean += (y_pred[i] - y_test[i]) ** 2  # if the target is np array

                    sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test[i]) ** 2
                else:
                    print("This is REAL value %.4f, ======ELM=====> PRED value: %.4f" % (y_test.values[i], y_pred[i]))
                    # sum_mean += (y_pred[i] - y_test.values[i]) ** 2

                    sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test.values[i]) ** 2
            sum_erro = np.sqrt(sum_mean / len(y_pred))
            elmList.append(sum_erro[0])
            print("This is RMSE for ELM: ", sum_erro[0])
            print("This is iteration num: ", j + 1)
    return elmList


if __name__ == '__main__':
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    iteraNum = 100  # the number of iteration
    targetList = ['NO3']
    isRegression = False
    isCheckPara = False
    isNormal = False
    isPCA = True
    # isPCA = False
    # ismRMR = True
    ismRMR = False
    n_components = 7
    targetNormal = isCheckPara
    normalMethod = 2
    testSize = 0.2
    fileName = 1000 # original data
    # fileName = 1000
    fileNameList = [600, 750, 800, 850, 900, 950, 1000]
    # fileName = fileNameList[0]  # check the efficiency data size
    # fileName = 850
    # featureNum = [5,10, 20, 30, 50,75,100]
    # featureNum = [5, 10, 15, 20, 30, 40, 44]
    featureNum = [5, 10, 20, 50, 75, 100, 150]
    # featureNum = [10, 50, 100, 150, 200, 300, 400]
    # featureNum = [5, 8, 10, 15, 20, 35, 50]
    # featureNum = [1, 2, 3, 4, 5]
    # featureNum = [15]
    # componentsNum = [0.9]
    componentsNum = [0.9, 0.75, 0.6, 0.45, 0.3, 0.15]
    errorList = []

    finalErrorELM = []
    finalErrorSVR = []
    finalErrorRF = []
    # figureTitle = "Compare the accuracy based on PCA"
    figureTitle = "Error analysis, isMRMR = True, threshold = 0.00, testsize = 0.2 "
    # figureTitle = "Compare the accuracy based on the number of selected features"
    # figureTitle = "Compare the efficiency of data pre-processing"
    lableList_mRMR = []
    lableList_PCA = []
    x_axis_name_mRMR = []
    x_axis_name_PCA = []
    kernelFunc = 'rbf'
    isKernel = False
    # X = pd.read_excel(
    #     './Training Data/OTUwithEasyPara_%d.xlsx' % fileName)
    # X = pd.read_excel('./Training Data/easy_get_para.xlsx')
    # X = pd.read_excel('./Training Data/OTUmergedByLevel4_transpose_isdeleted_True_threshold_10_with_Easy_Get.xlsx')
    # X = pd.read_excel('./Training Data/OTUwithEasyPara_%d.xlsx' % 5)
    # print("This is : ", X)
    # X = pd.read_excel(
    #     './Training Data/newWaterSamples_%d.xlsx' % fileName)
    subCol = fillByKnn.loc[:, targetList[0]]
    T = pd.DataFrame()
    T[targetList[0]] = subCol.values
    # print("This is : ", T.head())


    X = pd.read_excel('./Training Data/newWaterSamples_%d_easy_get.xlsx' % fileName)
    tempData = X.copy()
    tempData[targetList[0]] = subCol.values
    cols = tempData.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    indexdf = tempData[cols]
    print("This is train data: ", indexdf.head())
    if ismRMR:
        for numFeature in featureNum:
            print("This is feature number: ", numFeature)

            featureList = reduceDim.featureSelection(indexdf, numFeature)
            X = indexdf[featureList]
            # print("This is new X data: ", X)

            xname = str(numFeature)
            x_axis_name_mRMR.append(xname)
            lableList_mRMR += iteraNum * [xname]
            # errorFeature = sum(errorELM_PCA) / len(errorELM_PCA)
            # print("This is mean value: ", errorFeature)
            # errorList.append(errorFeature)

            # errorELM_PCA = hpElM(X, T, iteraNum, isNormal, isRegression, isPCA, n_components, normalMethod, testSize)
            # print("This is elm error: ", errorELM_PCA)
            # print("SVR Part %d DONE!" % (featureNum.index(numFeature) + 1))
            # finalErrorELM.extend(errorELM_PCA)
            # print("This is final error list: ", finalErrorELM)

            errorSVR_mRMR = paramSVR.supportVectorM(X, subCol, iteraNum, targetNormal, isRegression,
                                                    False, 6, normalMethod, testSize, isKernel, kernelFunc)
            print("This is svr error: ", errorSVR_mRMR)
            print("SVR Part %d DONE!" % (featureNum.index(numFeature) + 1))
            finalErrorSVR.extend(errorSVR_mRMR)
            print("This is final error svr: ", finalErrorSVR)

            errorRF_mRMR = paramSVR.randomForest(X, subCol, iteraNum, targetNormal, isRegression,
                                                 False, 6, 4, testSize, isKernel, kernelFunc)
            print("This is rf error: ", errorRF_mRMR)
            print("RF Part %d DONE!" % (featureNum.index(numFeature) + 1))
            finalErrorRF.extend(errorRF_mRMR)
            print("This is final error rf: ", finalErrorRF)

    elif isPCA:
        for numComponent in componentsNum:
            print("This is component number: ", numComponent)

            # check the size of file
            # xname = str(fileSize)

            # check the number of component
            xname = str(numComponent)

            x_axis_name_PCA.append(xname)
            lableList_PCA += iteraNum * [xname]
            # errorFeature = sum(errorELM_PCA) / len(errorELM_PCA)
            # print("This is mean value: ", errorFeature)
            # errorList.append(errorFeature)

            # errorELM_PCA = hpElM(X, T, iteraNum, isNormal, isRegression, isPCA, n_components, normalMethod, testSize)
            # print("This is elm error: ", errorELM_PCA)
            # print("SVR Part %d DONE!" % (featureNum.index(numFeature) + 1))
            # finalErrorELM.extend(errorELM_PCA)
            # print("This is final error list: ", finalErrorELM)

            errorSVR_PCA = paramSVR.supportVectorM(X, subCol, iteraNum, targetNormal, isRegression,
                                                   isPCA, numComponent, normalMethod, testSize, isKernel,
                                                   kernelFunc)
            print("This is svr error: ", errorSVR_PCA)
            # print("SVR Part %d DONE!" % (componentsNum.index(numComponent) + 1))
            finalErrorSVR.extend(errorSVR_PCA)
            print("This is final error svr: ", finalErrorSVR)

            errorRF_PCA = paramSVR.randomForest(X, subCol, iteraNum, targetNormal, isRegression,
                                                isPCA, numComponent, normalMethod, testSize, isKernel, kernelFunc)
            print("This is rf error: ", errorRF_PCA)
            # print("RF Part %d DONE!" % (componentsNum.index(numComponent) + 1))
            finalErrorRF.extend(errorRF_PCA)
            print("This is final error rf: ", finalErrorRF)

    if ismRMR:
        writer1 = pd.ExcelWriter(
            './Results/mrmrResults/FeatureSelectionFor_%s_Size_%d_testSize_%.1f_easy_get.xlsx' % (
                targetList[0], fileName, testSize))
        pd.DataFrame(lableList_mRMR).to_excel(writer1, 'sheet1')
        pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
        pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
        # pd.DataFrame(finalErrorELM).to_excel(writer1, 'sheet4')
        pd.DataFrame(x_axis_name_mRMR).to_excel(writer1, 'sheet5')
        pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
        writer1.save()
    elif isPCA:
        writer1 = pd.ExcelWriter(
            './Results/PCAResults/FeatureSelectionFor_%s_Size_%d_testSize_%.1f_easy_get.xlsx' % (
                targetList[0], fileName, testSize))
        pd.DataFrame(lableList_PCA).to_excel(writer1, 'sheet1')
        pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
        pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
        # pd.DataFrame(finalErrorELM).to_excel(writer1, 'sheet4')
        pd.DataFrame(x_axis_name_PCA).to_excel(writer1, 'sheet5')
        pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
        writer1.save()
