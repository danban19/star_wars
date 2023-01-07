Star Wars project uses SWAPI api to fetch data about Star Wars characters. The project consists of 4 endpoints:
/api/start/ Main page
/api/characters/ Page shown after characters' fetch
/api/collections/ Shows the list of all the collections fetched by the user
/api/collections/<name>/ Shows a specific collection

In order to setup the project locally, run the following commands in the project's folder:

Create a virtual environment
python3 -m venv .venv

Install dependencies
pip install -r requirements.txt

Activate virtual environment
. ./.venv/bin/activate

Apply migrations
python manage.py migrate

Run server
python manage.py runserver
