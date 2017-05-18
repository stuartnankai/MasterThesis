import plotly.plotly as py
import pandas as pd

df = pd.read_excel('NumberNullWithNull.xlsx')
dfWithNull = df.iloc[:,1:8]
# print(dfWithNull)
df2 = pd.DataFrame()

# for i in dfWithNull.index:
#     if(dfWithNull.ix[i]).isnull().any():
#         print(dfWithNull.ix[i])
#         dfWithNull.drop(i,inplace = True)
# print(df2)
# tempdf = dfWithNull.iloc[:,1:4]

# separate the data into two parts, one has NOT Null and on has Null
for index, row in dfWithNull.iterrows():
    if(dfWithNull.loc[index].isnull().any()):
        df2 = df2.append(row,ignore_index=True)
        dfWithNull.drop(index, inplace=True)
tempdf = dfWithNull.iloc[:,0:3]
# print(tempdf)
tempdfWithNull = df2[['salinity','Depth','Temperature']]

tempdf.to_csv('temp.csv',encoding='utf-8')
data = pd.read_csv('temp.csv')
data.head()

tempdfWithNull.to_csv('tempNull.csv',encoding='utf-8')
data1 = pd.read_csv('tempNull.csv')
data1.head()
#
scatter = dict(
    mode = "markers",
    name = "Normal Data",
    type = "scatter3d",
    x = data['salinity'], y = data['Depth'], z = data['Temperature'],
    marker = dict( size=2, color="rgb(23, 190, 207)" )
)
scatter1 =dict(
    mode = "markers",
    name = "Null Data",
    type = "scatter3d",
    x = data1['salinity'], y = data1['Depth'], z = data1['Temperature'],
    marker = dict( size=2, color="rgb(246, 70, 91)" )
)
clusters = dict(
    alphahull = 7,
    name = "y",
    opacity = 0.1,
    type = "mesh3d",
    x=data['salinity'], y=data['Depth'], z=data['Temperature']
)
layout = dict(
    title = '3d point clustering',
    scene = dict(
        xaxis = dict( zeroline=False ),
        yaxis = dict( zeroline=False ),
        zaxis = dict( zeroline=False ),
    )
)
fig = dict(data=[scatter, scatter1,clusters], layout=layout)
# Use py.iplot() for IPython notebook
py.plot(fig, filename='3d point clustering')