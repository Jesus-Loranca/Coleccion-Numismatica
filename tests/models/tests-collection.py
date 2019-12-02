from models.site import Site
from models.collection import Collection

# Faked google sheet data to be used in the tests.
def googleData():
    return [
        {
            'Tipo | Type': '',
            'Nombre | Name': '',
            'Imagen Cara | Front Image': '',
            'Imagen Dorso | Back Image': '',
            'País | Country': '',
            'Denominación | Denomination': '',
            'Fecha de fabricación | Date of issue': '',
            'Año de la serie | Series number': '',
            'Número de Serie | Serial numbers': '',
            'Estado | Grading': '',
            'Valor | Value': '',
            'Coste | Cost': '',
            'Link': '',
            'Link de la Ceca | Mint\'s Link': '',
        },
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
            'Link': 'nombre-del-objeto | item-name',
            'Link de la Ceca | Mint\'s Link': 'https://www.google.es/',
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
            'Link': 'nombre-del-objeto-2 | item-name-2',
            'Link de la Ceca | Mint\'s Link': 'https://www.google.com/',
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

        # Assert expected value from a different field.
        assert collection.find('nombre-del-objeto-2', 'Link') == data[1]

        # Assert empty dict from a different field.
        assert collection.find('Wrong', 'Link de la Ceca | Mint\'s Link') == {}

    def test_as_item_returns_expected_results(self):
        data = googleData()

        site = Site('es', '')
        collection = Collection(site)
        collection.googleData = data

        # Assert data is turned right into a list of Items.
        assert collection.asItems()[0].name() == 'Nombre del objeto'

        # Assert data is skipped if all the fields are empty.
        assert collection.asItems()[1].name() == 'Nombre del objeto 2'

        # Assert empty list is returned when there's no data.
        collection.googleData = []
        assert collection.asItems() == []
