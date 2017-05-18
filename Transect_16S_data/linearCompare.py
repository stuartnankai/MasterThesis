import time
import pandas as pd
import numpy as np
from sklearn import preprocessing
import paramSVR
import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')


# def scale_linear_bycolumn(rawpoints, high=1.0, low=0.0):
#     mins = np.min(rawpoints, axis=0)
#     maxs = np.max(rawpoints, axis=0)
#     rng = maxs - mins
#     return high - (((high - low) * (maxs - rawpoints)) / rng)


# def extremLM(data, target):  # Extreme Learning Machine
#     scalar = 10000.0
#     errorList = []
#     X = data.iloc[:, :-1]
#     # print("This is X: ", X)
#     # X_norm = (X - X.mean()) / (X.max() - X.min())
#     X_norm = preprocessing.MinMaxScaler().fit_transform(X)
#     print("This is X_norm: ", X_norm)
#     y = data[target]
#     # y_int = y.apply(lambda x: x * scalar)  # Need to be fixed!
#     y_int = y * scalar
#     y_int = y_int.apply(np.int64)
#     for j in range(100):
#         sum_mean = 0
#         X_train, X_test, y_train, y_test = train_test_split(X_norm, y_int, test_size=0.2)
#         elm = ELM(hid_num=500).fit(X_train, y_train)
#         y_pred = (elm.predict(X_test))
#         # final_y_pred = [i/scalar for i in y_pred]
#         # final_y_test = [i/scalar for i in y_test]
#         print("This is pred value: ", y_pred)
#         print("This is real value: ", y_test)
#         for i in range(len(y_pred)):
#             sum_mean += ((y_pred[i] - y_test[i]) / scalar) ** 2
#         sum_erro = (np.sqrt(sum_mean / len(y_pred)))
#         print("This is sum_error: ", sum_erro)
#         if sum_erro >= 8:
#             print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! BIG ERROR")
#         errorList.append(sum_erro)
#         print("Iteration num: ", j + 1)
#     # return errorList

#
# def hpELM(data, target, iterNum):  # new ELM method for multi output
#     errorList = []
#     for j in range(iterNum):
#         X_train, X_test, T_train, T_test = train_test_split(data, target, test_size=0.2)
#         elm = ELM(data.shape[1], target.shape[1])  # number of data features /  number of classes
#         # elm.add_neurons(125, 'rbf_l2')  # rbf_l2 and sigm are the best
#         elm.add_neurons(125, 'sigm')
#         # elm.add_neurons(100,'tanh')
#         # elm.add_neurons(100, 'rbf_linf')
#         # elm.train(X_train,T_train,'r')
#         # elm.train(X_train, T_train, 'CV','r',k=5)
#         elm.train(X_train, T_train, 'LOO', 'OP', 'r')
#         T_pred = elm.predict(X_test)
#         # print("This is predict value: ", T_pred)
#         # print("This is real value: ", T_test)
#         print("This is error: ", elm.error(T_test, T_pred))
#
#         sum_mean = 0
#         T_pred_List = []
#         T_test_List = []
#         for x in np.nditer(T_pred):
#             T_pred_List.append(x)
#         for y in np.nditer(T_test):
#             T_test_List.append(y)
#         for i in range(len(T_pred_List)):
#             sum_mean += (T_pred_List[i] - T_test_List[i]) ** 2
#         sum_erro = (np.sqrt(sum_mean / len(T_pred_List)))
#         # print("This is sum_error: ", sum_erro)
#         if sum_erro >= 8:
#             print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! BIG ERROR")
#         errorList.append(sum_erro)
#         print("Iteration num: ", j + 1)
#
#         # Plot the figure
#         # plt.figure('ELM model')
#         # plt.plot(range(len(T_pred_List)), T_pred_List, 'b', label="predict")
#         # plt.plot(range(len(T_pred_List)), T_test_List, 'r', label="test")
#         # plt.legend(loc="upper right")  # show the lable
#         # plt.xlabel("The number of water samples")
#         # plt.ylabel("Real values")
#         # plt.text(len(T_pred_List) / 2, (max(T_test_List)) + 3, "RMSE: %.4f" % sum_erro)
#         # plt.show()
#     return errorList



def drawFigure(predValue, realValue, methodName):
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
                "x": 0.297619047619,
                "y": 105.207432998,
                "align": "left",
                "arrowcolor": "#636363",
                "arrowhead": 2,
                "arrowsize": 1,
                "arrowwidth": 2,
                "ax": 28,
                "ay": -106,
                "bgcolor": "rgba(0,0,0,0)",
                "bordercolor": "",
                "borderpad": 1,
                "borderwidth": 1,
                "font": {"size": 16},
                "opacity": 0.8,
                "showarrow": True,
                "text": "R<sup>2</sup> = 0.9840<br>y   = 199 - 316x",
                "xanchor": "auto",
                "xref": "x",
                "yanchor": "auto",
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
        "title": "Prediction vs Real",
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
            "title": "Real value",
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
            "range": [-11.6447875867, 216.490499768],
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
    funNum = 1
    # target = 'salinity'
    # target = 'NO3'
    # targetList = ['salinity', 'Depth', 'Temperature', 'O2', 'PO4', 'SiO2', 'NO2', 'NO3']
    targetList = ['salinity']
    iteraNum = 1  # the number of iteration

    dataFile = [750]
    # dataFile = [990, 975, 965, 950, 900]
    # fillByKnn = pd.read_excel('./Training Data/FillByKnn.xlsx')
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    lableList = []
    finalErrorDL = []
    finalErrorRF = []
    finalErrorSVR = []
    start = time.time()

    for i in range(len(targetList)):
        # fillByKnn1 = pd.read_excel('./Training Data/FillBy_%s.xlsx' % targetList[i])
        subCol = fillByKnn.loc[:, targetList[i]]
        print("This is subCol: ", subCol)
        for fileName in dataFile:
            lableList += iteraNum * [str(fileName / 1000.0)]
            errorDL = []
            errorRF = []
            errorSVR = []
            # trainData = pd.read_excel(
            #  all input no environmental parameters
            trainData = pd.read_excel(
                './Training Data/newWaterSamples_%d.xlsx' % fileName)
            # Three options!!!! For preprocessing normalization
            # normalized_trainData = preprocessing.normalize(trainData) #1
            # normalized_trainData = preprocessing.scale(trainData) #2
            normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3

            # trainData[targetList[i]] = subCol.values  # this data will be used to test the efficiency of ELM and RF
            errorSVR = paramSVR.supportVectorM(normalized_trainData,subCol,iteraNum,isNormal=False,isRegression=False)
            # errorSVR = supportVectorM(trainData, targetList[i], iteraNum)
            print("This is svr error: ", errorSVR)
            print("SVR Part %d DONE!" % (dataFile.index(fileName) + 1))
            finalErrorSVR.extend(errorSVR)


            errorRF = paramSVR.randomForest(normalized_trainData,subCol,iteraNum,isNormal=False,isRegression=False)
            # errorRF = randomForest(trainData, targetList[i], iteraNum)
            print("This is rf error: ", errorRF)
            print("RF Part %d DONE!" % (dataFile.index(fileName) + 1))
            finalErrorRF.extend(errorRF)
        # print("This is the mean error for ELM: ", sum(finalErrorELM) / float(len(finalErrorELM)))
        # print("This is the mean error for RF: ", sum(finalErrorRF) / float(len(finalErrorRF)))
        trace1 = {
            "x": lableList,
            # "y": finalErrorELM,
            "y": finalErrorSVR,
            "line": {"color": "rgba(102,194,165,1)"},
            # "name": "ELM",
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
            "title": "The reliability of SVR and Random Forest",
            "xaxis": {
                "categoryarray": sorted(list(set(lableList)), reverse=True),
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
    end = time.time()
    print("Time: %d seconds " % int((end - start)))