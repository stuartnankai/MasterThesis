# import pandas as pd
# from pandas import ExcelWriter
# import matplotlib.pyplot as plt
# import seaborn
# minNum = 10
# data = pd.read_table('Data_all_2016_otus.txt',delim_whitespace=True,index_col=0)
#
# def dataReBuild(oldData):
#     dataP1 = oldData.iloc[:,0:1]
#     dataP2 = oldData.iloc[:,1:]
#     dataP2['Col_sum'] = 0
#     dataP2.loc['Row_sum'] = 0
#     dataP2['Col_sum'] = dataP2.apply(lambda x: x.sum(), axis=1)
#     dataP2.loc['Row_sum'] = dataP2.apply(lambda x: x.sum())
#     dataP1.loc['Row_sum','Taxonomy'] = 'NaN'
# #    print(dataP1)
# #    print(dataP2)
#     tempData = dataP1.join(dataP2)
#     return tempData
#
# newdata = dataReBuild(data)
#
#
# for index, row in newdata.iterrows():
# #    print(row['Col_sum'])
#     if row['Col_sum'] <= minNum:
#         newdata.drop([index],inplace = True)
#
# # for row in newdata.itertuples(index=True, name='Pandas'):
# #     print(row)
# #     if getattr(row,"Col_sum") <= minNum:
# #         newdata.drop([row])
#
#
# finalData = dataReBuild(newdata)
# print(finalData)
#
# #print(finalData.iloc[-1,2:-1])
#
# #plt.hist(finalData.loc['Row_sum'], bins=len(finalData.index))
# seaborn.distplot(finalData.iloc[-1,2:-1], bins=len(finalData.iloc[-1,2:-1]))
#
#
# finalData.to_csv('out1.csv')
# writer = ExcelWriter('Excel.xls')
# finalData.to_excel(writer,'Sheet1')
# writer.save()
# Learn about API authentication here: https://plot.ly/pandas/getting-started
# Find your api_key here: https://plot.ly/settings/api
import random

import plotly.plotly as py
import plotly as pltl
from plotly.graph_objs import *

pltl.tools.set_credentials_file(username='sunjiannankai', api_key='r8kdW8nbxiw5HJeCehBj')
py.sign_in('sunjiannankai', 'r8kdW8nbxiw5HJeCehBj')
import pandas as pd


def random_color():
    r = lambda: random.randint(0, 255)
    return ('#%02X%02X%02X' % (r(), r(), r()))


df = pd.read_excel("Workbook3.xlsx")
genSamples = list(df.iloc[:-1, 0])
# print(genSamples)
waterSample = list(df.columns.values)
waterSample = waterSample[2:]
print(waterSample)
DataSample = []

# Demo1
otuDict = dict()
for i in range(len(genSamples)):
    tempList = []
    for j in range(len(waterSample)):
        sumList = list(df.iloc[-1, 2:])
        # print(sumList)
        tempList.append(df.iloc[i, j + 2] / sumList[j])
        # print(j/df.iloc[-1,j+2] for j in list(df.iloc[i,2:]))
    # print(tempList)
    otuDict[genSamples[i]] = tempList
print(otuDict)

for j in range(len(genSamples)):
    trace = 'trace%d' % j
    trace = {
        "x": waterSample,
        "y": otuDict[genSamples[j]],
        "error_x": {"visible": False},
        "error_y": {"visible": False},
        "hoverinfo": "text",
        # "legendgroup": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__",
        "marker": {
            "color": "rgb" + str(random_color()),
            "line": {
                "color": "rgba(0,0,0,1)",
                "width": 1.88976377953
            }
        },
        # "name": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__",
        "opacity": 1,
        "orientation": "v",
        "showlegend": True,
        "text": str(genSamples[j]),
        # "text": [
        #     "Diagnosis: Healthy<br>absolute_abundance: 0<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__",
        #     "Diagnosis: Crohn's Disease<br>absolute_abundance: 0<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__",
        #     "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__",
        #     "Diagnosis: Uncertain<br>absolute_abundance: 0<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__"],
        "type": "bar",
        "visible": True,
        "xaxis": "x",
        "yaxis": "y"
    }
    DataSample.append(trace)
data = Data(DataSample)
layout = {
  "autosize": True,
  "bargap": 0.2,
  "bargroupgap": 0,
  "barmode": "stack",
  "barnorm": "",
  "dragmode": "zoom",
  "font": {
    "color": "rgba(0, 0, 0, 1)",
    "family": "sans",
    "size": 15.9402241594
  },
  "height": 572.875,
  "hidesources": False,
  "hovermode": "closest",
  "margin": {
    "r": 9.29846409298,
    "t": 35.0871272815,
    "autoexpand": True,
    "b": 161.387996017,
    "l": 85.6787048568,
    "pad": 0
  },
  "paper_bgcolor": "#fff",
  "plot_bgcolor": "transparent",
  "separators": ".,",
  "shapes": [
    {
      "fillcolor": "rgba(0,0,0,0)",
      "layer": "above",
      "line": {
        "dash": "solid",
        "width": 0
      },
      "opacity": 1,
      "type": "rect",
      "x0": 0,
      "x1": 1,
      "xref": "paper",
      "y0": 0,
      "y1": 1,
      "yref": "paper"
    }
  ],
  "showlegend": False,
  "smith": False,
  "title": "OTU proportion structure",
  "titlefont": {
    "color": "rgba(0, 0, 0, 1)",
    "family": "sans",
    "size": 22
  },
  "width": 1020,
  "xaxis": {
    "anchor": "y",
    "autorange": True,
    "color": "#444",
    "domain": [0, 1],
    "exponentformat": "B",
    "fixedrange": False,
    "hoverformat": ".2f",
    "linecolor": "rgba(0, 0, 0, 1)",
    "linewidth": 0.664176006642,
    "mirror": False,
    "range": [0.5, 4.5],
    "rangemode": "normal",
    "showexponent": "all",
    "showgrid": False,
    "showline": True,
    "showticklabels": True,
    "side": "bottom",
    "tickangle": -45,
    "tickcolor": "rgba(0, 0, 0, 1)",
    "tickfont": {
      "color": "rgba(0, 0, 0, 1)",
      "family": "sans",
      "size": 23.9103362391
    },
    "tickformat": "",
    "ticklen": 4.64923204649,
    "tickmode": "array",
    "tickprefix": "",
    "ticks": "outside",
    "ticksuffix": "",
    # "ticktext": ["Healthy", "Crohn's Disease", "Ulcerative Colitis", "Uncertain"],
    "ticktext": waterSample,
    "tickvals": [1, 2, 3, 4],
    "tickwidth": 0.664176006642,
    "title": "Diagnosis",
    "titlefont": {
      "color": "rgba(0, 0, 0, 1)",
      "family": "sans",
      "size": 23.9103362391
    },
    "type": "linear",
    "zeroline": False
  },
  "yaxis": {
    "anchor": "x",
    "autorange": True,
    "color": "#444",
    "domain": [0, 1],
    "exponentformat": "B",
    "fixedrange": False,
    "hoverformat": ".2f",
    "linecolor": "rgba(0, 0, 0, 1)",
    "linewidth": 0.664176006642,
    "mirror": False,
    "range": [0, 0.215845323434],
    "rangemode": "normal",
    "showexponent": "all",
    "showgrid": False,
    "showline": True,
    "showticklabels": True,
    "side": "left",
    "tickangle": 0,
    "tickcolor": "rgba(0, 0, 0, 1)",
    "tickfont": {
      "color": "rgba(0, 0, 0, 1)",
      "family": "sans",
      "size": 23.9103362391
    },
    "tickformat": "",
    "ticklen": 4.64923204649,
    "tickmode": "array",
    "tickprefix": "",
    "ticks": "outside",
    "ticksuffix": "",
    "ticktext": ["0.00", "0.05", "0.10", "0.15", "0.20"],
    "tickvals": [0, 0.05, 0.1, 0.15, 0.2],
    "tickwidth": 0.664176006642,
    "title": "OTU",
    "titlefont": {
      "color": "rgba(0, 0, 0, 1)",
      "family": "sans",
      "size": 23.9103362391
    },
    "type": "linear",
    "zeroline": False
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

# for i in range(len(waterSample)):
#     # ylable = list(df.iloc[:-1,i+2])
#     # ylable = [j for j in ylable if j>30]
#     ylable = []
#     nameList = []
#     for n in range(1,len(genSamples)):
#         if df.iloc[n,i+2] > 30:
#             nameList.append(df.iloc[n,0])
#             ylable.append(df.iloc[n,i+2])
#     print(nameList)
#     print(ylable)
#     # ylable = [j/sum(ylable) for j in ylable]
#     # print(ylable)
#     for m in range(len(nameList)):
#         trace = 'trace%d'%(i*10+m)
#         trace = {
#             "x":list(waterSample),
#             "y":ylable,
#             "marker": {"color": "rgb" + str(random_color())},
#             "type": "bar",
#             "name":"%s"%nameList[m],
#         }
#         DataSample.append(trace)
#
# data = Data(DataSample)
# layout = {
#   "annotations": [
#     {
#       "x": 0.1,
#       "y": 0.3,
#       "align": "center",
#       "arrowcolor": "rgba(68, 68, 68, 0)",
#       "arrowhead": 1,
#       "arrowsize": 1,
#       "arrowwidth": 0,
#       "ax": 1,
#       "ay": 255.608329773,
#       "bgcolor": "rgba(0,0,0,0)",
#       "bordercolor": "",
#       "borderpad": 1,
#       "borderwidth": 1,
#       "font": {
#         "color": "",
#         "family": "",
#         "size": 0
#       },
#       "opacity": 1,
#       "showarrow": True,
#       "text": "Data: Institute for Health Metrics  and Evaluation",
#       "xanchor": "auto",
#       "xref": "paper",
#       "yanchor": "auto",
#       "yref": "paper"
#     }
#   ],
#   "autosize": False,
#   "bargap": 0.2,
#   "bargroupgap": 0,
#   "barmode": "stack",
#   "boxgap": 0.3,
#   "boxgroupgap": 0.3,
#   "boxmode": "overlay",
#   "dragmode": "zoom",
#   "font": {
#     "color": "#444",
#     "family": "Raleway, sans-serif",
#     "size": 12
#   },
#   "height": 800,
#   "hidesources": True,
#   "hovermode": "x",
#   "legend": {
#     "x": 1.01889808481,
#     "y": 0.958064516129,
#     "bgcolor": "rgba(255, 255, 255, 0)",
#     "bordercolor": "#444",
#     "borderwidth": 0,
#     "font": {
#       "color": "",
#       "family": "",
#       "size": 0
#     },
#     "traceorder": "reversed",
#     "xanchor": "left",
#     "yanchor": "top"
#   },
#   "margin": {
#     "r": 80,
#     "t": 100,
#     "autoexpand": True,
#     "b": 80,
#     "l": 80,
#     "pad": 0
#   },
#   "paper_bgcolor": "rgb(255, 255, 255)",
#   "plot_bgcolor": "#fff",
#   "separators": ".,",
#   "showlegend": True,
#   "smith": False,
#   "title": "<br><br>Most Common Ways to Die, by Age, in the U.S.",
#   "titlefont": {
#     "color": "",
#     "family": "",
#     "size": 0
#   },
#   "width": 1000,
#   "xaxis": {
#     "anchor": "y",
#     "autorange": True,
#     "autotick": True,
#     "domain": [0, 1],
#     "dtick": 1,
#     "exponentformat": "B",
#     "gridcolor": "#eee",
#     "gridwidth": 1,
#     "linecolor": "#444",
#     "linewidth": 1,
#     "mirror": False,
#     "nticks": 0,
#     "overlaying": False,
#     "position": 0,
#     "range": [-0.5, 18.5],
#     "rangemode": "normal",
#     "showexponent": "all",
#     "showgrid": False,
#     "showline": False,
#     "showticklabels": True,
#     "tick0": 0,
#     "tickangle": "auto",
#     "tickcolor": "#444",
#     "tickfont": {
#       "color": "",
#       "family": "",
#       "size": 0
#     },
#     "ticklen": 5,
#     "ticks": "",
#     "tickwidth": 1,
#     "title": "",
#     "titlefont": {
#       "color": "",
#       "family": "",
#       "size": 0
#     },
#     "type": "category",
#     "zeroline": False,
#     "zerolinecolor": "#444",
#     "zerolinewidth": 1
#   },
#   "yaxis": {
#     "anchor": "x",
#     "autorange": True,
#     "autotick": False,
#     "domain": [0, 1],
#     "dtick": 10,
#     "exponentformat": "B",
#     "gridcolor": "#eee",
#     "gridwidth": 1,
#     "linecolor": "#444",
#     "linewidth": 1,
#     "mirror": False,
#     "nticks": 0,
#     "overlaying": False,
#     "position": 0,
#     "range": [0, 105.263157895],
#     "rangemode": "normal",
#     "showexponent": "all",
#     "showgrid": False,
#     "showline": False,
#     "showticklabels": True,
#     "tick0": 0,
#     "tickangle": "auto",
#     "tickcolor": "#444",
#     "tickfont": {
#       "color": "",
#       "family": "",
#       "size": 0
#     },
#     "ticklen": 5,
#     "ticks": "",
#     "tickwidth": 1,
#     "title": "% Deaths",
#     "titlefont": {
#       "color": "",
#       "family": "",
#       "size": 0
#     },
#     "type": "linear",
#     "zeroline": False,
#     "zerolinecolor": "#444",
#     "zerolinewidth": 1
#   }
# }
# fig = Figure(data=data, layout=layout)
# plot_url = py.plot(fig)
