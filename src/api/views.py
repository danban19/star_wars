import requests
from django.shortcuts import render
from django.http import HttpResponse


def character(request):
    r = requests.get('https://swapi.dev/api/people/')

    return render(request, 'api/characters.html', {})
