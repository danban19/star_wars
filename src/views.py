import requests
from django.shortcuts import render
from django.http import HttpResponse


def character(response):
    r = requests.get('https://swapi.dev/api/people/')

    return HttpResponse(r.text)
