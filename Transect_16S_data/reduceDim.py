import time
import pandas as pd
import numpy as np
# import mrmr
import pymrmr

from sklearn import decomposition, preprocessing
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


def featureExtraction(trainData, testData, numFeature):
    print("PCA is running....")
    # print("This is features: ", feature )
    # print("This is array: ", data.as_matrix() )

    # automatic pick the features by using mle
    # X_std = data
    # # print("This is X_std: ", X_std )
    # pca = decomposition.PCA(n_components=numFeature)
    # X_std_pca = pca.fit_transform(X_std)
    pca = decomposition.PCA(n_components=numFeature)
    X_train_pca = pca.fit_transform(trainData)
    X_test_pca = pca.transform(testData)
    numPCA = len(pca.explained_variance_ratio_)
    print("This is the ratio of features", pca.explained_variance_ratio_)
    # print ("This is the variance of features", pca.explained_variance_)
    # print("This is X_train pca: ", len(X_train_pca) )
    # print("This is X_test pca: ", len(X_test_pca))

    # print("This is shape: ",X_std_pca )
    # print ("Extracting the top eigenfaces from %d OTUs" %
    #                        trainData.shape[0])
    #                 print("This is features: ", trainData.columns)
    #                 X_feature = np.array(trainData.columns)
    #                 print("This is X_feature shape: ", X_feature.shape )
    print("PCA DONE!!!!!!")
    return X_train_pca, X_test_pca


def featureSelection(data, numFeature):  # mrmr
    featureList = pymrmr.mRMR(data, 'MIQ', numFeature)
    print("This is selected features: ", featureList)
    return featureList


def buildInputData(fileName, targetList, needNormalized):  # Use easy get parameters
    sc = preprocessing.StandardScaler()
    fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    subCol = fillByKnn.loc[:, targetList[0]]
    df = pd.read_excel('./Training Data/newWaterSamples_%d_easy_get.xlsx' % fileName)
    if needNormalized:
        tempIndex = df.columns.tolist()
        df_std = sc.fit_transform(df)
        # print("This is : ", df_std)
        tempDf = pd.DataFrame(df_std)
        tempDf.columns = tempIndex
        print("This is new df: ", tempDf)
    else:
        tempDf = df
    tempDf[targetList[0]] = subCol.values
    cols = tempDf.columns.tolist()
    cols = cols[-1:] + cols[:-1]
    newDf = tempDf[cols]
    # print("This is : ", newDf)
    newDf.to_csv('./Training Data/newWaterSamples_%d_noHeader.csv' % fileName, index=False)
    return pd.read_csv('./Training Data/newWaterSamples_%d_noHeader.csv' % fileName)


if __name__ == '__main__':
    fileName = 950
    numFeature = 10
    targetList = ['NO3']
    needNormalized = False
    # fillByKnn = pd.read_excel('./Training Data/WaterSamplesNoNull.xlsx')
    # subCol = fillByKnn.loc[:, targetList[0]]
    df = buildInputData(fileName, targetList, needNormalized)
    print("This is : ", df)

    # trainData = pd.read_excel(
    #     './Training Data/newWaterSamples_%d.xlsx' % fileName)
    # temp = featureExtraction(trainData,10)
    #
    # print("This is X_std: ", temp )
    # print("This is : ", df)
    # df = pd.read_csv('out.csv')
    # df = pd.read_csv('./Training Data/newWaterSamples_%d_noHeader.csv' % fileName)
    featureList = featureSelection(df, numFeature)
    print("This is selected features: ", featureList)
