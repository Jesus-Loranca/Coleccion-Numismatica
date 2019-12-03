import os
import json
from flask import Flask, jsonify, request, render_template
from models.site import Site
from models.collection import Collection
from models.item import Item
from helpers.utilities import splitByLanguage
app = Flask(__name__)

@app.route('/test')
def test():
    site = Site('es', 'test')
    collection = Collection(site)

    return print(collection.all())

@app.route('/')
@app.route('/<string:language>/')
def home(language = 'es'):
    site = Site(language, splitByLanguage('Inicio | Home', language))
    collection = Collection(site)
    items = collection.asItems()

    return render_template('home.html', site = site, items = items)

@app.route('/<string:language>/links-interesantes/')
@app.route('/<string:language>/interesting-links/')
def interestingLinks(language = 'es'):
    site = Site(language, splitByLanguage('Links Interesantes | Interesting Links', language))

    return render_template('interesting-links.html', site = site)

@app.route('/<string:language>/<string:item>/')
def item(language, item):
    site = Site(language, item)
    collection = Collection(site)
    item = Item(language, collection.find(item, 'Link'))
    site.title = item.name()

    return render_template('item.html', site = site, item = item)

# @app.route('/api/staff/')
# def api_staff():
#     person = request.args.get('name', False)

#     with open('staff.json') as json_file:

#         data = json.load(json_file)
#     if person:
#         data = [
#             p for p in data
#             if p['name'].lower() == person.lower()
#         ]
#         return jsonify(data)
#     else:
#         return jsonify(data)

if __name__ == "__main__" and os.environ.get('environment') == 'local':
    # Debugger is nice for development as it restarts the server for you.
    app.run(debug = True)
