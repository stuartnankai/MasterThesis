# Get this figure: fig = py.get_figure("https://plot.ly/~econtijoch/519/")
# Get this figure's data: data = py.get_figure("https://plot.ly/~econtijoch/519/").get_data()
# Add data to this figure: py.plot(Data([Scatter(x=[1, 2], y=[2, 3])]), filename ="IBD Absolute Abundances", fileopt="extend")
# Get y data of first trace: y1 = py.get_figure("https://plot.ly/~econtijoch/519/").get_data()[0]["y"]

# Get figure documentation: https://plot.ly/python/get-requests/
# Add data documentation: https://plot.ly/python/file-options/

# If you're using unicode in your file, you may need to specify the encoding.
# You can reproduce this figure in Python with the following code!

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00412032597966, 0.00297830847967, 0.0028795801568, 0.00492933234159], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__", 
  "marker": {
    "color": "rgba(86,180,233,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__"], 
  "type": "bar", 
  "uid": "340caf", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace2 = {
  "x": [1, 2, 3, 4], 
  "y": [0.0217565269054, 0.00725655879605, 0.00473321237926, 0.00689284242929], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__adolescentis", 
  "marker": {
    "color": "rgba(0,158,115,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__adolescentis", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__adolescentis", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__adolescentis", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__adolescentis", "Diagnosis: Uncertain<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__adolescentis"], 
  "type": "bar", 
  "uid": "4a8f3a", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace3 = {
  "x": [1, 2, 3, 4], 
  "y": [7.53882452706e-06, 0.000161725613051, 0.000210967955728, 9.12652214815e-05], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__animalis", 
  "marker": {
    "color": "rgba(240,228,66,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__animalis", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__animalis", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__animalis", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__animalis", "Diagnosis: Uncertain<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__animalis"], 
  "type": "bar", 
  "uid": "997c38", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace4 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000633332934701, 0.000356920303299, 0.000596128895485, 0.000971456040001], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__bifidum", 
  "marker": {
    "color": "rgba(0,114,178,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__bifidum", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__bifidum", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__bifidum", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__bifidum", "Diagnosis: Uncertain<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__bifidum"], 
  "type": "bar", 
  "uid": "5767a6", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace5 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00586067919332, 0.00281501607221, 0.00538772462504, 0.00790664357257], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__longum", 
  "marker": {
    "color": "rgba(213,94,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__longum", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__longum", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__longum", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__longum", "Diagnosis: Uncertain<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__longum"], 
  "type": "bar", 
  "uid": "99fb8e", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace6 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000306155812617, 0.000286636542961, 0.000127351144203, 0.000216588357696], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__pseudolongum", 
  "marker": {
    "color": "rgba(204,121,167,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__pseudolongum", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__pseudolongum", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__pseudolongum", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__pseudolongum", "Diagnosis: Uncertain<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Actinobacteria; o__Bifidobacteriales; f__Bifidobacteriaceae; g__Bifidobacterium; s__pseudolongum"], 
  "type": "bar", 
  "uid": "af032d", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace7 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000159738997949, 0.00010049206815, 0.000553499835159, 8.38686305678e-05], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__", 
  "marker": {
    "color": "rgba(153,153,153,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.01<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__"], 
  "type": "bar", 
  "uid": "5cbbef", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace8 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00658007573014, 0.00218390949591, 0.00333053149258, 0.00438325975584], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__aerofaciens", 
  "marker": {
    "color": "rgba(230,159,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__aerofaciens", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__aerofaciens", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__aerofaciens", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__aerofaciens", "Diagnosis: Uncertain<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__aerofaciens"], 
  "type": "bar", 
  "uid": "787217", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace9 = {
  "x": [1, 2, 3, 4], 
  "y": [5.11605678703e-07, 0.000264427072689, 0.000314479020714, 0.000363079811656], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__stercoris", 
  "marker": {
    "color": "rgba(255,0,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__stercoris", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__stercoris", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__stercoris", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__stercoris", "Diagnosis: Uncertain<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Collinsella; s__stercoris"], 
  "type": "bar", 
  "uid": "f6e6eb", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace10 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000156315105869, 0.000298834250246, 0.00059485351146, 0.000232080204389], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Eggerthella; s__lenta", 
  "marker": {
    "color": "rgba(0,0,255,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Eggerthella; s__lenta", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Eggerthella; s__lenta", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Eggerthella; s__lenta", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Eggerthella; s__lenta", "Diagnosis: Uncertain<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Actinobacteria; c__Coriobacteriia; o__Coriobacteriales; f__Coriobacteriaceae; g__Eggerthella; s__lenta"], 
  "type": "bar", 
  "uid": "e96454", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace11 = {
  "x": [1, 2, 3, 4], 
  "y": [0.0125272449698, 0.00655103109672, 0.0101024328681, 0.0153945104357], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__", 
  "marker": {
    "color": "rgba(255,0,255,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__"], 
  "type": "bar", 
  "uid": "39aa01", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace12 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000861033930112, 0.000517488201237, 0.000335996360661, 0.000985057796781], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__caccae", 
  "marker": {
    "color": "rgba(160,32,240,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__caccae", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__caccae", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__caccae", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__caccae", "Diagnosis: Uncertain<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__caccae"], 
  "type": "bar", 
  "uid": "f1a2ec", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace13 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00183075365736, 0.000962101612704, 0.000952336318404, 0.00142302329343], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__fragilis", 
  "marker": {
    "color": "rgba(0,255,255,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__fragilis", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__fragilis", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.02<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__fragilis", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__fragilis", "Diagnosis: Uncertain<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__fragilis"], 
  "type": "bar", 
  "uid": "5f8398", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace14 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00204292164197, 0.000716902361422, 0.000485065095183, 0.00249301847849], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__ovatus", 
  "marker": {
    "color": "rgba(255,255,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__ovatus", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__ovatus", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__ovatus", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__ovatus", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__ovatus"], 
  "type": "bar", 
  "uid": "ced575", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace15 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00258537588215, 0.00149936155125, 0.00130038179574, 0.00261181764479], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__uniformis", 
  "marker": {
    "color": "rgba(0,0,128,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__uniformis", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__uniformis", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__uniformis", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__uniformis", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Bacteroidaceae; g__Bacteroides; s__uniformis"], 
  "type": "bar", 
  "uid": "2df1d0", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace16 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00150885657387, 0.00034408143359, 0.000479295411058, 0.000392207886241], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__", 
  "marker": {
    "color": "rgba(210,180,140,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__"], 
  "type": "bar", 
  "uid": "e71629", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace17 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000962079641428, 0.000212218026523, 0.00215523880285, 0.00174455510364], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__distasonis", 
  "marker": {
    "color": "rgba(46,139,87,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__distasonis", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__distasonis", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__distasonis", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__distasonis", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Porphyromonadaceae; g__Parabacteroides; s__distasonis"], 
  "type": "bar", 
  "uid": "b6c892", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace18 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00185630284108, 0.00121336807785, 0.000592034746037, 2.43011777153e-06], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Prevotellaceae; g__Prevotella; s__copri", 
  "marker": {
    "color": "rgba(0,255,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Prevotellaceae; g__Prevotella; s__copri", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Prevotellaceae; g__Prevotella; s__copri", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Prevotellaceae; g__Prevotella; s__copri", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Prevotellaceae; g__Prevotella; s__copri", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Prevotellaceae; g__Prevotella; s__copri"], 
  "type": "bar", 
  "uid": "9ef592", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace19 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00190844787136, 0.000813111698494, 0.00148044005473, 0.000563558059303], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Rikenellaceae; g__; s__", 
  "marker": {
    "color": "rgba(218,165,32,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Rikenellaceae; g__; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Rikenellaceae; g__; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Rikenellaceae; g__; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Rikenellaceae; g__; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Bacteroidetes; c__Bacteroidia; o__Bacteroidales; f__Rikenellaceae; g__; s__"], 
  "type": "bar", 
  "uid": "e15e73", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace20 = {
  "x": [1, 2, 3, 4], 
  "y": [9.62014798507e-05, 0.000350985950296, 0.000568285240719, 7.43497610037e-05], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Enterococcaceae; g__Enterococcus; s__", 
  "marker": {
    "color": "rgba(205,192,176,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Enterococcaceae; g__Enterococcus; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Enterococcaceae; g__Enterococcus; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Enterococcaceae; g__Enterococcus; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Enterococcaceae; g__Enterococcus; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Enterococcaceae; g__Enterococcus; s__"], 
  "type": "bar", 
  "uid": "9fd747", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace21 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00246338600075, 0.000434810429106, 0.00251833965988, 0.000240002151203], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__", 
  "marker": {
    "color": "rgba(85,107,47,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__"], 
  "type": "bar", 
  "uid": "d74301", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace22 = {
  "x": [1, 2, 3, 4], 
  "y": [3.94685055763e-07, 3.21116501792e-09, 1.6096510384e-05, 0], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__mucosae", 
  "marker": {
    "color": "rgba(165,42,42,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__mucosae", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__mucosae", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__mucosae", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__mucosae", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Lactobacillus; s__mucosae"], 
  "type": "bar", 
  "uid": "21f6bc", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace23 = {
  "x": [1, 2, 3, 4], 
  "y": [6.49778738995e-07, 0.000143491117949, 0.00178167120816, 7.1381230736e-07], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Pediococcus; s__", 
  "marker": {
    "color": "rgba(205,16,118,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Pediococcus; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Pediococcus; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Pediococcus; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Pediococcus; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Lactobacillaceae; g__Pediococcus; s__"], 
  "type": "bar", 
  "uid": "b810ef", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace24 = {
  "x": [1, 2, 3, 4], 
  "y": [0, 0.0017009298772, 9.86051799726e-07, 0], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Lactococcus; s__", 
  "marker": {
    "color": "rgba(86,180,233,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Lactococcus; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Lactococcus; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Lactococcus; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Lactococcus; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Lactococcus; s__"], 
  "type": "bar", 
  "uid": "e54bbd", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace25 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00457634312622, 0.00177421625366, 0.00352011720003, 0.00417976798259], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Streptococcus; s__", 
  "marker": {
    "color": "rgba(0,158,115,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Streptococcus; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Streptococcus; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Streptococcus; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Streptococcus; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Lactobacillales; f__Streptococcaceae; g__Streptococcus; s__"], 
  "type": "bar", 
  "uid": "8cbe43", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace26 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000648784432065, 0.000530311419878, 0.000605674305544, 0.000356316417969], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Turicibacterales; f__Turicibacteraceae; g__Turicibacter; s__", 
  "marker": {
    "color": "rgba(240,228,66,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Bacilli; o__Turicibacterales; f__Turicibacteraceae; g__Turicibacter; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Turicibacterales; f__Turicibacteraceae; g__Turicibacter; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.03<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Turicibacterales; f__Turicibacteraceae; g__Turicibacter; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Turicibacterales; f__Turicibacteraceae; g__Turicibacter; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Bacilli; o__Turicibacterales; f__Turicibacteraceae; g__Turicibacter; s__"], 
  "type": "bar", 
  "uid": "a9153b", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace27 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00584355910903, 0.00215292364422, 0.00380257447772, 0.00374160987326], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__; g__; s__", 
  "marker": {
    "color": "rgba(0,114,178,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__; g__; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.08<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__; g__; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__; g__; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.05<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__; g__; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__; g__; s__"], 
  "type": "bar", 
  "uid": "b8555e", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace28 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00354060239833, 0.00304056145626, 0.00608517902896, 0.00281816912665], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__; s__", 
  "marker": {
    "color": "rgba(213,94,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.08<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__; s__"], 
  "type": "bar", 
  "uid": "74f28f", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace29 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00173202380516, 0.00227790726819, 0.0017654606972, 0.00141889979166], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__Clostridium; s__", 
  "marker": {
    "color": "rgba(204,121,167,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__Clostridium; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.08<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__Clostridium; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.04<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__Clostridium; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__Clostridium; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Clostridiaceae; g__Clostridium; s__"], 
  "type": "bar", 
  "uid": "76c812", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace30 = {
  "x": [1, 2, 3, 4], 
  "y": [0.0408732126646, 0.0224009838901, 0.0305864646625, 0.0445926602005], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__; s__", 
  "marker": {
    "color": "rgba(153,153,153,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.13<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.09<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__; s__"], 
  "type": "bar", 
  "uid": "054415", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace31 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000937068400503, 0.000258696665403, 0.00107425232787, 0.000563926989123], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__", 
  "marker": {
    "color": "rgba(230,159,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.13<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.09<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__"], 
  "type": "bar", 
  "uid": "57a886", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace32 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000188423421332, 0.000101789858769, 0.000421663344211, 0.000102148374066], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__gnavus", 
  "marker": {
    "color": "rgba(255,0,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__gnavus", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.13<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__gnavus", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.06<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__gnavus", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.09<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__gnavus", "Diagnosis: Uncertain<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__[Ruminococcus]; s__gnavus"], 
  "type": "bar", 
  "uid": "78d480", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace33 = {
  "x": [1, 2, 3, 4], 
  "y": [0.0110052853257, 0.00729400717855, 0.00920583563997, 0.00980433676544], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__", 
  "marker": {
    "color": "rgba(0,0,255,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.12<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__"], 
  "type": "bar", 
  "uid": "af24cd", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace34 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00225267483122, 0.000320826219321, 0.00149205096265, 0.000638853934993], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__producta", 
  "marker": {
    "color": "rgba(255,0,255,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__producta", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__producta", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.07<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__producta", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__producta", "Diagnosis: Uncertain<br>absolute_abundance: 0.12<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Blautia; s__producta"], 
  "type": "bar", 
  "uid": "78cc69", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace35 = {
  "x": [1, 2, 3, 4], 
  "y": [0.0104641953399, 0.00611877719039, 0.00698460025623, 0.00672802173544], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Coprococcus; s__", 
  "marker": {
    "color": "rgba(160,32,240,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Coprococcus; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.15<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Coprococcus; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.08<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Coprococcus; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Coprococcus; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.13<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Coprococcus; s__"], 
  "type": "bar", 
  "uid": "58e57f", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace36 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00592852610079, 0.00254744074501, 0.00252066695814, 0.00466449102653], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Dorea; s__", 
  "marker": {
    "color": "rgba(0,255,255,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Dorea; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.16<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Dorea; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.08<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Dorea; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Dorea; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.13<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Dorea; s__"], 
  "type": "bar", 
  "uid": "e8b691", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace37 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000288137195663, 0.000266920314736, 0.000393886188239, 4.04656231807e-05], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Lachnospira; s__", 
  "marker": {
    "color": "rgba(255,255,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Lachnospira; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.16<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Lachnospira; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.08<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Lachnospira; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Lachnospira; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.13<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Lachnospira; s__"], 
  "type": "bar", 
  "uid": "32225c", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace38 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00192006716731, 0.00132054496543, 0.00145154656933, 0.00342337537791], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Roseburia; s__", 
  "marker": {
    "color": "rgba(0,0,128,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Roseburia; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.16<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Roseburia; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.08<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Roseburia; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Roseburia; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Lachnospiraceae; g__Roseburia; s__"], 
  "type": "bar", 
  "uid": "268f28", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace39 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000149492859288, 2.78034769296e-05, 6.28408300286e-06, 8.54280142106e-05], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Peptostreptococcaceae; g__; s__", 
  "marker": {
    "color": "rgba(210,180,140,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Peptostreptococcaceae; g__; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.16<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Peptostreptococcaceae; g__; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.08<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Peptostreptococcaceae; g__; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Peptostreptococcaceae; g__; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Peptostreptococcaceae; g__; s__"], 
  "type": "bar", 
  "uid": "f89457", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace40 = {
  "x": [1, 2, 3, 4], 
  "y": [0.0176182869838, 0.00904423840625, 0.0146272187343, 0.0169613451156], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__; s__", 
  "marker": {
    "color": "rgba(46,139,87,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.09<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.13<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.15<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__; s__"], 
  "type": "bar", 
  "uid": "5e1ece", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace41 = {
  "x": [1, 2, 3, 4], 
  "y": [0.0126198695986, 0.00611397934418, 0.00838483530805, 0.0200996744398], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Faecalibacterium; s__prausnitzii", 
  "marker": {
    "color": "rgba(0,255,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Faecalibacterium; s__prausnitzii", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.19<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Faecalibacterium; s__prausnitzii", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Faecalibacterium; s__prausnitzii", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.13<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Faecalibacterium; s__prausnitzii", "Diagnosis: Uncertain<br>absolute_abundance: 0.17<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Faecalibacterium; s__prausnitzii"], 
  "type": "bar", 
  "uid": "03e1eb", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace42 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000419071072708, 0.000369686174423, 0.0010731924566, 0.000866489545277], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Oscillospira; s__", 
  "marker": {
    "color": "rgba(218,165,32,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Oscillospira; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.19<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Oscillospira; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Oscillospira; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Oscillospira; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.17<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Oscillospira; s__"], 
  "type": "bar", 
  "uid": "4567f1", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace43 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00571115111279, 0.00315735954859, 0.00457092360933, 0.00643666230771], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Ruminococcus; s__", 
  "marker": {
    "color": "rgba(205,192,176,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Ruminococcus; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.19<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Ruminococcus; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Ruminococcus; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Ruminococcus; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Ruminococcaceae; g__Ruminococcus; s__"], 
  "type": "bar", 
  "uid": "a20ed8", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace44 = {
  "x": [1, 2, 3, 4], 
  "y": [6.39032297953e-05, 0.00013486026285, 0.000309654202334, 0.000734989056007], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Acidaminococcus; s__", 
  "marker": {
    "color": "rgba(85,107,47,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Acidaminococcus; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Acidaminococcus; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Acidaminococcus; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Acidaminococcus; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Acidaminococcus; s__"], 
  "type": "bar", 
  "uid": "2e5d29", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace45 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000355519232439, 0.000702524220291, 0.000233700463545, 0.00142874924563], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Dialister; s__", 
  "marker": {
    "color": "rgba(165,42,42,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Dialister; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Dialister; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Dialister; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Dialister; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Dialister; s__"], 
  "type": "bar", 
  "uid": "304456", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace46 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00149908949527, 0.000226633761812, 0.000249903517524, 0.000175538156653], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Megasphaera; s__", 
  "marker": {
    "color": "rgba(205,16,118,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Megasphaera; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Megasphaera; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Megasphaera; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Megasphaera; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Clostridia; o__Clostridiales; f__Veillonellaceae; g__Megasphaera; s__"], 
  "type": "bar", 
  "uid": "054c2e", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace47 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000333830660458, 0.000888713304967, 0.00149353534279, 0.00204412666722], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__; s__", 
  "marker": {
    "color": "rgba(86,180,233,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__; s__"], 
  "type": "bar", 
  "uid": "107aa5", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace48 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00218319139763, 0.00015748466168, 0.00179233782669, 2.68884026769e-06], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__biforme", 
  "marker": {
    "color": "rgba(0,158,115,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__biforme", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__biforme", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__biforme", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__biforme", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__biforme"], 
  "type": "bar", 
  "uid": "4908ed", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace49 = {
  "x": [1, 2, 3, 4], 
  "y": [3.30672007336e-05, 4.73144904088e-05, 0.000583417742603, 7.70104007916e-05], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__dolichum", 
  "marker": {
    "color": "rgba(240,228,66,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__dolichum", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__dolichum", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__dolichum", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.14<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__dolichum", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__[Eubacterium]; s__dolichum"], 
  "type": "bar", 
  "uid": "a31932", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace50 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00166849217934, 0.000437890231975, 0.000428428775783, 9.18874619171e-07], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__Catenibacterium; s__", 
  "marker": {
    "color": "rgba(0,114,178,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__Catenibacterium; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__Catenibacterium; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__Catenibacterium; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.15<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__Catenibacterium; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Firmicutes; c__Erysipelotrichi; o__Erysipelotrichales; f__Erysipelotrichaceae; g__Catenibacterium; s__"], 
  "type": "bar", 
  "uid": "a2eae7", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace51 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000352999809418, 0.000519830706876, 0.000873602741997, 0.000369263237066], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Proteobacteria; c__Betaproteobacteria; o__Burkholderiales; f__Alcaligenaceae; g__Sutterella; s__", 
  "marker": {
    "color": "rgba(213,94,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Proteobacteria; c__Betaproteobacteria; o__Burkholderiales; f__Alcaligenaceae; g__Sutterella; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Proteobacteria; c__Betaproteobacteria; o__Burkholderiales; f__Alcaligenaceae; g__Sutterella; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.1<br>Taxon: k__Bacteria; p__Proteobacteria; c__Betaproteobacteria; o__Burkholderiales; f__Alcaligenaceae; g__Sutterella; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.15<br>Taxon: k__Bacteria; p__Proteobacteria; c__Betaproteobacteria; o__Burkholderiales; f__Alcaligenaceae; g__Sutterella; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.18<br>Taxon: k__Bacteria; p__Proteobacteria; c__Betaproteobacteria; o__Burkholderiales; f__Alcaligenaceae; g__Sutterella; s__"], 
  "type": "bar", 
  "uid": "efc634", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace52 = {
  "x": [1, 2, 3, 4], 
  "y": [0.00301328835542, 0.00329392213909, 0.00260887096501, 0.00123534895704], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__; s__", 
  "marker": {
    "color": "rgba(204,121,167,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__; s__", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.2<br>Taxon: k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__; s__", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__; s__", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.15<br>Taxon: k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__; s__", "Diagnosis: Uncertain<br>absolute_abundance: 0.19<br>Taxon: k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__; s__"], 
  "type": "bar", 
  "uid": "2f7b3a", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace53 = {
  "x": [1, 2, 3, 4], 
  "y": [0.000587204524174, 0.00116082515262, 0.000440717733704, 2.65839732312e-05], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__Pantoea; s__agglomerans", 
  "marker": {
    "color": "rgba(153,153,153,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__Pantoea; s__agglomerans", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.21<br>Taxon: k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__Pantoea; s__agglomerans", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__Pantoea; s__agglomerans", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.15<br>Taxon: k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__Pantoea; s__agglomerans", "Diagnosis: Uncertain<br>absolute_abundance: 0.19<br>Taxon: k__Bacteria; p__Proteobacteria; c__Gammaproteobacteria; o__Enterobacteriales; f__Enterobacteriaceae; g__Pantoea; s__agglomerans"], 
  "type": "bar", 
  "uid": "c6e466", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
trace54 = {
  "x": [1, 2, 3, 4], 
  "y": [2.08461887745e-05, 0.000180773501045, 9.3136431871e-06, 8.08388527399e-06], 
  "error_x": {"visible": False}, 
  "error_y": {"visible": False}, 
  "hoverinfo": "text", 
  "legendgroup": "k__Bacteria; p__Verrucomicrobia; c__Verrucomicrobiae; o__Verrucomicrobiales; f__Verrucomicrobiaceae; g__Akkermansia; s__muciniphila", 
  "marker": {
    "color": "rgba(230,159,0,1)", 
    "line": {
      "color": "rgba(0,0,0,1)", 
      "width": 1.88976377953
    }
  }, 
  "name": "k__Bacteria; p__Verrucomicrobia; c__Verrucomicrobiae; o__Verrucomicrobiales; f__Verrucomicrobiaceae; g__Akkermansia; s__muciniphila", 
  "opacity": 1, 
  "orientation": "v", 
  "showlegend": True, 
  "text": ["Diagnosis: Healthy<br>absolute_abundance: 0.21<br>Taxon: k__Bacteria; p__Verrucomicrobia; c__Verrucomicrobiae; o__Verrucomicrobiales; f__Verrucomicrobiaceae; g__Akkermansia; s__muciniphila", "Diagnosis: Crohn's Disease<br>absolute_abundance: 0.11<br>Taxon: k__Bacteria; p__Verrucomicrobia; c__Verrucomicrobiae; o__Verrucomicrobiales; f__Verrucomicrobiaceae; g__Akkermansia; s__muciniphila", "Diagnosis: Ulcerative Colitis<br>absolute_abundance: 0.15<br>Taxon: k__Bacteria; p__Verrucomicrobia; c__Verrucomicrobiae; o__Verrucomicrobiales; f__Verrucomicrobiaceae; g__Akkermansia; s__muciniphila", "Diagnosis: Uncertain<br>absolute_abundance: 0.19<br>Taxon: k__Bacteria; p__Verrucomicrobia; c__Verrucomicrobiae; o__Verrucomicrobiales; f__Verrucomicrobiaceae; g__Akkermansia; s__muciniphila"], 
  "type": "bar", 
  "uid": "74c79a", 
  "visible": True, 
  "xaxis": "x", 
  "yaxis": "y"
}
data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9, trace10, trace11, trace12, trace13, trace14, trace15, trace16, trace17, trace18, trace19, trace20, trace21, trace22, trace23, trace24, trace25, trace26, trace27, trace28, trace29, trace30, trace31, trace32, trace33, trace34, trace35, trace36, trace37, trace38, trace39, trace40, trace41, trace42, trace43, trace44, trace45, trace46, trace47, trace48, trace49, trace50, trace51, trace52, trace53, trace54])
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
  "title": "IBD Absolute Abundances", 
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
    "ticktext": ["Healthy", "Crohn's Disease", "Ulcerative Colitis", "Uncertain"], 
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
    "title": "Average Absolute Abundance (ug DNA per mg Fecal Pellet)", 
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