import numpy as np
import pandas as pd
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV
from sklearn import preprocessing
from sklearn.model_selection import train_test_split


def supportVectorM(data, target, iterNum, isNormal, isRegression):
    X_norm = data
    y = target
    svrList = []
    for j in range(iterNum):
        X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
        C_range = np.logspace(0, 2, num=20)
        gamma_range = np.logspace(-1, 1, num=3) # best 0.1
        svr_rbf = GridSearchCV(SVR(kernel='rbf'), cv=5,
                               param_grid={"C": C_range,
                                           "gamma": gamma_range}, n_jobs=1)
        svr_rbf.fit(X_train, y_train)
        print("The best parameters are %s with a score of %0.2f"
              % (svr_rbf.best_params_, svr_rbf.best_score_))
        # svr_rbf = SVR(kernel='rbf', C=1000.0, gamma='auto', max_iter=-1, epsilon=0.1)
        # svr_poly = SVR(kernel='poly', C=1000, degree=3)
        y_pred = svr_rbf.predict(X_test)
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
            svrList.append(sum_erro)
            print("This is mean error for SVR: ", sum_erro)
            print("This is iteration num: ", j + 1)
    return svrList


def randomForest(data, target, iterNum, isNormal, isRegression):
    X_norm = data
    y = target
    rfList = []
    for j in range(iterNum):
        X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
        param_test1 = {'n_estimators': range(10, 91, 10), 'max_depth': range(4, 14, 2)}
        regr_rf = GridSearchCV(estimator=RandomForestRegressor(),
                               param_grid=param_test1, cv=5, n_jobs=1)
        # regr_rf = RandomForestRegressor(n_estimators=numTree, max_depth=max_depth,oob_score=True)
        regr_rf.fit(X_train, y_train)
        print("The best parameters are %s with a score of %0.2f"
              % (regr_rf.best_params_, regr_rf.best_score_))
        # Predict on new data
        y_pred = regr_rf.predict(X_test)
        if isRegression:
            return y_pred
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
            print("This is mean error for RF: ", sum_erro)
            print("This is iteration num: ", j + 1)
    return rfList


if __name__ == '__main__':

    dataFile = [950,850, 750]
    iteraNum = 10
    targetList = ['salinity']
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    # Y
    typeTrainDB = 1
    isRegression = False
    isCheckPara = False
    isRemote = True
    # isRemote = False
    targetNormal = isCheckPara

    if typeTrainDB == 1:
        figureTitle = "The reliability of SVR and Random Forest. Use OTU only"
    elif typeTrainDB == 2:
        figureTitle = "The reliability of SVR and Random Forest. Use Easy-get parameters only"
        dataFile = [(dataFile.index(d) + 1) * 1000 for d in dataFile]
    elif typeTrainDB == 3:
        figureTitle = "The reliability of SVR and Random Forest. Use both OTU and Easy parameters"

    for i in range(len(targetList)):
        subCol = fillByKnn.loc[:, targetList[i]]
        if targetNormal:
            subCol = preprocessing.MinMaxScaler().fit_transform(subCol)
        # print("This is subCol: ", subCol)
        tempName = ''
        lableList = []  # the target's name
        finalErrorRF = []  # Random forest
        finalErrorSVR = []  # SVR
        for fileName in dataFile:
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

            # trainData[targetList[i]] = subCol.values  # this data will be used to test the efficiency of ELM and RF
            # print("This is trainData:",trainData)
            errorSVR = supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
            print("This is svr error: ", errorSVR)
            print("SVR Part %d DONE!" % (dataFile.index(fileName) + 1))
            finalErrorSVR.extend(errorSVR)

            errorRF = randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
            print("This is rf error: ", errorRF)
            print("RF Part %d DONE!" % (dataFile.index(fileName) + 1))
            finalErrorRF.extend(errorRF)

        if typeTrainDB == 2:
            temp1 = list(set(lableList))
            x_axis_name = [(temp1.index(p) + 1) for p in temp1]
        else:
            x_axis_name = sorted(list(set(lableList)), reverse=True)

        if isRemote:
            writer1 = pd.ExcelWriter(
                './Training Data/remoteResultForPlot_%s_type_%d.xlsx' % (targetList[i], typeTrainDB))
            pd.DataFrame(lableList).to_excel(writer1, 'sheet1')
            pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
            pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
            pd.DataFrame(x_axis_name).to_excel(writer1, 'sheet5')
            pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet6')
            writer1.save()
        else:
            import plotly.plotly as py
            from plotly.graph_objs import *

            # py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
            py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')
            if typeTrainDB == 2:
                temp1 = list(set(lableList))
                x_axis_name = [(temp1.index(p) + 1) for p in temp1]
                # lableList = x_axis_name
            else:
                x_axis_name = sorted(list(set(lableList)), reverse=True)
                # Draw the figure
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
                # "title": "The reliability of ELM and Random Forest",
                "title": figureTitle,
                "xaxis": {
                    "categoryarray": x_axis_name,
                    "categoryorder": "array",
                    "domain": [0, 1],
                    "title": targetList[i],
                    "type": "category"
                },
                "yaxis": {
                    "domain": [0, 1],
                    "title": "RMSE-Root mean square error"
                }
            }
            fig = Figure(data=data, layout=layout)
            plot_url = py.plot(fig)

        print("This is final mean SVR: ", sum(finalErrorSVR) / len(finalErrorSVR))
        print("This is final mean RF: ", sum(finalErrorRF) / len(finalErrorRF))
