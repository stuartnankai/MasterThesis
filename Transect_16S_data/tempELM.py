import time
import numpy as np
import pandas as pd
import plotly.plotly as py
# import elm
import elm
from plotly.graph_objs import *
from sklearn import preprocessing
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split

# py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')


def buildELM(data,iterNum, isNormal, isRegression):
    X_norm = data
    rfList = []
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
        elmr = elm.ELMKernel()
        # elmr = elm.ELMRandom()
        # search for best parameter for this dataset
        # define "kfold" cross-validation method, "accuracy" as a objective function
        # to be optimized and perform 10 searching steps.
        # best parameters will be saved inside 'elmk' object
        elmr.search_param(X_norm, eval=50, cv='kfold')

        # split data in training and testing sets
        # use 80% of dataset to training and shuffle data before splitting
        tr_set, te_set = elm.split_sets(X_norm, training_percent=.8, perm=True)

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
                print(
                    "This is REAL value %.4f, ======ELM=====> PRED value: %.4f" % (y_test_list[i], y_pred[i]))
                # sum_mean += (y_pred[i] - y_test[i]) ** 2  # if the target is np array
                sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test_list[i]) ** 2
                # else:
                #     print("This is REAL value %.4f, ======Random Forest=====> PRED value: %.4f" % (
                #         y_test.values[i], y_pred[i]))
                #     # sum_mean += (y_pred[i] - y_test.values[i]) ** 2
                #     sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test.values[i]) ** 2
            sum_erro = np.sqrt(sum_mean / len(y_pred))
            rfList.append(sum_erro)
            print("This is mean error for ELM: ", sum_erro)
            print("This is iteration num: ", j + 1)
    return rfList



if __name__ == '__main__':
    funNum = 3  # the number of function for deep learning method 1:normal,2:more neurons 3: more layers
    start = time.time()
    # targetNormal = True  # the target is normalized or not
    dataFile = [900, 850, 800, 750]
    lableList = []  # the target's name
    iteraNum = 1  # the number of iteration
    targetList = ['salinity']
    finalErrorELM = []
    # targetList = ['salinity', 'Depth', 'Temperature', 'O2', 'PO4', 'SiO2', 'NO2', 'NO3']
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    isRegression = False
    isCheckPara = False
    targetNormal = isCheckPara
    # trainData = pd.read_excel(
    #     './Training Data/OTUwithEasyPara_%d.xlsx' % 600)  #

    trainData = pd.read_excel(
        './Training Data/easy_get_para.xlsx')
    subCol = fillByKnn.loc[:, targetList[0]]
    trainData[targetList[0]] = subCol.values
    cols = trainData.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    trainData = trainData[cols].values
    # print(trainData)
    normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3
    temp = buildELM(trainData, iteraNum, isNormal=False, isRegression=False)
    print("This is : ", temp)
    # load dataset
    # data = elm.read("./Training Data/iris.data")
    # print("This is data:", data)
    # data = pd.read_excel('./Training Data/testSampleELM.xlsx')
    # newData = data.values
    # print("This is newData: ", newData)
    #
    #
    # # create a classifier
    # elmr = elm.ELMKernel()
    # # search for best parameter for this dataset
    # # define "kfold" cross-validation method, "accuracy" as a objective function
    # # to be optimized and perform 10 searching steps.
    # # best parameters will be saved inside 'elmk' object
    # elmr.search_param(newData, eval=10,cv='kfold')
    #
    # # split data in training and testing sets
    # # use 80% of dataset to training and shuffle data before splitting
    # tr_set, te_set = elm.split_sets(newData, training_percent=.8, perm=True)
    #
    # # train and test
    # # results are Error objects
    # tr_result = elmr.train(tr_set)
    #
    # te_result = elmr.test(te_set)
    #
    # # print("This is tr_result: ", tr_result.expected_targets)
    # # print("This is tr_result pre: ",tr_result.predicted_targets )
    # print("This is te_result: ", te_result.expected_targets) #expected is the real value
    # print("This is te_result predict: ", te_result.predicted_targets )
    # # print(te_result.get_accuracy)
