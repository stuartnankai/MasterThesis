#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 13:17:27 2017
Using BP algorithm

@author: sunjian
"""

import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
import time

# # load dataset
start = time.time()
trainData = pd.read_excel('OTU_Transpose_Salinity.xlsx')
dataset1 = trainData.values

X = dataset1[:, 0:-1]
X_norm = (X - X.mean()) / (X.max() - X.min()) # Normalization
# print("This is X: ",X)
Y = dataset1[:, -1]
# print("This is Y: ",Y)
X_train, X_test, y_train, y_test = train_test_split(X_norm, Y, random_state=1)


# define base model
def baseline_model():
    # create model
    model = Sequential()
    model.add(Dense(5607, input_dim=5607, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(2800, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(1400, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(700, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(350, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(140, kernel_initializer='normal', activation='relu'))
    # model.add(Dense(48, kernel_initializer='normal', activation='relu'))
    model.add(Dense(10, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal'))
    # Compile model
    model.compile(loss='mean_squared_error', optimizer='adam')

    return model


# model = baseline_model()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print("This is prediction: ", y_pred)
# print("This is real salinity: ",y_test)
#


# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
# evaluate model with standardized dataset


estimator = KerasRegressor(build_fn=baseline_model, nb_epoch=100, batch_size=5, verbose=0)
estimator.fit(X_train, y_train)
y_pred = estimator.predict(X_test)
print("This is prediction: ", y_pred)

sum_mean = 0
for i in range(len(y_pred)):
    sum_mean += (y_pred[i] - y_test[i]) ** 2
sum_erro = np.sqrt(sum_mean / len(y_pred))
# calculate RMSE
print("RMSE:", sum_erro)  # Root Mean Squared Error, RMSE
end = time.time()
print("Total time: ", (end - start))

plt.figure('Backpropagation regression model')
plt.plot(range(len(y_pred)), y_pred, 'b', label="predict")
plt.plot(range(len(y_pred)), y_test, 'r', label="test")
plt.legend(loc="upper right")  # show the lable
plt.xlabel("The number of water samples")
plt.ylabel('Salinity')
plt.show()

