import requests
from django.shortcuts import render
from api.models import Collection
from api.helpers import update_homeworld, export_to_csv, retrieve_table_to_json


def start_view(request):
    return render(request, 'api/start.html', {})


def character_view(request):
    """Fetch character data and saves it to database"""

    r = requests.get('https://swapi.dev/api/people/')
    data = r.json()['results']
    update_homeworld(data)
    export_to_csv(data)
    return render(request, 'api/characters.html')


def collections_view(request):
    """Display all the character collections fetched by the user"""

    collections = Collection.objects.all()
    return render(request, 'api/collections.html', {"collections": collections})


def single_collection_view(request, name: str):
    """Display the collection chosen by the user"""

    table = retrieve_table_to_json(name)
    headers = [item for item in next(iter(table))]
    characters = table[1:]
    return render(request, 'api/collection.html', {'characters': characters, 'headers': headers, 'name':name})

