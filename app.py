import os
import json
from flask import Flask, request, render_template
from models.site import Site
from models.collection import Collection
from models.item import Item
from helpers.utilities import splitByLanguage
from helpers.utilities import prepareItemLink

app = Flask(__name__)

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

@app.route('/<string:language>/añadir/', methods=['GET', 'POST'])
@app.route('/<string:language>/anadir-un-objeto-a-la-coleccion/', methods=['GET', 'POST'])
@app.route('/<string:language>/add/', methods=['GET', 'POST'])
@app.route('/<string:language>/add-an-item-to-the-collection/', methods=['GET', 'POST'])
def form(language = 'es'):
    site = Site(language, splitByLanguage('Añadir un Objeto a la Colección | Add an Item to the Collection', language))
    collection = Collection(site)

    # Ensure the form is being sent.
    if request.method == 'POST':
        # Upload the images first to SmartFile and once we get the URLs for the images
        # we will update our Google Spreadsheet to include that URLs.
        if not request.files['obverse'] or not request.files['reverse']:
            return render_template('form-error.html', site = site)
        else:
            # Builds the folder structure to store the image.
            filePath = 'Items/' +  splitByLanguage(request.form.get('type'), 'en') + '/' +  splitByLanguage(request.form.get('country'), 'en') + '/' +  splitByLanguage(request.form.get('date'), 'en')

            obverse = collection.smartFileClient.post('/path/data/' + filePath, file = (request.files['obverse'].filename, request.files['obverse']))

            print(obverse)

            # [{'id': 252129318, 'name': 'image3.jpg', 'path': '/Items/Coin/United Kingdom/1997/image3.jpg', 'url': '/api/2.1/path/info/Items/Coin/United%20Kingdom/1997/image3.jpg', 'links': 1, 'remote_status': None, 'size': 169711, 'items': None, 'time': '2020-03-09T09:58:53', 'created_time': '2020-03-09T09:58:53', 'isfile': True, 'isdir': False, 'owner': {'first_name': '', 'last_name': '', 'email': 'jesus.creatiboom@gmail.com', 'name': '', 'username': 'ejecutor', 'url': '/api/2.1/user/ejecutor/'}, 'acl': {'read': True, 'write': True, 'remove': True, 'list': True}, 'extension': 'jpg', 'mime': 'image/jpeg', 'tags': [], 'attributes': {}, 'has_preview': False, 'version': 0, 'lock': {'owner': None, 'islocked': False, 'id': None}, 'is_shared': False, 'uid': 113453960}]

            print(obverse['url'])

            obverseURL = collection.smartFileClient.get('/path/info', obverse['url'])

            print(obverseURL)

        # Insert our data in the Google Spreadsheet.
        # insertData = [
        #     request.form.get('type'),
        #     request.form.get('name'),
        #     request.form.get('obverse'),
        #     request.form.get('reverse'),
        #     request.form.get('country'),
        #     request.form.get('denomination'),
        #     request.form.get('date'),
        #     request.form.get('diameter'),
        #     request.form.get('composition'),
        #     request.form.get('series'),
        #     request.form.get('serial'),
        #     request.form.get('grading'),
        #     request.form.get('value'),
        #     request.form.get('cost'),
        #     prepareItemLink(request.form.get('name')),
        #     request.form.get('mint'),
        # ]

        # rowCount = len(collection.googleData)
        # collection.sheet.insert_row(insertData, rowCount + 1)

        # return render_template('form-success.html', site = site)

    return render_template('form.html', site = site)

@app.route('/<string:language>/<string:item>/')
def item(language, item):
    site = Site(language, item)
    collection = Collection(site)
    item = Item(language, collection.find(item, 'Link'))
    site.title = item.name()

    return render_template('item.html', site = site, item = item)

if __name__ == "__main__":
    if os.getenv('environment') == 'local':
        # Debugger is nice for development as it restarts the server for you.
        app.run(debug = True)

    if os.getenv('environment') == 'production':
        app.run(debug = False)
