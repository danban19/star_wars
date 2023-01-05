import requests
import petl
from datetime import datetime

from django.shortcuts import render
from api.models import Collection


def start_view(request):
    return render(request, 'api/start.html', {})


def character_view(request):
    r = requests.get('https://swapi.dev/api/people/')
    data = r.json()['results']
    headers = [item for item in next(iter(data))]
    export_to_csv(data)

    return render(
        request,
        'api/characters.html',
        {'characters': data,
         'headers': headers
         }
    )


def collections_view(request):
    collections = Collection.objects.all()
    return render(request, 'api/collections.html', {"collections": collections})


def single_collection_view(request, name):
    table = petl.fromcsv(name)
    petl.tojson(table)
    headers = [item for item in next(iter(table))]
    characters = table[1:]
    return render(request, 'api/collection.html', {'characters': characters, 'headers': headers, 'name':name})


def export_to_csv(data):
    name = f'collection_{datetime.now().strftime(("%Y-%m-%dT%H-%M-%S"))}.csv'
    save_to_db(name)
    table = petl.fromdicts(data)
    petl.tocsv(table, name)


def save_to_db(name):
    file_name = Collection(name=name)
    file_name.save()

