from sklearn import decomposition

import plotly.plotly as py
import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np
import xlwt
import matplotlib.pyplot as plt

df = pd.read_excel('NumberNullWithNull.xlsx')
# print(df.head())
df = df.dropna()
# print(df.columns)
parameterList = np.array(df[['salinity', 'Depth', 'Temperature', 'O2', 'PO4', 'SiO2', 'NO2',
                             'NO3', 'Tbact', 'Synechococcus', 'Latitude', 'Longitude']])

# print(parameterList)
sc = StandardScaler()
paraStand = sc.fit_transform(parameterList)
# print(paraStand)
pca = decomposition.PCA()  # n_compenent = 12
paraStand_pca = pca.fit_transform(paraStand)
# print(paraStand_pca)
cov_1 = np.cov(paraStand_pca.T)
# print(cov_1.shape)
eigen_val, eigen_vecs = np.linalg.eig(cov_1)
print('EigenValue：{}\nEigenVectors：{}'.format(eigen_val,eigen_vecs))
# print(w)
# print(paraStand_pca)
# workbook = xlwt.Workbook()
# sheet1 = workbook.add_sheet('sheet1')
# for row,array in enumerate(v):
#     for col,value in enumerate(array):
#         sheet1.write(row,col,value)
# name = 'PCA.xls'
# workbook.save(name)
tot = sum(eigen_val)
var_exp = [(i / tot) for i in sorted(eigen_val, reverse=True)]
# print(var_exp)
cum_var_exp = np.cumsum(var_exp)

plt.bar(range(len(eigen_val)), var_exp, width=1, bottom=0, alpha=1, label='individual explained variance')
plt.step(range(len(eigen_val)), cum_var_exp, where='mid', label='cumulative explained variance')
plt.ylabel('Explained variance ratio')
plt.xlabel('Principal components')
plt.legend(loc='best')
plt.show()
