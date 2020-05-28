from django.shortcuts import render
import pandas as pd
from requests.auth import HTTPBasicAuth
import requests
import json

# Create your views here.
def index(request):
    username = '31ff0841404f58fa7d6b23258cf6473ec30799ce2406385134cb5314d7bd020e'
    password = '816443112718221d3a7925c5d53930fa4606ba9f5f89cfc47cfae20a1dc648e7'
    url = 'http://212.88.98.126:7095/tweets'

    data = requests.get(url, auth=HTTPBasicAuth(username, password))
    response = json.loads(data.content)

    barPlotData = pd.DataFrame(response)
    yAxis = barPlotData['retweet_count'].values.tolist()
    xAxis = barPlotData['id'].values.tolist()

    barPlotData = barPlotData['user'].values.tolist()
    values = pd.DataFrame(barPlotData)
    xValues = values['screen_name'].values.tolist()
    yValues = values['friends_count'].values.tolist()

    showGraph = 'True'
    context = {
        'xAxis': xAxis,
        'yAxis': yAxis,
        'showGraph': showGraph,
        'xValues': xValues,
        'yValues': yValues,
    }
    return render(request, 'index.html', context)

def itemDetails(request):
    username = '31ff0841404f58fa7d6b23258cf6473ec30799ce2406385134cb5314d7bd020e'
    password = '816443112718221d3a7925c5d53930fa4606ba9f5f89cfc47cfae20a1dc648e7'
    url = 'http://212.88.98.126:7095/tweets'

    data = requests.get(url, auth=HTTPBasicAuth(username, password))
    response = json.loads(data.content)

    barPlotData = pd.DataFrame(response)
    yAxis = barPlotData['retweet_count'].values.tolist()
    xAxis = barPlotData['id'].values.tolist()

    barPlotData = barPlotData['user'].values.tolist()
    values = pd.DataFrame(barPlotData)
    xValues = values['screen_name'].values.tolist()
    yValues = values['friends_count'].values.tolist()

    showGraph = 'False'
    context = {
        'xAxis': xAxis,
        'yAxis': yAxis,
        'showGraph': showGraph,
        'xValues': xValues,
        'yValues': yValues,
    }
    return render(request, 'index.html', context)

def showMap(request):
    username = '31ff0841404f58fa7d6b23258cf6473ec30799ce2406385134cb5314d7bd020e'
    password = '816443112718221d3a7925c5d53930fa4606ba9f5f89cfc47cfae20a1dc648e7'
    url = 'http://212.88.98.126:7095/tweets'

    data = requests.get(url, auth=HTTPBasicAuth(username, password))
    response = json.loads(data.content)

    barPlotData = pd.DataFrame(response)
    yAxis = barPlotData['retweet_count'].values.tolist()
    xAxis = barPlotData['id'].values.tolist()

    barPlotData = barPlotData['user'].values.tolist()
    values = pd.DataFrame(barPlotData)
    xValues = values['screen_name'].values.tolist()
    yValues = values['friends_count'].values.tolist()

    showGraph = 'False'
    context = {
        'xAxis': xAxis,
        'yAxis': yAxis,
        'showGraph': showGraph,
        'xValues': xValues,
        'yValues': yValues,
    }
    return render(request, 'map.html', context)

def contact(request):
    context = {
        'a': 'a',
    }
    return render(request, 'contact.html', context)

def api_data(request):
    username = '31ff0841404f58fa7d6b23258cf6473ec30799ce2406385134cb5314d7bd020e'
    password = '816443112718221d3a7925c5d53930fa4606ba9f5f89cfc47cfae20a1dc648e7'
    url = 'http://212.88.98.126:7095/tweets'

    data = requests.get(url, auth=HTTPBasicAuth(username, password))
    response = json.loads(data.content)

    context = {
        'response': response,
    }
    return render(request, 'api_data.html', context)