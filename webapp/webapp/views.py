import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


with open('../data/correlated_series.json', 'r') as infile:
    correlated_series = json.load(infile)


def index(request):
    series1, series2, correlation = correlated_series[0]
    context = {
        "series1": series1,
        "series2": series2,
        "correlation": correlation,
        # "correlated_series": correlated_series
    }
    return render(request, 'webapp/index.html', context)


@csrf_exempt
def data(request):
    idx = json.loads(request.body)['index']
    series1, series2, correlation = correlated_series[idx]
    data = {
        "series1": series1,
        "series2": series2,
        "correlation": correlation,
        # "correlated_series": correlated_series
    }
    return JsonResponse(data=data)
