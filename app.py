import json
from flask import Flask, jsonify, request, render_template
from models.item import Item
app = Flask(__name__)

# pipenv run python app.py


@app.route('/')
def home():
    return 'Colección Numismática'


@app.route('/<string:item>/')
def item(item):
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


    item = Item('esp', googleData)

    return render_template('item.html', item = item)

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
