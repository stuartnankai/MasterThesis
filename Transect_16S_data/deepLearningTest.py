import numpy as np
import pandas as pd
from sklearn.grid_search import GridSearchCV
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import plotly.plotly as py
import matplotlib.pyplot as plt

# py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')

# define the models and configure the learning process
def baseline_model(inputDim):
    # create model
    model = Sequential()
    model.add(Dense(inputDim, input_dim=inputDim, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    # model.compile(loss='mean_squared_error', optimizer='adam')
    model.compile(optimizer='rmsprop',
                  loss='mse')
    print(" Base Line Model construction.......DONE!")
    return model


# define wider model
def wider_model(inputDim, scalarNum):
    # create model
    model = Sequential()
    # model.add(Dense(inputDim * scalarNum, input_dim=inputDim, kernel_initializer='normal', activation='relu'))
    model.add(Dense(inputDim * scalarNum, input_dim=inputDim, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    # model.compile(loss='mean_squared_error', optimizer='adam')
    # For a mean squared error regression problem
    model.compile(optimizer='rmsprop',
                  loss='mse')
    print(" Wider Model construction.......DONE!")
    return model


# define the model
def larger_model():
    # inputDim = 39
    inputDim = 109
    # create model
    model = Sequential()

    # Use uniform

    # model.add(Dense(inputDim, input_dim=inputDim, kernel_initializer='uniform', activation='relu'))
    # model.add(Dense(int(inputDim*0.8), kernel_initializer='uniform', activation='relu'))
    # model.add(Dense(int(inputDim*0.5), kernel_initializer='uniform', activation='relu'))
    # model.add(Dense(int(inputDim*0.25), kernel_initializer='uniform', activation='relu'))
    # # model.add(Dense(int(inputDim*0.15), kernel_initializer='uniform', activation='relu'))
    # model.add(Dense(1, kernel_initializer='uniform'))

    # Use normal

    # model.add(Dense(int(inputDim*1.5), input_dim=inputDim, kernel_initializer='normal', activation='relu'))
    # # model.add(Dense(int(inputDim * 0.8), kernel_initializer='normal', activation='relu'))
    # model.add(Dense(int(inputDim * 0.5), kernel_initializer='normal', activation='relu'))
    # model.add(Dense(int(inputDim * 0.25), kernel_initializer='normal', activation='relu'))
    # # model.add(Dense(int(inputDim * 0.15), kernel_initializer='normal', activation='relu'))
    # model.add(Dense(1, kernel_initializer='normal'))

    model.add(Dense(int(inputDim * 1.5), input_dim=inputDim, activation='relu'))
    model.add(Dense(int(inputDim * 0.8), activation='relu'))
    model.add(Dense(int(inputDim * 0.5), activation='relu'))
    model.add(Dense(int(inputDim * 0.25), activation='relu'))
    model.add(Dense(int(inputDim * 0.15),  activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform'))

    # Use None


    # model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    # model.compile(loss='mean_squared_error', optimizer='adam')
    model.compile(optimizer='rmsprop',
                  loss='mse')
    print(" Larger Model construction.......DONE!")
    return model


def deepLearning(data, target, iteraNum, funNum):
    # load dataset
    global kerasModel
    X_norm = data
    print("This is X_norm: ", X_norm)
    y = target
    print("This is target : ", y)
    tempDim = len(X_norm[0])
    print("This is input dimension: ", tempDim)

    kerasList = []
    batch_size = [50, 100, 150, 200]
    epochs = [10, 20, 30, 50, 80]
    inputDim = [tempDim]
    # neurons = [40,50,60,100,200]
    param_grid = dict(batch_size=batch_size, nb_epoch=epochs,input_dim = inputDim)

    if funNum == 1:
        kerasModel = KerasRegressor(build_fn=baseline_model, verbose=0)
    elif funNum == 2:
        kerasModel = KerasRegressor(build_fn=wider_model, verbose=0)
    elif funNum == 3:
        kerasModel = KerasRegressor(build_fn=larger_model, verbose=0)

    for j in range(iteraNum):
        X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
        print("This is X_train: ", X_train)
        print("This is y_train: ", y_train)
        grid = GridSearchCV(estimator=kerasModel, cv=5, param_grid=param_grid)
        newModel = grid.fit(X_train, y_train)
        print("Best: %f using %s" % (newModel.best_score_, newModel.best_params_))
        y_pred = newModel.predict(X_test).tolist()
        print("This is y_pred: ", y_pred)
        sum_mean = 0
        y_test_list = y_test.tolist()
        print("This is y_test_list: ", y_test_list)
        # for n in range(len(y_pred)):
        #     print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test_list[n], y_pred[n]))
        #     # sum_mean += (y_pred[n] - y_test[n]) ** 2
        #     sum_mean += (float("{0:.4f}".format(float(y_pred[n]))) - y_test_list[n]) ** 2
        # sum_erro = np.sqrt(sum_mean / len(y_pred))
        #
        # print("This is sum_erro: ", sum_erro)
        sum_erro = np.sqrt(mean_squared_error(y_test_list, y_pred))
        print("This is : sum_erro ", sum_erro)
        print("This is iteration number: ", j + 1)
        kerasList.append(sum_erro)
    # # Train the model, iterating on the data in batches of n(32/64/128) samples
    # for j in range(iteraNum):
    #     X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
    #     if funNum == 1:
    #         kerasModel = KerasRegressor(build_fn=baseline_model(inputDim), verbose=0)
    #         grid = GridSearchCV(estimator=kerasModel, param_grid=param_grid, n_jobs=1)
    #         bestDLModel = grid.fit(X_train, y_train)
    #         print("Best: %f using %s" % (bestDLModel.best_score_, bestDLModel.best_params_))
    #         y_pred = bestDLModel.predict(X_test)
    #
    #         # kerasModel = baseline_model(inputDim)
    #         # kerasModel.fit(X_train, y_train, epochs=200, batch_size=128)
    #         # y_pred = kerasModel.predict(X_test)
    #         sum_mean = 0
    #         for n in range(len(y_pred)):
    #             print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test[n], y_pred[n]))
    #             sum_mean += (float("{0:.4f}".format(float(y_pred[n]))) - y_test[n]) ** 2
    #         sum_erro = np.sqrt(sum_mean / len(y_pred))
    #         print("This is sum_erro: ", sum_erro)
    #         print("This is iteration number: ", j + 1)
    #         kerasList.append(sum_erro)
    #         # plotFigure(y_pred, y_test, sum_erro[0])
    #     elif funNum == 2:
    #         # kerasModel = wider_model(inputDim, 2)
    #         # kerasModel.fit(X_train, y_train, epochs=100, batch_size=scalar, shuffle=True)
    #         # y_pred = kerasModel.predict(X_test)
    #         kerasModel = KerasRegressor(build_fn=wider_model(inputDim), verbose=0)
    #         grid = GridSearchCV(estimator=kerasModel, param_grid=param_grid, n_jobs=1)
    #         bestDLModel = grid.fit(X_train, y_train)
    #         print("Best: %f using %s" % (bestDLModel.best_score_, bestDLModel.best_params_))
    #         y_pred = bestDLModel.predict(X_test)
    #
    #         sum_mean = 0
    #         for n in range(len(y_pred)):
    #             print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test[n], y_pred[n]))
    #             sum_mean += (float("{0:.4f}".format(float(y_pred[n]))) - y_test[n]) ** 2
    #         sum_erro = np.sqrt(sum_mean / len(y_pred))
    #         print("This is sum_erro: ", sum_erro)
    #         print("This is iteration number: ", j + 1)
    #         kerasList.append(sum_erro)
    #         # plotFigure(y_pred,y_test,sum_erro[0])
    #     elif funNum == 3:
    #
    #         # kerasModel = larger_model(inputDim)
    #         # kerasModel.fit(X_train, y_train, epochs=100, batch_size=scalar, shuffle=True)
    #
    #         kerasModel = KerasRegressor(build_fn=larger_model(inputDim), verbose=0)
    #         grid = GridSearchCV(estimator=kerasModel, cv=5,param_grid=param_grid)
    #         grid.fit(X_train, y_train)
    #         print("Best: %f using %s" % (grid.best_score_, grid.best_params_))
    #         y_pred = grid.predict(X_test)
    #         sum_mean = 0
    #         for n in range(len(y_pred)):
    #             print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test[n], y_pred[n]))
    #             # sum_mean += (y_pred[n] - y_test[n]) ** 2
    #             sum_mean += (float("{0:.4f}".format(float(y_pred[n]))) - y_test[n]) ** 2
    #         sum_erro = np.sqrt(sum_mean / len(y_pred))
    #         print("This is sum_erro: ", sum_erro)
    #         print("This is iteration number: ", j + 1)
    #         kerasList.append(sum_erro)
    #         # plotFigure(y_pred, y_test, sum_erro)
    return kerasList


def plotFigure(y_pred, y_test, sum_error):
    # Plot the figure
    plt.figure('Deep learning model')
    plt.plot(range(len(y_pred)), y_pred, 'b', label="predict")
    plt.plot(range(len(y_test)), y_test, 'r', label="test")
    plt.legend(loc="upper right")  # show the lable
    plt.xlabel("The number of water samples")
    plt.ylabel("Real values")
    plt.text(len(y_pred) / 2, (max(y_test)) + 3, "RMSE: %.4f" % sum_error)
    plt.show()


def plotCompare(x, y):
    # N = len(y)
    # width = 1 / 2
    # plt.bar(x, y, width, color="blue")
    # fig = plt.gcf()
    # plot_url = py.plot_mpl(fig, filename='mpl-basic-bar')

    objects = x
    y_pos = np.arange(len(objects))
    performance = y
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('RMSE')
    plt.title('The file size')
    plt.show()


if __name__ == '__main__':

    targetList = ['salinity']
    iteraNum = 10
    funNum = 3  # model for deeplearning
    errorList = []
    isNormal = False
    # fillByKnn = pd.read_excel('./Training Data/FillByKnn.xlsx')
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    subCol = fillByKnn.loc[:, targetList[0]]
    if isNormal:
        subCol = preprocessing.MinMaxScaler().fit_transform(subCol)
    fileSize = [750]  # input Dim = 39
    for j in fileSize:
        # trainData = pd.read_excel(
        #     './Training Data/newWaterSamples_%d.xlsx' % j)
        trainData = pd.read_excel(
            './Training Data/easy_get_para.xlsx')
        normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)  # 3
        # tempdata = deepLearning(normalized_trainData, subCol, iteraNum, funNum)
        # tempdata = deepLearning(normalized_trainData, subCol.as_matrix(), iteraNum, funNum)
        tempdata = deepLearning(normalized_trainData, subCol.as_matrix(), iteraNum, funNum)
        print("This is error list: ", tempdata)
        meanError = sum(tempdata) / float(len(tempdata))
        print("This is mean error: ", meanError)
        errorList.append(meanError)
    plotCompare(fileSize, errorList)
