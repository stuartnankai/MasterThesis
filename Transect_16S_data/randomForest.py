from hpelm import ELM
import pandas as pd
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.grid_search import GridSearchCV
import reduceDim
import paramSVR
import numpy as np

if __name__ == '__main__':
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    iteraNum = 100  # the number of iteration
    targetList = ['NO3']

    isRegression = False
    isCheckPara = False
    isNormal = False
    # isPCA = True
    isPCA = False
    ismRMR = True
    normalMethod = 4
    n_components = 7
    targetNormal = isCheckPara
    # For random forest, normalization is not necessary
    testSize = 0.2
    # featureNum = [5, 10, 20, 30, 50, 80] # for size = 750 file
    # featureNum = [5, 10, 30, 60, 90, 120, 150] # for size = 800
    featureNum = [5,10,50,100,150,200,300] # for size = 900 file
    # featureNum = [3, 5, 10, 15, 20, 25, 30]
    # featureNum = [3, 5, 8, 10, 15, 20, 35]  # for size = 600 file
    # featureNum = [1, 2, 3, 4, 5]
    # featureNum = [15]
    errorList = []
    # fileName = 600
    # fileName = 750
    # fileName = 800
    fileName = 900
    finalErrorELM = []
    finalErrorSVR = []
    finalErrorRF = []
    finalErrorRF_nomRMR = []
    figureTitle = "Compare the accuracy of Random Forest based on the number of selected features"
    lableList_mRMR = []
    x_axis_name_mRMR = []
    # Using kernel PCA or not
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
    X = pd.read_excel('./Training Data/newWaterSamples_%d_easy_get.xlsx' % fileName)
    subCol = fillByKnn.loc[:, targetList[0]]
    T = pd.DataFrame()
    T[targetList[0]] = subCol.values
    # print("This is : ", T.head())
    tempData = X.copy()
    tempData[targetList[0]] = subCol.values
    cols = tempData.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    indexdf = tempData[cols]
    print("This is train data: ", indexdf.head())

    for numFeature in featureNum:
        print("This is feature number: ", numFeature)
        if ismRMR:
            featureList = reduceDim.featureSelection(indexdf, numFeature)
            X_mRMR = indexdf[featureList]
            # print("This is new X data: ", X_mRMR)
        xname = str(numFeature)
        x_axis_name_mRMR.append(xname)
        lableList_mRMR += iteraNum * [xname]
        # noinspection PyUnboundLocalVariable
        errorRF_mRMR = paramSVR.randomForest(X_mRMR, subCol, iteraNum, targetNormal, isRegression,
                                             isPCA, n_components, normalMethod, testSize, isKernel, kernelFunc)
        print("This is rf error: ", errorRF_mRMR)
        print("RF Part %d DONE!" % (featureNum.index(numFeature) + 1))
        finalErrorRF.extend(errorRF_mRMR)
        print("This is final error rf: ", finalErrorRF)
    for j in range(len(featureNum)):
        # print("Not using feature selection for Random forest: ", X)
        errorRF_nomMRMR = paramSVR.randomForest(X, subCol, iteraNum, targetNormal, isRegression,
                                                isPCA, n_components, normalMethod, testSize, isKernel, kernelFunc)
        print("This is rf_no error: ", errorRF_nomMRMR)
        finalErrorRF_nomRMR.extend(errorRF_nomMRMR)
        print("This is final error rf: ", finalErrorRF_nomRMR)
    writer1 = pd.ExcelWriter(
        './Results/mrmrResults/RF_FeatureSelectionFor_%s_Size_%d_testSize_%.1f_easy_get.xlsx' % (
            targetList[0], fileName, testSize))
    pd.DataFrame(lableList_mRMR).to_excel(writer1, 'sheet1')
    pd.DataFrame(finalErrorRF_nomRMR).to_excel(writer1, 'sheet2')
    pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
    # pd.DataFrame(finalErrorELM).to_excel(writer1, 'sheet4')
    pd.DataFrame(x_axis_name_mRMR).to_excel(writer1, 'sheet5')
    pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
    writer1.save()
