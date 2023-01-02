import requests
from django.shortcuts import render
from django.http import HttpResponse


def character(request):
    r = requests.get('https://swapi.dev/api/people/')
    for item in r.json()['results']:
        print(item)

    return render(request, 'api/characters.html', {'characters': r.json()['results']})
