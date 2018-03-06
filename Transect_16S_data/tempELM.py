import time
import numpy as np
import pandas as pd
import plotly.plotly as py
import reduceDim
# import elm
import elm
from plotly.graph_objs import *
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')


def buildELM(data, iterNum, isNormal, isRegression, isPCA, n_components,normalMethod):
    rfList = []
    elmr = elm.ELMKernel()
    # elmr = elm.ELMRandom()
    elmr.search_param(data, eval=100, cv='kfold')
    # print("This is X_norm: ", X_norm)
    for j in range(iterNum):
        # X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)

        # param_test1 = {'n_hidden': range(10, 21, 10)}
        # model = GridSearchCV(estimator=elm.ELMRegressor(),
        #                        param_grid=param_test1, cv=5, n_jobs=1)
        # model = elm.ELMRegressor(n_hidden=tempDim,activation_func='sine')
        # model = elm.ELMRegressor(activation_func='tanh')
        # model = elm.GenELMRegressor()
        # temp = model.fit(X_train, y_train)
        # print("The best parameters are %s with a score of %0.2f"
        #       % (model.best_params_, model.best_score_))
        # Predict on new data
        # y_pred = temp.predict(X_test).tolist()
        # y_test_list = y_test.tolist()

        # create a classifier
        # elmr = elm.ELMRandom()
        # search for best parameter for this dataset
        # define "kfold" cross-validation method, "accuracy" as a objective function
        # to be optimized and perform 10 searching steps.
        # best parameters will be saved inside 'elmk' object


        # split data in training and testing sets
        # use 80% of dataset to training and shuffle data before splitting

        tr_set, te_set = elm.split_sets(data, training_percent=.9, perm=True)
        # print("This is tr_set: ", tr_set)

        X_train = tr_set[:, 1:].copy()
        # print("This is X_train", X_train)
        X_test = te_set[:, 1:].copy()
        # print("This is X_test: ", X_test)


        if normalMethod == 1:
            print("Normalizer() is using..." )
            sc = preprocessing.Normalizer()
        elif normalMethod == 2:
            print("StandardScalar() is using...")
            sc = preprocessing.StandardScaler()
        elif normalMethod == 3:
            print("MinMaxScalar() is using...")
            sc = preprocessing.MinMaxScaler()

        sc.fit(X_train)
        X_train_std = sc.transform(X_train)
        X_test_std = sc.transform(X_test)

        if isPCA:
            X_train, X_test = reduceDim.featureExtraction(X_train_std, X_test_std, n_components)
        else:
            X_train = X_train_std
            X_test = X_test_std

        tr_set = np.c_[tr_set[:, 0], X_train]
        te_set = np.c_[te_set[:, 0], X_test]

        # print("This is new tr_set: ", tr_set)
        # print("This is new te_set: ", te_set)
        # train and test
        # results are Error objects
        tr_result = elmr.train(tr_set)
        te_result = elmr.test(te_set)
        y_test_list = te_result.expected_targets
        y_pred = te_result.predicted_targets
        # print("This is tr_result: ", tr_result.expected_targets)
        # print("This is tr_result pre: ",tr_result.predicted_targets )
        # print("This is te_result: ", te_result.expected_targets)  # expected is the real value
        # print("This is te_result predict: ", te_result.predicted_targets)
        # print(te_result.get_accuracy)
        if isRegression:
            return y_pred
        else:
            sum_mean = 0
            for i in range(len(y_pred)):
                # print(
                #     "This is REAL value %.4f, ======ELM=====> PRED value: %.4f" % (y_test_list[i], y_pred[i]))
                # sum_mean += (y_pred[i] - y_test[i]) ** 2  # if the target is np array
                sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test_list[i]) ** 2
                # else:
                #     print("This is REAL value %.4f, ======Random Forest=====> PRED value: %.4f" % (
                #         y_test.values[i], y_pred[i]))
                #     # sum_mean += (y_pred[i] - y_test.values[i]) ** 2
                #     sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test.values[i]) ** 2
            sum_erro = np.sqrt(sum_mean / len(y_pred))
            rfList.append(sum_erro)
            print("This is RMSE for ELM: ", sum_erro)
            print("This is iteration num: ", j + 1)
    return rfList


if __name__ == '__main__':
    funNum = 3  # the number of function for deep learning method 1:normal,2:more neurons 3: more layers
    start = time.time()
    # targetNormal = True  # the target is normalized or not
    dataFile = [950]
    lableList = []  # the target's name
    iteraNum = 10  # the number of iteration
    targetList = ['NO3']
    finalErrorELM = []
    # targetList = ['salinity', 'Depth', 'Temperature', 'O2', 'PO4', 'SiO2', 'NO2', 'NO3']
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    isRegression = False
    isCheckPara = False
    isNormal = False
    isPCA = True
    n_components = 'mle'
    targetNormal = isCheckPara
    # trainData = pd.read_excel(
    #     './Training Data/OTUwithEasyPara_%d.xlsx' % 600)
    temptrainData = pd.read_excel('./Training Data/easy_get_para.xlsx')
    #

    # trainData = pd.read_excel(
    #     './Training Data/easy_get_para.xlsx')
    subCol = fillByKnn.loc[:, targetList[0]]
    # print("This is target: ", subCol)

    # Three options!!!! For preprocessing normalization
    # normalized_trainData = pd.DataFrame(preprocessing.normalize(trainData))  # 1
    # normalized_trainData = preprocessing.scale(trainData) #2
    # normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3
    # print("This is data frame: ", normalized_trainData)
    # normalized_trainData[targetList[0]] = subCol.values
    # cols = normalized_trainData.columns.tolist()
    # cols = cols[-1:] + cols[:-1]
    # trainData = normalized_trainData[cols].values

    temptrainData[targetList[0]] = subCol.values
    cols = temptrainData.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    trainData = temptrainData[cols].values
    print(trainData)
    # normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3
    temp = buildELM(trainData, iteraNum, isNormal, isRegression, isPCA, n_components,2)
