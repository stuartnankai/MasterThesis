import time
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn import cross_validation
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn.naive_bayes import GaussianNB
import numpy as np
import matplotlib.pyplot as plt
import os.path
import tempELM
import paramSVR
import elm
from hpelm import ELM
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
from sklearn.metrics import accuracy_score
import plotly.plotly as py
from plotly.graph_objs import *
import deepLearningTest
from keras.models import Sequential
from keras.layers import Dense

# py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')

# py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')

#
# def scale_linear_bycolumn(rawpoints, high=1.0, low=0.0):
#     mins = np.min(rawpoints, axis=0)
#     maxs = np.max(rawpoints, axis=0)
#     rng = maxs - mins
#     return high - (((high - low) * (maxs - rawpoints)) / rng)
#
#
# def randomForest(X_train, y_train, X_test):
#     max_depth = 30
#     regr_rf = RandomForestRegressor(max_depth=max_depth)
#     regr_rf.fit(X_train, y_train)
#     # Predict on new data
#     y_pred = regr_rf.predict(X_test)
#     return y_pred
#
#
# def supportVectorM(X_train, y_train, X_test):
#     svr_rbf = SVR(kernel='rbf', C=1000.0, gamma='auto', max_iter=100, epsilon=0.1)
#     # svr_poly = SVR(kernel='poly', C=100,degree=1000)
#     y_pred = svr_rbf.fit(X_train, y_train).predict(X_test)
#     # y_pred = svr_poly.fit(X_train, y_train).predict(X_test)
#     return y_pred
#
#
# # !!!!!!!!!!!!!!!!!!!!!!!!!!!!! To Do List: 1: hpelm,2:PCA
# def hpELM(X_train, y_train, X_test):  # new ELM method for multi output
#
#     y = np.reshape(y_train, (X_train.shape[0], 1))
#     print("This is X-train value: ", X_train.shape)
#     print("This is y-train value: ", y.shape)
#     elm = ELM(X_train.shape[1], y.shape[1])  # number of data features /  number of classes
#     elm.add_neurons(50, 'rbf_l2')  # rbf_l2 and sigm are the best
#     elm.add_neurons(50, 'sigm')
#     # elm.add_neurons(100,'tanh')
#     # elm.add_neurons(100, 'rbf_linf')
#     # elm.train(X_train,T_train,'r')
#     # elm.train(X_train, T_train, 'CV','r',k=5)
#     elm.train(X_train, y, 'LOO', 'OP', 'r')
#     y_pred = elm.predict(X_test)
#     print("This is pred value: ", y_pred)
#     print("This is test value: ", y_test)
#     return y_pred
#
#
# def deepLearning(X_train, y_train, X_test):
#     model = Sequential()
#     inputDim = X_train.shape[1]
#     print("This is input dimension: ", inputDim)
#     model.add(Dense(inputDim, input_dim=inputDim, kernel_initializer='uniform', activation='relu'))
#     model.add(Dense(int(inputDim * 0.5), kernel_initializer='uniform', activation='relu'))
#     # model.add(Dense(int(inputDim * 0.25), kernel_initializer='uniform', activation='relu'))
#     model.add(Dense(100, kernel_initializer='uniform', activation='relu'))
#     model.add(Dense(1, kernel_initializer='uniform'))
#     model.compile(optimizer='rmsprop',
#                   loss='mse')
#     print(" Deep Learning Model construction.......DONE!")
#     # Train the model, iterating on the data in batches of n(32/64/128) samples
#     kerasModel = model
#     kerasModel.fit(X_train, y_train, epochs=100, batch_size=64, shuffle=True)
#     y_pred = kerasModel.predict(X_test)
#     return y_pred


def buildELM(X_train, y_train, X_test, y_test, target):
    tempData = pd.DataFrame(X_train)
    tempData[target] = y_train.values
    cols = tempData.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    newtrainData = tempData[cols].values

    tempData1 = pd.DataFrame(X_test)
    tempData1[target] = y_test.values
    cols1 = tempData1.columns.tolist()
    cols1 = cols[-1:] + cols[:-1]
    testData = tempData1[cols1].values

    elmr = elm.ELMKernel()
    # search for best parameter for this dataset
    # define "kfold" cross-validation method, "accuracy" as a objective function
    # to be optimized and perform 10 searching steps.
    # best parameters will be saved inside 'elmk' object
    elmr.search_param(newtrainData, eval=50, cv='kfold')

    # split data in training and testing sets
    # use 80% of dataset to training and shuffle data before splitting

    # train and test
    # results are Error objects
    tr_result = elmr.train(newtrainData)
    te_result = elmr.test(testData)
    y_test_list = te_result.expected_targets
    return te_result.predicted_targets


def drawFigure(predValue, realValue, methodName, paraName, datasize):
    slope, intercept, r_value, p_value, std_err = stats.linregress(realValue, predValue)
    print("r_value DONE!!!")
    regressionFunc = "R<sup>2</sup> = %.4f<br>y  = x" % (r_value ** 2)
    # accuarcy = accuracy_score(realValue, predValue)
    x_title = "Real value " + "( Algorithm: " + methodName + " )"
    header = "Prediction vs Real " + " ( Param: " + paraName + " Data Size: " + datasize + " )"
    trace1 = {
        "x": realValue,
        "y": predValue,
        "mode": "markers",
        "name": methodName,
        "type": "scatter",
        "uid": "0b9334"
    }
    trace2 = {
        "x": realValue,
        "y": realValue,
        "line": {
            "color": "rgb(55, 126, 184)",
            "width": 4
        },
        "name": "Real values",
        "opacity": 0.5,
        "type": "scatter",
        "uid": "c607b8",
        "xaxis": "x",
        "yaxis": "y"
    }
    data = Data([trace1, trace2])
    layout = {
        "annotations": [
            {
                "x": "auto",
                "y": "auto",
                "align": "auto",
                "arrowcolor": "#636363",
                "arrowhead": 2,
                "arrowsize": 1,
                "arrowwidth": 2,
                "ax": "auto",
                "ay": "auto",
                "bgcolor": "rgba(0,0,0,0)",
                "bordercolor": "",
                "borderpad": 1,
                "borderwidth": 1,
                "font": {"size": 16},
                "opacity": 0.8,
                "showarrow": False,
                "text": regressionFunc,
                "xanchor": "middle",
                "xref": "x",
                "yanchor": "middle",
                "yref": "y"
            }
        ],
        "autosize": True,
        "bargap": 0.2,
        "bargroupgap": 0,
        "barmode": "group",
        "boxgap": 0.3,
        "boxgroupgap": 0.3,
        "boxmode": "overlay",
        "dragmode": "zoom",
        "font": {
            "color": "#444",
            "family": "\"Open sans\", verdana, arial, sans-serif",
            "size": 12
        },
        "height": 672,
        "hidesources": False,
        "hovermode": "x",
        "legend": {
            "x": 1.02,
            "y": 1,
            "bgcolor": "#fff",
            "bordercolor": "#444",
            "borderwidth": 0,
            "font": {
                "color": "",
                "family": "",
                "size": 0
            },
            "traceorder": "normal",
            "xanchor": "left",
            "yanchor": "top"
        },
        "margin": {
            "r": 80,
            "t": 100,
            "autoexpand": True,
            "b": 80,
            "l": 80,
            "pad": 0
        },
        "paper_bgcolor": "#fff",
        "plot_bgcolor": "#fff",
        "separators": ".,",
        "showlegend": True,
        "smith": False,
        "title": header,
        "titlefont": {
            "color": "",
            "family": "",
            "size": 0
        },
        "width": 1189,
        "xaxis": {
            "anchor": "y",
            "autorange": True,
            "autotick": True,
            "domain": [0, 1],
            "dtick": 0.1,
            "exponentformat": "B",
            "gridcolor": "#eee",
            "gridwidth": 1,
            "linecolor": "#444",
            "linewidth": 1,
            "mirror": False,
            "nticks": 0,
            "overlaying": False,
            "position": 0,
            "range": [-0.0347290505845, 0.618062383918],
            "rangemode": "normal",
            "showexponent": "all",
            "showgrid": True,
            "showline": False,
            "showticklabels": True,
            "tick0": 0,
            "tickangle": "auto",
            "tickcolor": "#444",
            "tickfont": {
                "color": "",
                "family": "",
                "size": 0
            },
            "ticklen": 5,
            "ticks": "",
            "tickwidth": 1,
            "title": x_title,
            "titlefont": {
                "color": "",
                "family": "",
                "size": 0
            },
            "type": "linear",
            "zeroline": True,
            "zerolinecolor": "#444",
            "zerolinewidth": 1
        },
        "yaxis": {
            "anchor": "x",
            "autorange": True,
            "autotick": True,
            "domain": [0, 1],
            "dtick": 50,
            "exponentformat": "B",
            "gridcolor": "#eee",
            "gridwidth": 1,
            "linecolor": "#444",
            "linewidth": 1,
            "mirror": False,
            "nticks": 0,
            "overlaying": False,
            "position": 0,
            "rangemode": "normal",
            "showexponent": "all",
            "showgrid": True,
            "showline": False,
            "showticklabels": True,
            "tick0": 0,
            "tickangle": "auto",
            "tickcolor": "#444",
            "tickfont": {
                "color": "",
                "family": "",
                "size": 0
            },
            "ticklen": 5,
            "ticks": "",
            "tickwidth": 1,
            "title": "Predicted value",
            "titlefont": {
                "color": "",
                "family": "",
                "size": 0
            },
            "type": "linear",
            "zeroline": True,
            "zerolinecolor": "#444",
            "zerolinewidth": 1
        }
    }
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)


if __name__ == '__main__':
    start = time.time()
    # targetList = ['salinity', 'Depth', 'Temperature', 'O2', 'PO4', 'SiO2', 'NO2', 'NO3']
    targetNormal = False  # the target is normalized or not
    # targetList = ['O2', 'NO2', 'NO3', 'PO4', 'SiO2']
    # targetList = ['PO4']
    targetList = ['salinity']

    # targetList = ['salinity']
    dataFile = [750]  # the max percentage of zeors
    # dataFile = [990, 975, 965, 950, 900]
    # fillByKnn = pd.read_excel('./Training Data/FillByKnn.xlsx')
    waterNoNull = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')

    # print("This is target value: ", y)
    for fileName in dataFile:
        # trainData = pd.read_excel(
        #     './Training Data/OTU_Transpose_by_ratio_%d.xlsx' % fileName)  # all input no environmental parameters
        trainData = pd.read_excel(
            './Training Data/newWaterSamples_%d.xlsx' % fileName)
        featureDim = trainData.shape[1]
        normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3
        # percentage of zeros
        zeroPer = str((1000 - fileName) / 1000)
        for target in targetList:
            # subCol = fillByKnn.loc[:, target]
            subCol = waterNoNull.loc[:, target]
            y = subCol.values
            if targetNormal:
                subCol = preprocessing.MinMaxScaler().fit_transform(subCol)
            X_train, X_test, y_train, y_test = train_test_split(normalized_trainData, y, test_size=0.2)
            # print("This is y_test: ", y_test)
            # Comparing different algorithms
            # 1. SVR
            predSVR = paramSVR.supportVectorM(X_train, y_train, X_test)
            print("This is svr : ", predSVR)
            print("SVR Part DONE!")
            drawFigure(predSVR, y_test, "SVR", target, str(fileName))
            # # 2. RF
            predRF = paramSVR.randomForest(X_train, y_train, X_test)
            print("This is rf pred value: ", predRF)
            print("RF Part DONE!")
            drawFigure(predRF, y_test, "RF", target, str(fileName))

            # 3. ELM
            predELM = buildELM(X_train, y_train, X_test, y_test, target)
            print("This is ELM pred value: ", predELM)
            print("ELM Part DONE!")
            drawFigure(predRF, y_test, "RF", target, str(fileName))

            # 4. DeepLearning
            # tempDL = deepLearning(X_train, y_train, X_test)
            # predDL = tempDL.T.tolist()
            # predDL = predDL[0]
            # print("This is DL pred value:: ", predDL)
            # print("DL Part DONE!")
            # print("This is y_test :", y_test.tolist())
            # drawFigure(predDL, y_test.tolist(), "DL", target, str(fileName))
            # draw the figure
            x_title = "Real Value " + " ( Parameter: " + str(target) + " Size: " + str(fileName) + ")"
            trace1 = {
                "x": y_test,
                "y": predSVR,
                "marker": {
                    "color": "rgb(255,127, 14)",
                    "opacity": 0.55,
                    "sizemode": "area",
                    "sizeref": 0.01,
                },
                "mode": "markers",
                "name": "SVR",
                "type": "scatter",
            }
            trace2 = {
                "x": y_test,
                "y": predRF,
                "marker": {
                    "color": "rgb( 44,160, 40)",
                    "opacity": 0.55,
                    "sizemode": "area",
                    "sizeref": 0.01,
                },
                "mode": "markers",
                "name": "RF",
                "type": "scatter",
            }
            trace3 = {
                "x": y_test,
                "y": predELM,
                "marker": {
                    "color": "rgb( 31,119,180)",
                    "opacity": 0.55,
                    "sizemode": "area",
                    "sizeref": 0.01,
                },
                "mode": "markers",
                "name": "ELM",
                "type": "scatter",
            }
            # trace4 = {
            #     "x": y_test,
            #     "y": predDL,
            #     "marker": {
            #         "color": "rgb(148,103,189)",
            #         "opacity": 0.55,
            #         "sizemode": "area",
            #         "sizeref": 0.01,
            #     },
            #     "mode": "markers",
            #     "name": "Deep Learning",
            #     "type": "scatter",
            # }
            trace5 = {
                "x": y_test,
                "y": y_test,
                "line": {
                    "color": "#7FDBFF",
                    "dash": "dot"
                },
                "name": "y=x",
                "type": "scatter",
            }
            data = Data([trace1, trace2, trace3, trace5])
            layout = {
                "autosize": False,
                "height": 800,
                "title": "Relation: SVR,RF and DL",
                "titlefont": {
                    "color": "#000000",
                    "family": "Courier New, monospace",
                    "size": 20
                },
                "width": 800,
                "xaxis": {
                    "title": x_title,
                    "titlefont": {
                        "color": "#000000",
                        "family": "Courier New, monospace",
                        "size": 18
                    }
                },
                "yaxis": {
                    "title": "Prediction",
                    "titlefont": {
                        "color": "#000000",
                        "family": "Courier New, monospace",
                        "size": 18
                    }
                }
            }
            fig = Figure(data=data, layout=layout)
            plot_url = py.plot(fig)
        end = time.time()
        print("Time: %d seconds " % int((end - start)))
