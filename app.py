import json
from flask import Flask, jsonify, request, render_template
from models.site import Site
from models.item import Item
app = Flask(__name__)

# pipenv run python app.py


@app.route('/<string:language>')
def home(language):
    return 'Colección Numismática'


@app.route('/<string:language>/<string:item>/')
def item(language, item):
    googleData = {
        'Tipo | Type': 'Moneda | Coin',
        'Nombre | Name': 'Nombre del objeto | Item name',
        'Image Cara | Front Image': '',
        'Image Dorso | Back Image': '',
        'País | Country': 'Reino Unido | United Kingdom',
        'Denominación | Denomination': '2 EUR',
        'Fecha de fabricación | Date of issue': '1992',
        'Año de la serie | Series number': '',
        'Número de Serie | Serial numbers': '',
        'Estado | Grading': 'EBC (Extraordinariamente Bien Conservada) | EF (Extremely Fine)',
        'Valor | Value': '2 EUR',
        'Coste | Cost': '6,99 EUR',
    }

    item = Item(language, googleData)
    site = Site(language, item.name())

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

if __name__ == "__main__":
    # Debugger is nice for development as it restarts the server for you.
    app.run(debug=True)
