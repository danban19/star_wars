import requests
import csv
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def start_view(request):
    return render(request, 'api/start.html', {})


def character_view(request):
    r = requests.get('https://swapi.dev/api/people/')
    data = r.json()['results']
    headers = [item for item in next(iter(data))]
    export_to_csv(data, headers)

    return render(
        request,
        'api/characters.html',
        {'characters': data,
         'headers': headers
         }
    )


def collections_view(request):
    return render(request, 'api/collections.html', {})


def export_to_csv(data, headers):
    name = f'Collection_{datetime.now().strftime(("%m-%d-%YT%H-%M-%S"))}'

    with open(f'{name}.csv', 'w', encoding='UTF8') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)

