import pandas as pd
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *

# py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
# py.sign_in('JianSun', 'AmAEUGYZCUR2D1dxFCZk')
py.sign_in('eddyrain','nzUXim14zjLU5cwWKtC0')

dataSize = 600
fileName = 'NO3'
testSize = 0.2


typeTrainDB = 7
kernelFunc = 'cosine'
normalMethod = 2
# n_components = 'mle'
n_components = 6
targetLevel = 2
minNum = 1000
figureTitle = ''
# df = pd.ExcelFile("Results/PCAResults/FeatureSelectionFor_NO3_Size_600_testSize_0.2_easy_get_1.xlsx")
df = pd.ExcelFile("Results/mrmrResults/FeatureSelectionFor_NO3_Size_750_testSize_0.2_easy_get_1.xlsx")
# df = pd.read_excel('./Training Data/remoteResultForPlot_%s_%d_type_%d.xlsx' % (fileName,fileSize,typeTrainDB))
# df = pd.ExcelFile('./Results/remoteResultForPlot_%s_type_%d_components_%s_size_%d_compare normalization methods.xlsx' % (
#                         fileName, typeTrainDB, str(n_components), dataSize))
# df = pd.ExcelFile('./Results/remoteResultForPlot_%s_type_%d_easy-get-param_size_%d.xlsx' % (
#                         fileName, typeTrainDB, dataSize))  #2

# df = pd.ExcelFile('./Results/remoteResultForPlot_%s_type_%d_both_param_used_size_%d.xlsx' % (
#                         fileName, typeTrainDB, dataSize))  #3
# df = pd.ExcelFile('./Results/remoteResultForPlot_%s_type_%d_both_param_used_size_%d_testSize_%.1f_n_component_%.1f.xlsx' % (
#                             fileName, typeTrainDB, dataSize,testSize,n_components))
# df = pd.ExcelFile(
#                         './Results/remoteResultForPlot_%s_type_%d_only_OTU_used_testSize_%.1f_n_component_%s_merged_Level_%d_Threshold_%d.xlsx' % (
#                             fileName, typeTrainDB,testSize,str(n_components),targetLevel,minNum))
# df = pd.ExcelFile(
#                         './Results/remoteResultForPlot_%s_type_%d_n_compoenet_%s_only_EasyParameters_used_including_salinity.xlsx' % (
#                             fileName, typeTrainDB,str(n_components)))
# df = pd.ExcelFile(
#                         './Results/remoteResultForPlot_%s_type_%d_both_merged_OTU_and Easy_get_testSize_%.1f_n_component_%s_merged_Level_%d_Threshold_%d.xlsx' % (
#                             fileName, typeTrainDB,testSize,str(n_components),targetLevel,minNum))
#
# df = pd.ExcelFile(
#                         './Results/remoteResultForPlot_%s_type_%d_both_merged_OTU_and Easy_get_testSize_%.1f_n_component_%s_merged_Level_%d_Threshold_%d_normal_method_%d_KernelPCA_%s.xlsx' % (
#                             fileName, typeTrainDB,testSize,str(n_components),targetLevel,minNum,normalMethod,kernelFunc))


# df = pd.ExcelFile(
#                         './Results/mrmrResults/remoteResultForPlot_%s_type_%d_Only_OTUs_Size_%d_mRMR_testSize_%.1f_normal_method_%d_useOriginal_False.xlsx' % (
#                             fileName, typeTrainDB,dataSize,testSize,normalMethod))
# df = pd.ExcelFile(
#                         './Results/mrmrResults/remoteResultForPlot_%s_type_%d_OTUs_and_Easy_get_Size_%d_mRMR_testSize_%.1f_normal_method_%d_useOriginal_False.xlsx' % (
#                             fileName, typeTrainDB,dataSize,testSize,normalMethod))
# df = pd.ExcelFile(
#     './Results/mrmrResults/FeatureSelectionFor_%s_Size_%d_testSize_%.1f_easy_get.xlsx' % (
#         fileName, dataSize, testSize))
# df = pd.ExcelFile('./Results/mrmrResults/RF_FeatureSelectionFor_%s_Size_%d_testSize_%.1f_easy_get.xlsx' %(fileName, dataSize, testSize))
# df = pd.ExcelFile('./Results/mrmrResults/RF_FeatureSelectionFor_%s_Size_%d_testSize_%.1f_easy_get_1.xlsx'%(fileName, dataSize, testSize))
# df = pd.ExcelFile('./Results/PCAResults/FeatureSelectionFor_%s_Size_%d_testSize_%.1f_easy_get.xlsx'%(fileName, dataSize, testSize))
dfLableList = df.parse('sheet1')
dfSVR = df.parse('sheet2') #nomRMR
dfRF = df.parse('sheet3')
# dfELM = df.parse('sheet4')
# dfDL = df.parse('Sheet5')
dfx = df.parse('sheet5')
print("This is dfx: ", dfx.values.T[0].tolist())
dfFigureTitle = df.parse('sheet6')

lableList = dfLableList.values.T[0].tolist()
print("This is lableList: ", lableList)
if typeTrainDB != 2:
    x_axis_name = ((dfx.values.T[0].tolist()))
else:
    x_axis_name = dfx.values.T[0].tolist()
# figureTitle = ' '.join(dfFigureTitle.values.T[0].tolist())
finalErrorSVR = dfSVR.values.T[0].tolist()
finalErrorRF = (dfRF.values.T[0].tolist())
# finalErrorELM = (dfELM.values.T[0].tolist())
# finalErrorNN = dfDL.values.T[0].tolist()
# figureTitle = figureTitle.replace('u', '', 1)
print("This is lableList: ", lableList)
print("This is : SVR", finalErrorSVR)
print("This is : RF", finalErrorRF)
# print("This is : ELM", finalErrorELM )
# print("This is DL: ", finalErrorNN )
# print("This is : x", x_axis_name)
# print("This is : title ", figureTitle)

# Draw the figure
trace1 = {
    "x": lableList,
    "y": finalErrorSVR,
    "line": {"color": "rgba(102,194,165,1)"},
    "name": "SVR",
    # "name": "Without mRMR",
    # "name": "PCA",
    "type": "box",
    "xaxis": "x",
    "yaxis": "y"
}
trace2 = {
    "x": lableList,
    "y": finalErrorRF,
    "line": {"color": "rgba(141,160,203,1)"},
    "name": "Random Forest",
    # "name": "With mRMR",
    "type": "box",
    "xaxis": "x",
    "yaxis": "y"
}
# trace3 = {
#     "x": lableList,
#     "y": finalErrorELM,
#     "line": {"color": "rgba(181,130,233,1)"},
#     "name": "ELM",
#     "type": "box",
#     "xaxis": "x",
#     "yaxis": "y"
# }
# trace4 = {
#     "x": lableList,
#     "y": finalErrorNN,
#     "line": {"color": "rgba(121,110,193,1)"},
#     "name": "Deep Learning",
#     "type": "box",
#     "xaxis": "x",
#     "yaxis": "y"
# }
# data = Data([trace1, trace2, trace3,trace4])
data = Data([trace1, trace2])
# data = Data([trace1, trace2, trace3])
layout = {
    "boxmode": "group",
    "margin": {
        "r": 10,
        "t": 25,
        "b": 40,
        "l": 60
    },
    # "title": "The reliability of ELM and Random Forest",
    # "title": figureTitle,
    "xaxis": {
        # "autorange": False,
        # "autotick": False,
        "categoryarray": [5,10,15,20,40,50,90],
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
