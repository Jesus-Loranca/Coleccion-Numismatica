from models.site import Site
from models.collection import Collection

# Faked google sheet data to be used in the tests.
def googleData():
    return [
        {
            'Tipo | Type': 'Moneda | Coin',
            'Nombre | Name': 'Nombre del objeto | Item name',
            'Imagen Cara | Front Image': '',
            'Imagen Dorso | Back Image': '',
            'País | Country': 'España | Spain',
            'Denominación | Denomination': '2 EUR',
            'Fecha de fabricación | Date of issue': '1992',
            'Año de la serie | Series number': '',
            'Número de Serie | Serial numbers': '',
            'Estado | Grading': 'EBC (Extraordinariamente Bien Conservada) | EF (Extremely Fine)',
            'Valor | Value': '2 EUR',
            'Coste | Cost': '6,99 EUR',
        },
        {
            'Tipo | Type': 'Moneda | Coin',
            'Nombre | Name': 'Nombre del objeto 2 | Item name 2',
            'Imagen Cara | Front Image': '',
            'Imagen Dorso | Back Image': '',
            'País | Country': 'Reino Unido | United Kingdom',
            'Denominación | Denomination': '2 GBP',
            'Fecha de fabricación | Date of issue': '1996',
            'Año de la serie | Series number': '',
            'Número de Serie | Serial numbers': '',
            'Estado | Grading': 'EBC (Extraordinariamente Bien Conservada) | EF (Extremely Fine)',
            'Valor | Value': '4 GBP',
            'Coste | Cost': '9,99 GBP',
        }
    ]

class TestCollection:
    def test_find_item_returns_expected_results(self):
        data = googleData()

        site = Site('es', '')
        collection = Collection(site)
        collection.googleData = data

        # Assert expected item by Spanish name.
        assert collection.find('Nombre del objeto 2') == data[1]

        # Assert expected item by English name.
        assert collection.find('Item name 2') == data[1]

        # Assert empty dict by wrong name.
        assert collection.find('Wrong') == {}
