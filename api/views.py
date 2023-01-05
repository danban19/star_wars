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
    update_homeworld(data)
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
    table = retrieve_table_to_json(name)
    headers = [item for item in next(iter(table))]
    characters = table[1:]
    return render(request, 'api/collection.html', {'characters': characters, 'headers': headers, 'name':name})


def export_to_csv(data):
    name = f'collection_{datetime.now().strftime(("%Y-%m-%dT%H-%M-%S"))}.csv'
    save_to_db(name)
    table = petl.fromdicts(data)

    # Rename 'edited' to 'date' column
    table = petl.rename(table, 'edited', 'date')

    # Remove redundant columns
    columns_to_remove = ['films', 'species', 'vehicles', 'starships', 'created', 'url']
    for column in columns_to_remove:
        table = petl.cutout(table, column)

    # Save table to csv file
    petl.tocsv(table, name)

    return table


def retrieve_table_to_json(name):
    table = petl.fromcsv(name)
    petl.tojson(table)
    return table


def save_to_db(name):
    file_name = Collection(name=name)
    file_name.save()


def update_homeworld(data):
    for character in data:
        character['homeworld'] = requests.get(character['homeworld']).json()['name']


