# Star Wars project

Star Wars project uses SWAPI api to fetch data about Star Wars characters. The project consists of 4 endpoints:
/api/start/ Main page
/api/characters/ Page shown after characters' fetch
/api/collections/ Shows the list of all the collections fetched by the user
/api/collections/<name>/ Shows a specific collection

## In order to setup the project locally, run the following commands in the project's folder:

### Create a virtual environment
_python3 -m venv .venv_

### Install dependencies
_pip install -r requirements.txt_

### Activate virtual environment
_. ./.venv/bin/activate_

### Apply migrations
_python manage.py migrate_

### Run server
_python manage.py runserver_
