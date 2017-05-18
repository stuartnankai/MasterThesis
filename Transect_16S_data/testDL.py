# Use scikit-learn to grid search the batch size and epochs
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.constraints import maxnorm
from keras.wrappers.scikit_learn import KerasRegressor


# Function to create model, required for KerasR
def create_model(optimizer='rmsprop', init='glorot_uniform'):
    inputDim = 4
    # create model
    model = Sequential()
    model.add(Dense(300, input_dim=inputDim, kernel_initializer=init, activation='relu'))
    # model.add(Dense(250, kernel_initializer=init, activation='relu'))
    # model.add(Dense(200, kernel_initializer=init, activation='relu'))
    model.add(Dense(150, kernel_initializer=init, activation='relu'))
    # model.add(Dense(100, kernel_initializer=init, activation='relu'))
    # model.add(Dense(50, kernel_initializer=init, activation='relu'))
    # model.add(Dense(30, kernel_initializer=init, activation='relu'))
    # model.add(Dense(50, kernel_initializer=init, activation='relu'))
    model.add(Dense(15, kernel_initializer=init, activation='relu'))
    # model.add(Dense(10, kernel_initializer=init, activation='relu'))
    model.add(Dense(1, kernel_initializer=init, activation='relu'))
    # Compile model
    model.compile(loss='mse', optimizer=optimizer, metrics=['accuracy'])
    return model


def larger_model():
    inputDim = 39
    # create model
    model = Sequential()

    model.add(Dense(inputDim*5, input_dim=inputDim, activation='relu'))
    # model.add(Dense(int(inputDim * 0.5), activation='relu'))
    # model.add(Dense(int(inputDim * 0.25), activation='relu'))
    model.add(Dense(1))

    # model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    # model.compile(loss='mean_squared_error', optimizer='adam')
    model.compile(optimizer='rmsprop',
                  loss='mse', metrics=['accuracy'])
    print(" Larger Model construction.......DONE!")
    return model


# Function to create model, required for KerasClassifier
def create_model_neurons(neurons=100):
    # create model
    model = Sequential()
    model.add(
        Dense(neurons, input_dim=113, kernel_initializer='uniform', activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(1, kernel_initializer='uniform', activation='relu'))
    # Compile model
    model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
    return model


# Function to create model, required for KerasR----activation
def create_model_activation(activation='relu'):
    # create model
    model = Sequential()
    model.add(Dense(300, input_dim=39, kernel_initializer='uniform', activation=activation))
    model.add(Dense(250, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(200, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(150, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(100, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(50, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(25, kernel_initializer='uniform', activation='relu'))
    model.add(Dense(1, kernel_initializer='uniform', activation='relu'))
    # Compile model
    model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
    return model




# print("This is X_train : ", X_train)
# print("This is y_train: ", y_train)


def buildDeepLearning(data, target, iteraNum, funNum):
    # global kerasModel
    X_norm = data
    # print("This is X_norm: ", X_norm)
    y = target
    # print("This is target : ", y)
    tempDim = len(X_norm[0])
    kerasList = []
    scaleList = [0.5,0.8,1,1.5,2]
    print("This is input dimension: ", tempDim)
    for j in range(iteraNum):
        X_train, X_test, y_train, y_test = train_test_split(X_norm, y, test_size=0.2)
        # print("This is X_train: ", X_train)
        # print("This is y_train: ", y_train)
        # define the grid search parameters
        neurons = [int(i*tempDim) for i in scaleList]

        param_grid = dict(neurons=neurons)
        print("This is DL training process.........")
        model = KerasRegressor(build_fn=create_model_neurons, verbose=0, epochs=100, batch_size=5)
        # model = KerasRegressor(build_fn=larger_model, verbose=0, epochs=100, batch_size=5)
        grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=1, cv=5)
        newModel = grid.fit(X_train, y_train)
        print("Best: %f using %s" % (newModel.best_score_, newModel.best_params_))
        y_pred = newModel.predict(X_test).tolist()
        # print("This is y_pred: ", y_pred)
        for n in range(len(y_pred)):
            print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test[n], y_pred[n]))
        sum_erro = np.sqrt(mean_squared_error(y_test, y_pred))
        print("This is : sum_erro ", sum_erro)
        print("This is iteration number: ", j + 1)
        kerasList.append(sum_erro)
    return kerasList

if __name__ == '__main__':
    # load dataset and 0-1 normalization
    fileName = 600
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    # trainData = pd.read_excel(
    #     './Training Data/newWaterSamples_%d.xlsx' % fileName)
    trainData = pd.read_excel(
        './Training Data/easy_get_para.xlsx')
    subCol = fillByKnn.loc[:, 'salinity']

    normalized_trainData = preprocessing.MinMaxScaler().fit_transform(trainData)

    print("This is NORM: ", normalized_trainData)
    inputDim = len(normalized_trainData[0])
    print("This is inputDim: ", inputDim)

    X_train, X_test, y_train, y_test = train_test_split(normalized_trainData, subCol.as_matrix(), test_size=0.2)

# define the grid search parameters
# grid search epochs, batch size and optimizer
# optimizers = ['rmsprop', 'adam']
# init = ['glorot_uniform', 'normal', 'uniform']
# epochs = [200, 250,300]  # bigger
# batches = [2, 4, 8, 20]  # smaller
# param_grid = dict(optimizer=optimizers, epochs=epochs, batch_size=batches, init=init)
# # create model
# model = KerasRegressor(build_fn=create_model, verbose=0)
# grid = GridSearchCV(estimator=model,param_grid=param_grid,n_jobs=-1)

# define the grid search parameters
# batch_size = [40, 60, 80, 100,150,200,250]
# epochs = [50, 100,150,200,250]
# param_grid = dict(batch_size=batch_size, epochs=epochs)
# model = KerasRegressor(build_fn=create_model, verbose=0)
# grid = GridSearchCV(estimator=model,param_grid=param_grid,n_jobs=-1)

# define the grid search parameters 1
# neurons = [250, 260, 270, 280, 290, 300]
# param_grid = dict(neurons=neurons)
# model = KerasRegressor(build_fn=create_model_neurons, verbose=0, epochs=100, batch_size=5)
# grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)

# define the grid search parameters 2
# # define the grid search parameters
# activation = ['softmax', 'softplus', 'softsign', 'relu', 'tanh', 'sigmoid', 'hard_sigmoid', 'linear']
# model = KerasRegressor(build_fn=create_model_activation, epochs=100, batch_size=10, verbose=0)
# param_grid = dict(activation=activation)
# grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=-1)


# grid_result = grid.fit(X, Y)
# grid_result = grid.fit(X_train, y_train)
# summarize results
# print("Best: %f using %s" % (grid_result.best_score_, grid_result.best_params_))
# means = grid_result.cv_results_['mean_test_score']
# stds = grid_result.cv_results_['std_test_score']
# params = grid_result.cv_results_['params']
# for mean, stdev, param in zip(means, stds, params):
#     print("%f (%f) with: %r" % (mean, stdev, param))

# y_pred = grid_result.predict(X_test)
# print("This is y_test: ", y_test)
# print("This is y_pred: ", y_pred)
#
# for n in range(len(y_pred)):
#     print("This is REAL value %.4f, ===========> PRED value: %.4f" % (y_test[n], y_pred[n]))
#
# sum_erro = np.sqrt(mean_squared_error(y_test, y_pred))
#
# print("This is  sum_error: ", sum_erro)
