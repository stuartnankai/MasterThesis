import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler



def plotCumulative(X_train_std):

    cov_mat = np.cov(X_train_std.T)

    eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)

    print("This is eigen_vals: ", eigen_vals )

    tot = sum(eigen_vals)

    var_exp = [(i/tot) for i in sorted(eigen_vals,reverse=True)]
    cum_val_exp = np.cumsum(var_exp)

    plt.bar(range(1,len(X_train_std[1])+1),var_exp,alpha=0.5,align= 'center',label='individual explained variance')
    plt.step(range(1,len(X_train_std[1])+1),cum_val_exp,where='mid',label='cumulative explained varience')
    plt.ylabel("Explained variance ration")
    plt.xlabel('Principal components')
    plt.legend(loc='best')
    plt.show()



if __name__ == '__main__':

    fileName = 'NO3'
    targetList = ['NO3']
    typeTrainDB = 6
    df_pca = pd.read_excel('../Training Data/easy_get_para.xlsx')
    fillByKnn = pd.read_excel('../Training Data/WaterSamplesNoNull.xlsx')

    print("This is : ", df_pca)

    subCol = fillByKnn.loc[:, fileName]

    print("This is : ",subCol )

    X = df_pca.values
    y = subCol

    X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.1,random_state=0)

    sc = StandardScaler()
    X_train_std = sc.fit_transform(X_train)
    X_test_std = sc.transform(X_test)

    print("This is : ", X_test_std )

    plotCumulative(X_train_std)