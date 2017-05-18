import time
import pandas as pd
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
import deepLearningTest
from sklearn.cross_validation import train_test_split
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import paramSVR
import testDL
import tempELM

# py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')


#
# def scale_linear_bycolumn(rawpoints, high=1.0, low=0.0):
#     mins = np.min(rawpoints, axis=0)
#     maxs = np.max(rawpoints, axis=0)
#     rng = maxs - mins
#     return high - (((high - low) * (maxs - rawpoints)) / rng)
#
#
# def randomForest(data, target, iterNum, isNormal, isRegression):
#     X_norm = data
#     y = target
#     # max_depth = 30
#     max_depth = None
#     numTree = 10
#     rfList = []
#     for j in range(iterNum):
#         X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
#         regr_rf = RandomForestRegressor(n_estimators=numTree, max_depth=max_depth)
#         regr_rf.fit(X_train, y_train)
#         # Predict on new data
#         y_pred = regr_rf.predict(X_test)
#         if isRegression:
#             return y_test, y_pred
#         else:
#             sum_mean = 0
#             for i in range(len(y_pred)):
#                 if isNormal:
#                     print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test[i], y_pred[i]))
#                     # sum_mean += (y_pred[i] - y_test[i]) ** 2  # if the target is np array
#                     sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test[i]) ** 2
#                 else:
#                     print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test.values[i], y_pred[i]))
#                     # sum_mean += (y_pred[i] - y_test.values[i]) ** 2
#                     sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test.values[i]) ** 2
#             sum_erro = np.sqrt(sum_mean / len(y_pred))
#             rfList.append(sum_erro)
#     return rfList
#
#
# def supportVectorM(data, target, iterNum, isNormal, isRegression):
#     X_norm = data
#     y = target
#     svrList = []
#     for j in range(iterNum):
#         X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
#         C_range = np.logspace(-1, 5, 15)
#         gamma_range = np.logspace(-2, 6, 15)
#         svr_rbf = GridSearchCV(SVR(kernel='rbf'), cv=5,
#                            param_grid={"C": C_range,
#                                        "gamma": gamma_range})
#         # svr_rbf = SVR(kernel='rbf', C=1000.0, gamma='auto', max_iter=-1, epsilon=0.1)
#         # svr_poly = SVR(kernel='poly', C=1000, degree=3)
#         y_pred = svr_rbf.fit(X_train, y_train).predict(X_test)
#         # y_pred = svr_poly.fit(X_train, y_train).predict(X_test)
#         if isRegression:
#             return y_test, y_pred
#         else:
#             sum_mean = 0
#             for i in range(len(y_pred)):
#                 if isNormal:
#                     print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test[i], y_pred[i]))
#                     # sum_mean += (y_pred[i] - y_test[i]) ** 2  # if the target is np array
#                     sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test[i]) ** 2
#                 else:
#                     print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test.values[i], y_pred[i]))
#                     # sum_mean += (y_pred[i] - y_test.values[i]) ** 2
#                     sum_mean += (float("{0:.4f}".format(float(y_pred[i]))) - y_test.values[i]) ** 2
#             sum_erro = np.sqrt(sum_mean / len(y_pred))
#             print("This is sum_erro: ", sum_erro)
#             svrList.append(sum_erro)
#     return svrList
# Plot the figure
# plt.figure('SVR model')
# plt.plot(range(len(y_rbf)), y_rbf, 'b', label="predict")
# plt.plot(range(len(y_test)), y_test, 'r', label="test")
# plt.legend(loc="upper right")  # show the lable
# plt.xlabel("The number of water samples")
# plt.ylabel("Real values")
# plt.text(len(y_rbf) / 2, (max(y_test)) + 3, "RMSE: %.4f" % sum_erro)
# plt.show()


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

    funNum = 3  # the number of function for deep learning method 1:normal,2:more neurons 3: more layers
    start = time.time()
    # targetNormal = True  # the target is normalized or not
    dataFile = [900,850,800,750]
    iteraNum = 10  # the number of iteration
    targetList = ['salinity']
    # targetList = ['salinity', 'Depth', 'Temperature', 'O2', 'PO4', 'SiO2', 'NO2', 'NO3']
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    isRegression = False
    isCheckPara = False
    targetNormal = isCheckPara
    typeTrainDB = 1  # 1: only OTUs 2: only easy_get para 3: OUT + easy_get
    if typeTrainDB == 1:
        figureTitle = "The reliability of SVR, Random Forest and NN. Use OTU only"
    elif typeTrainDB == 2:
        figureTitle = "The reliability of SVR, Random Forest and NN. Use Easy-get parameters only"
        dataFile = [(dataFile.index(d) + 1) * 1000 for d in dataFile]
    elif typeTrainDB == 3:
        figureTitle = "The reliability of SVR, Random Forest and NN. Use both OTU and Easy parameters"

    # dataFile = [750]  # the max percentage of zeors
    # dataFile = [990, 970, 950, 900, 850,800,750]

    # dataFile = [1000,2000,3000,4000,5000]
    # fillByKnn = pd.read_excel('./Training Data/FillByKnn.xlsx')
    lableList = []  # the target's name
    finalErrorRF = []  # Random forest
    finalErrorSVR = []  # SVR
    finalErrorNN = []  # deeplearning
    finalErrorELM = [] # ELM

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
                testSVR, predSVR = testDL.supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal,
                                                         isRegression)
                print("This is svr : ", testSVR)
                print("SVR Part DONE!")
                # 2. RF
                testRF, predRF = testDL.randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                print("This is rf error: ", testRF)
                print("RF Part DONE!")
                trace1 = {
                    "x": testSVR,
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
                    "x": testRF,
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
                    "x": testSVR,
                    "y": testSVR,
                    "line": {
                        "color": "#7FDBFF",
                        "dash": "dot"
                    },
                    "name": "y=x",
                    "type": "scatter",
                }
                data = Data([trace1, trace2, trace3])
                layout = {
                    "autosize": False,
                    "height": 800,
                    "title": "Relation: SVR and RF",
                    "titlefont": {
                        "color": "#000000",
                        "family": "Courier New, monospace",
                        "size": 20
                    },
                    "width": 800,
                    "xaxis": {
                        "title": "Real Value",
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
        else:
            # compare the accuracy between SVR, RF and DeepLearning based on the same data size
            for fileName in dataFile:
                # trainData = pd.read_excel(
                #     './Training Data/OTU_Transpose_by_ratio_%d.xlsx' % fileName)  # all input no environmental parameters
                # trainData = pd.read_excel(
                #     './Training Data/newWaterSamples_%d.xlsx' % fileName)
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
                    errorSVR = paramSVR.supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal,
                                                       isRegression)
                    print("This is svr error: ", errorSVR)
                    print("SVR Part %d DONE!" % (i + 1))
                    finalErrorSVR.extend(errorSVR)
                    # 2. RF
                    errorRF = paramSVR.randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                    print("This is rf error: ", errorRF)
                    print("RF Part %d DONE!" % (i + 1))
                    finalErrorRF.extend(errorRF)

                    # 3.ELM
                    # errorELM = deepLearningTest.hpELM(normalized_trainData, subCol, iteraNum, targetNormal)
                    # print("This is ELM error: ", errorELM)
                    # print("ELM Part %d DONE!" % (i + 1))
                    # finalErrorELM.extend(errorELM)

                    # 4. DeepLearning
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
                trace1 = {
                    "x": lableList,
                    "y": finalErrorSVR,
                    # "line": {"color": "rgba(102,194,165,1)"},
                    "marker": {"color": "#3D9970"},
                    "name": "SVR",
                    "type": "box",
                    "xaxis": "x",
                    "yaxis": "y"
                }
                trace2 = {
                    "x": lableList,
                    "y": finalErrorRF,
                    # "line": {"color": "rgba(141,160,203,1)"},
                    "marker": {"color": "#FF4136"},
                    "name": "Random Forest",
                    "type": "box",
                    "xaxis": "x",
                    "yaxis": "y"
                }
                trace3 = {
                    "x": lableList,
                    "y": finalErrorNN,
                    # "line": {"color": "rgba(141,160,203,1)"},
                    "marker": {"color": "#FF851B"},
                    "name": "Deep Learning",
                    "type": "box",
                    "xaxis": "x",
                    "yaxis": "y"
                }

                data = Data([trace1, trace2, trace3])
                # data = Data([trace1, trace2])
                layout = {
                    "boxmode": "group",
                    "margin": {
                        "r": 10,
                        "t": 25,
                        "b": 40,
                        "l": 60
                    },
                    "title": title,
                    "xaxis": {
                        "categoryarray": sorted(list(set(lableList)), reverse=True),
                        "categoryorder": "array",
                        "domain": [0, 1],
                        # "title": fileName,
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
    else:
        for i in range(len(targetList)):
            subCol = fillByKnn.loc[:, targetList[i]]
            if targetNormal:
                subCol = preprocessing.MinMaxScaler().fit_transform(subCol)
            # print("This is subCol: ", subCol)
            sizeName = 0
            for fileName in dataFile:
                sizeName = fileName
                lableList += iteraNum * [str(fileName / 1000.0)]
                errorNN = []
                errorRF = []
                errorSVR = []
                errorELM = []
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

                trainData[targetList[i]] = subCol.values  # this data will be used to test the efficiency of ELM and RF
                # print("This is trainData:", trainData)
                errorSVR = paramSVR.supportVectorM(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                print("This is svr error: ", errorSVR)
                print("SVR Part %d DONE!" % (dataFile.index(fileName) + 1))
                finalErrorSVR.extend(errorSVR)

                errorRF = paramSVR.randomForest(normalized_trainData, subCol, iteraNum, targetNormal, isRegression)
                print("This is rf error: ", errorRF)
                print("RF Part %d DONE!" % (dataFile.index(fileName) + 1))
                finalErrorRF.extend(errorRF)

                tempData = pd.DataFrame(normalized_trainData)
                tempData[targetList[i]] = subCol.values
                cols = tempData.columns.tolist()
                cols = cols[-1:] + cols[:-1]
                newtrainData = tempData[cols].values
                # print ("This is newtrainData: ", newtrainData)
                errorELM = tempELM.buildELM(newtrainData, iteraNum, targetNormal, isRegression)
                print("This is EML error: ", errorELM)
                print("ELM Part %d DONE!" % (dataFile.index(fileName) + 1))
                finalErrorELM.extend(errorELM)

                # if not targetNormal:
                #     y = subCol.values
                #     # if not use normalized target variables
                #     errorNN = testDL.buildDeepLearning(normalized_trainData, y, iteraNum, funNum)
                # # Using normalized target variables
                # else:
                #     errorNN = testDL.buildDeepLearning(normalized_trainData, subCol, iteraNum, funNum)
                # print("This is Deep Learning error: ", errorNN)
                # print("DL Part %d DONE!" % (i + 1))
                # finalErrorNN.extend(errorNN)
            if typeTrainDB == 2:
                temp1 = list(set(lableList))
                x_axis_name = [(temp1.index(p) + 1) for p in temp1]
                # lableList = x_axis_name
            else:
                x_axis_name = sorted(list(set(lableList)), reverse=True)

                # if typeTrainDB != 2:
                #     writer1 = pd.ExcelWriter(
                #         './Training Data/remoteResultForPlot_%s_type_%d_size_%d.xlsx' % (
                #         targetList[i], typeTrainDB, sizeName))
                #     pd.DataFrame(lableList).to_excel(writer1, 'sheet1')
                #     pd.DataFrame(finalErrorSVR).to_excel(writer1, 'sheet2')
                #     pd.DataFrame(finalErrorRF).to_excel(writer1, 'sheet3')
                #     pd.DataFrame(finalErrorELM).to_excel(writer1, 'sheet4')
                #     # pd.DataFrame(finalErrorNN).to_excel(writer1, 'sheet5')
                #     pd.DataFrame(x_axis_name).to_excel(writer1, 'sheet6')
                #     pd.DataFrame(figureTitle.split(' ')).to_excel(writer1, 'sheet7')
                #     writer1.save()
                # else:
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
            # trace3 = {
            #     "x": lableList,
            #     "y": finalErrorNN,
            #     "line": {"color": "rgba(181,130,233,1)"},
            #     "name": "Deep Learning",
            #     "type": "box",
            #     "xaxis": "x",
            #     "yaxis": "y"
            # }
            trace4 = {
                "x": lableList,
                "y": finalErrorELM,
                "line": {"color": "rgba(121,110,193,1)"},
                "name": "ELM",
                "type": "box",
                "xaxis": "x",
                "yaxis": "y"
            }
            data = Data([trace1, trace2, trace4])
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
        end = time.time()
        print("Time: %d seconds " % int((end - start)))
