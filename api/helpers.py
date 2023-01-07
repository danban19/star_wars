import requests
import petl
from datetime import datetime
from api.models import Collection


def export_to_csv(data: dict):
    """Helper function to update columns and save table to db"""

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


def retrieve_table_to_json(name: str):
    table = petl.fromcsv(name)
    petl.tojson(table)
    return table


def save_to_db(name: str):
    file_name = Collection(name=name)
    file_name.save()


def update_homeworld(data: dict):
    for character in data:
        character['homeworld'] = requests.get(character['homeworld']).json()['name']

