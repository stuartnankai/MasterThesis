import time

import pandas as pd
import hpelm
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import os.path
from keras.models import Sequential
from keras.layers import Dense
from elm import ELM
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.multioutput import MultiOutputRegressor
import plotly.plotly as py
from plotly.graph_objs import *

py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')

# Try to use mulit liner regression based on OTU and salinity
# salinity=β0+β1OTU1+β2OTU2+...+βnOTUn


def scale_linear_bycolumn(rawpoints, high=1.0, low=0.0):
    mins = np.min(rawpoints, axis=0)
    maxs = np.max(rawpoints, axis=0)
    rng = maxs - mins
    return high - (((high - low) * (maxs - rawpoints)) / rng)

def buildDataForMultiLineReg(name):
    trainInput1 = pd.read_excel('OTU_Transpose.xlsx')
    # print(trainInput1)
    trainInput2 = pd.read_excel('FillByKnn.xlsx')
    tempList = list(trainInput2[name])
    # print(tempList)
    se = pd.Series(tempList)
    trainInput1[name] = se.values

    writer = pd.ExcelWriter('OTU_Transpose_%s.xlsx' % name)
    trainInput1.to_excel(writer, 'sheet1')
    writer.save()
    return pd.read_excel('OTU_Transpose_%s.xlsx' % name)


def drawMultiRegre(data, target):
    # print(trainSalinity.head())
    # visualize the relationship between the features and the response using scatterplots
    X = data.iloc[:, :-1]
    X_norm = (X - X.mean()) / (X.max() - X.min())
    # print(X.head())
    # select a Series from the DataFrame
    y = data[target]
    # print the first 5 values
    # print (y.head())
    X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
    # default split is 80% for training and 20% for testing

    linreg = LinearRegression()
    model = linreg.fit(X_train, y_train)
    # print(model)
    # print(linreg.intercept_)
    # print(linreg.coef_)

    # pair the feature names with the coefficients
    # pairCoe = zip(list(trainSalinity), linreg.coef_)
    # for (x, y) in pairCoe:
    #     print(x, y)
    y_pred = model.predict(X_test)
    # print(y_pred)
    # print(type(y_pred))
    #
    # print(type(y_pred), type(y_test))
    # print(len(y_pred), len(y_test))
    # print(y_pred.shape, y_test.shape)

    sum_mean = 0
    for i in range(len(y_pred)):
        sum_mean += (y_pred[i] - y_test.values[i]) ** 2
    sum_erro = np.sqrt(sum_mean / len(y_pred))
    # calculate RMSE
    print("RMSE:", sum_erro)  # Root Mean Squared Error, RMSE
    end = time.time()
    print("Time: ", (end - start))

    plt.figure('multivariable linear regression model')
    plt.plot(range(len(y_pred)), y_pred, 'b', label="predict")
    plt.plot(range(len(y_pred)), y_test, 'r', label="test")
    plt.legend(loc="upper right")  # show the lable
    plt.xlabel("The number of water samples")
    plt.ylabel(target)
    plt.text(20, 37, "RMSE: %.4f" % sum_erro)
    plt.show()


# define base model
def baseline_model(length):
    # create model
    model = Sequential()
    model.add(Dense(20, input_dim=length, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')
    return model


def backPropagation(data, target):
    pass


def extremLM(data, target, checkHiddenPoints, fileName):  # Extreme Learning Machine
    scalar = 10000
    X = data.iloc[:, :-1]
    X_norm = (X - X.mean()) / (X.max() - X.min())
    y = data[target]
    # y_int = y.apply(lambda x: x * scalar)  # Need to be fixed!
    y_int = y * scalar
    y_int = y_int.apply(np.int64)
    # print(y_int)
    elmList = []
    if checkHiddenPoints:
        inter_num = 100
        hiddenNum = [1000, 3000, 5000, 6000, 8000, 10000]  # number of hidden points in ELM
        errorList = []
        for hidNum in hiddenNum:
            total_error = 0
            for i in range(inter_num):
                X_train, X_test, y_train, y_test = train_test_split(X_norm, y_int, test_size=0.2)
                elm = ELM(hid_num=hidNum).fit(X_train, y_train)
                y_pred = elm.predict(X_test)
                sum_mean = 0
                # print("This is test value:", y_test.values)
                # print("This is prediction values:", y_pred)
                for i in range(len(y_pred)):
                    sum_mean += (y_pred[i] - y_test.values[i]) ** 2
                sum_erro = (np.sqrt(sum_mean / len(y_pred))) / scalar
                # calculate RMSE
                total_error = total_error + sum_erro
                print("RMSE:", sum_erro)  # Root Mean Squared Error, RMSE
            print("This is average RMSE for ELM:", total_error / inter_num)
            errorList.append(total_error / inter_num)
        # Plot
        x_pos = list(range(len(hiddenNum)))
        plt.bar(x_pos, errorList, align='center', alpha=0.5)
        plt.grid()
        plt.ylabel('Root Mean Squared Error')
        plt.xticks(x_pos, hiddenNum)
        plt.title('Different errors based on the number of hidden points')
        plt.show()
    else:
        for j in range(100):
            X_train, X_test, y_train, y_test = train_test_split(X_norm, y_int, test_size=0.2)
            elm = ELM(hid_num=6000).fit(X_train, y_train)
            y_pred = elm.predict(X_test)
            sum_mean = 0
            # print("This is test value:", y_test.values / scalar)
            print("This is prediction values:", y_pred / scalar)
            print("This is iteration number: ",j)
            for i in range(len(y_pred)):
                sum_mean += (y_pred[i] - y_test.values[i]) ** 2
            sum_erro = (np.sqrt(sum_mean / len(y_pred))) / scalar
            elmList.append(sum_erro)
        return elmList


        # calculate RMSE
        # print("RMSE:", sum_erro)  # Root Mean Squared Error, RMSE
        # end = time.time()
        # print("Time: ", (end - start))
        # plt.figure('ELM model')
        # plt.plot(range(len(y_pred)), y_pred / scalar, 'b', label="predict")
        # plt.plot(range(len(y_pred)), y_test / scalar, 'r', label="test")
        # plt.legend(loc="upper right")  # show the lable
        # plt.xlabel("The number of water samples")
        # plt.ylabel(target)
        # plt.text(len(y_pred) / 2, (max(y_test.values)) / scalar + 3, "RMSE: %.4f" % sum_erro)
        # plt.show()

def hpELM(data, target):  # new ELM method for multi output


    # print("This is train data input : ", X_train)
    # print("This is train data output: ", T_train)
    # print("This is test data input: ", X_test)
    # print("This is test data output: ", T_test)

    # print("This is predict value: ", T_pred)
    # print("This is real value: ", T_test)

    # print("This is length of output: ", len(T_pred))
    elmList = []
    for j in range(100):
        X_train, X_test, T_train, T_test = train_test_split(data, target, test_size=0.2)
        elm = hpelm.ELM(data.shape[1], target.shape[1])  # number of data features /  number of classes
        elm.add_neurons(5000, "sigm")
        elm.train(X_train, T_train, 'r')
        T_pred = elm.predict(X_test)
        print("This is error: ", elm.error(T_test, T_pred))
        sum_mean = 0
        T_pred_List = []
        T_test_List = []
        for x in np.nditer(T_pred):
            T_pred_List.append(x)
        for y in np.nditer(T_test):
            T_test_List.append(y)
        for i in range(len(T_pred_List)):
            sum_mean += (T_pred_List[i] - T_test_List[i]) ** 2
        sum_erro = (np.sqrt(sum_mean / len(T_pred_List)))
        elmList.append(sum_erro)
    return elmList

def randomForest(data, target):
    X = data.iloc[:, :-1]
    X_norm = (X - X.mean()) / (X.max() - X.min())
    y = data[target]
    max_depth = 30
    rfList = []
    for j in range(100):
        X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
        regr_rf = RandomForestRegressor(max_depth=max_depth, random_state=1)
        regr_rf.fit(X_train, y_train)
        # Predict on new data
        y_pred = regr_rf.predict(X_test)
        # print("This is test value:", y_test.values)
        # print("This is prediction values:", y_pred)
        sum_mean = 0
        for i in range(len(y_pred)):
            sum_mean += (y_pred[i] - y_test.values[i]) ** 2
        sum_erro = np.sqrt(sum_mean / len(y_pred))
        rfList.append(sum_erro)
    return rfList
    # calculate RMSE
    # print("RMSE:", sum_erro)  # Root Mean Squared Error, RMSE
    #
    # end = time.time()
    # print("Time: ", (end - start))
    # plt.figure('Random Forest model')
    # plt.plot(range(len(y_pred)), y_pred, 'b', label="predict")
    # plt.plot(range(len(y_pred)), y_test, 'r', label="test")
    # plt.legend(loc="upper right")  # show the lable
    # plt.xlabel("The number of water samples")
    # plt.ylabel(target)
    # plt.text(20, 37, "RMSE: %.4f" % sum_erro)
    # plt.show()


if __name__ == '__main__':
    start = time.time()
    funcNum = 3
    # target = 'Temperature'
    # target = 'NO3'
    target = "salinity"
    # if not os.path.isfile('OTU_Transpose_%s.xlsx' % target):
    #     trainData = buildDataForMultiLineReg(target)
    # else:
    #     trainData = pd.read_excel('OTU_Transpose_%s.xlsx' % target)
    # if funcNum == 1:
    #     print("Mult factor algorithm is running...")
    #     drawMultiRegre(trainData, target)
    # elif funcNum == 2:
    #     print("Back propagation algorithm is running...")
    #     backPropagation(trainData, target)
    # elif funcNum == 3:
    #     print("ELM algorithm is running...")
    #     extremLM(trainData, target, True)
    # elif funcNum == 4:
    #     print("Random Forest algorithm is running...")
    #     randomForest(trainData, target)
    dataFile = [970, 965, 950]
    # dataFile = [975]
    fillByKnn = pd.read_excel('FillByKnn.xlsx')
    lableList = []
    finalErrorELM = []
    finalErrorRF = []
    for fileName in dataFile:
        lableList += 100 * [str(fileName / 1000)]
        print(lableList)
        errorELM = []
        errorRF = []
        trainData = pd.read_excel('OTU_Transpose_by_ratio_%d.xlsx' % fileName)
        subCol = fillByKnn.loc[:, target]
        # print("This is subcol:",subCol)
        trainData[target] = subCol.values  # this data will be used to test the efficiency of ELM and RF
        # print("This is trainData:",trainData)

        # hpelm
        # fillByKnnhp = pd.read_excel('FillByKnn1.xlsx')
        # trainData_matrix = trainData.as_matrix()
        # fillByKnn1 = fillByKnnhp.iloc[:, 1:]
        # parameterMatrix = fillByKnn1.as_matrix()  # Problem: normalization or not?
        # trainData_matrix = scale_linear_bycolumn(trainData_matrix)  # Normalization the input data
        # errorELM = hpELM(trainData_matrix, parameterMatrix)


        errorELM = extremLM(trainData, target, False, fileName)
        print("This is elm error: ", errorELM)
        print("ELM Part %d DONE!" % (dataFile.index(fileName)+1))
        finalErrorELM.extend(errorELM)
        errorRF = randomForest(trainData, target)
        print("This is rf error: ", errorRF)
        print("RF Part %d DONE!" % (dataFile.index(fileName)+1))
        finalErrorRF.extend(errorRF)
    end = time.time()
    print("Time: ", (end - start))
    print("This is final ELM error list: ", finalErrorELM)
    trace1 = {
        "x": lableList,
        "y": finalErrorELM,
        "line": {"color": "rgba(102,194,165,1)"},
        "name": "ELM",
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
        "title": "The reliability of ELM and Random Forest",
        "xaxis": {
            "categoryarray": ["0.99", "0.985", "0.98", "0.975"],
            "categoryorder": "array",
            "domain": [0, 1],
            "title": "bin",
            "type": "category"
        },
        "yaxis": {
            "domain": [0, 1],
            "title": "RMSE-Root mean square error"
        }
    }
    fig = Figure(data=data, layout=layout)
    plot_url = py.plot(fig)
