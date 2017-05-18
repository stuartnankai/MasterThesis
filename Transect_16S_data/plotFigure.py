import pandas as pd
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *

# py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')

fileName = 'salinity'
typeTrainDB = 2

figureTitle = ''  # df = pd.read_excel('./Training Data/remoteResultForPlot_%s_%d_type_%d.xlsx' % (fileName,fileSize,typeTrainDB))
df = pd.ExcelFile('./Training Data/remoteResultForPlot_%s_type_%d.xlsx' % (fileName, typeTrainDB))
dfLableList = df.parse('sheet1')
dfSVR = df.parse('sheet2')
dfRF = df.parse('sheet3')
dfELM = df.parse('sheet4')
dfDL = df.parse('Sheet5')
dfx = df.parse('sheet6')
print("This is dfx: ", dfx.values.T[0].tolist() )
dfFigureTitle = df.parse('sheet7')

lableList = dfLableList.values.T[0].tolist()
print("This is lableList: ", lableList )
if typeTrainDB !=2:
    x_axis_name = int((dfx.values.T[0].tolist())/1000)
else:
    x_axis_name = dfx.values.T[0].tolist()
figureTitle = ' '.join(dfFigureTitle.values.T[0].tolist())
finalErrorSVR = dfSVR.values.T[0].tolist()
finalErrorRF = (dfRF.values.T[0].tolist())
finalErrorELM = (dfELM.values.T[0].tolist())
finalErrorNN = dfDL.values.T[0].tolist()
# figureTitle = figureTitle.replace('u', '', 1)
print("This is lableList: ", lableList)
print("This is : SVR", finalErrorSVR)
print("This is : RF", finalErrorRF)
print("This is : ELM", finalErrorELM )
print("This is DL: ", finalErrorNN )
print("This is : x", x_axis_name)
print("This is : title ", figureTitle)

# Draw the figure
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
trace3 = {
    "x": lableList,
    "y": finalErrorELM,
    "line": {"color": "rgba(181,130,233,1)"},
    "name": "ELM",
    "type": "box",
    "xaxis": "x",
    "yaxis": "y"
}
trace4 = {
    "x": lableList,
    "y": finalErrorNN,
    "line": {"color": "rgba(121,110,193,1)"},
    "name": "Deep Learning",
    "type": "box",
    "xaxis": "x",
    "yaxis": "y"
}
data = Data([trace1, trace2, trace3,trace4])
# data = Data([trace1, trace2])
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
        "title": fileName,
        "type": "category"
    },
    "yaxis": {
        "domain": [0, 1],
        "title": "RMSE-Root mean square error"
    }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
