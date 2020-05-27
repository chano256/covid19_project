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

    #data = requests.get(url, auth=HTTPBasicAuth(username, password))

    username = 'allandavicham@gmail.com'
    auth_key = 'rumXjXoEQeQIbQdBO6h0Mk7ud8lOCUttTO7B3c9h' #NASA
    url = 'https://api.nasa.gov/insight_weather/?api_key='

    data = requests.get(url + auth_key + '&feedtype=json&ver=1.0')
    response = json.loads(data.content)

    x = pd.DataFrame(response['526']['WD'], columns=['5'])
    x = x.reset_index()
    values = x['index'].values.tolist()

    xAxis = values
    yAxis = [25, 10, 5, 2, 20, 30, 40, 50, 55]
    showGraph = 'True'
    context = {
        'xAxis': xAxis,
        'yAxis': yAxis,
        'showGraph': showGraph,
        'values': values,
    }
    return render(request, 'index.html', context)

def itemDetails(request):
    xAxis = ['January', 'February', 'March', 'April', 'May', 'June', 'July']
    yAxis = [25, 10, 5, 2, 20, 30, 40, 50, 55]
    showGraph = 'False'
    context = {
        'xAxis': xAxis,
        'yAxis': yAxis,
        'showGraph': showGraph,
    }
    return render(request, 'index.html', context)

def showMap(request):
    context = {
        'a': 'a',
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

    #data = requests.get(url, auth=HTTPBasicAuth(username, password))
    #response = json.loads(data.content)
    context = {
            'response': 'response',
        }
    return render(request, 'api_data.html', context)