import time
import pandas as pd
from sklearn import preprocessing
import os.path
import numpy as np


def prepareFile(ratio):
    df = pd.read_excel('./Training Data/OTUremove_by_ratio_%d.xls' % ratio)
    df = df.drop(df.columns[1], axis=1)  # drop the class column
    df = df.set_index('ID').T  # transpose the row and column
    # print(df)
    writer = pd.ExcelWriter('./Training Data/OTU_Transpose_by_ratio_%d.xlsx' % ratio)
    df.to_excel(writer, 'sheet1')
    writer.save()
    return df


if __name__ == '__main__':
    start = time.time()
    ratio = 960
    # creat the testing file
    if not os.path.isfile('./Training Data/OTU_Transpose_by_ratio_%d.xlsx' % ratio):
        df = prepareFile(ratio)
    else:
        df = pd.read_excel('./Training Data/OTU_Transpose_by_ratio_%d.xlsx' % ratio)
    paraList = ['salinity', 'Depth', 'Temperature', 'O2', 'PO4', 'SiO2', 'NO2', 'NO3']
    # paraList = ['salinity']
    fillByKnn = pd.read_excel('./Training Data/FillByKnn.xlsx')
    for i in paraList:
        subCol = fillByKnn.loc[:, i]
        # print('This is original value:', subCol)
        min_max_scaler = preprocessing.MinMaxScaler(feature_range=(0, 1))
        data_scaled = min_max_scaler.fit_transform(subCol)
        # print('This is normalized value:', data_scaled)
        df[i] = data_scaled
    writer = pd.ExcelWriter('./Training Data/OTU_Transpose_by_ratio_%d_withParas.xlsx' % ratio)
    df.to_excel(writer, 'sheet1')
    writer.save()
    # dataFile = [990,985,980,975]
    # end = time.time()
    # print("Time: ", (end - start))