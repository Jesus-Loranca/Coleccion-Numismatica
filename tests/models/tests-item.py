import pytest
from models.item import Item

# Faked google sheet data to be used in the tests.
def googleData():
    return {
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

# Wrapper to avoid repetition in the Item tests.
def itemTestsWrapper(method, dataName):
    data = googleData()
    item = Item('es', data)

    if data[dataName].find(' | ') >= 0:
        assert getattr(item, method)() == (data[dataName].split(' | '))[0]

        item.language = 'en'
        assert getattr(item, method)() == (data[dataName].split(' | '))[1]
    else:
        assert getattr(item, method)() == data[dataName]

class TestItem:
    def test_item_returns_expected_type(self):
        itemTestsWrapper('type', 'Tipo | Type')

    def test_item_returns_expected_name(self):
        itemTestsWrapper('name', 'Nombre | Name')

    def test_item_returns_expected_front_image(self):
        itemTestsWrapper('frontImage', 'Image Cara | Front Image')

    def test_item_returns_expected_back_image(self):
        itemTestsWrapper('backImage', 'Image Dorso | Back Image')

    def test_item_returns_expected_country(self):
        itemTestsWrapper('country', 'País | Country')

    def test_item_returns_expected_denomination(self):
        itemTestsWrapper('denomination', 'Denominación | Denomination')

    def test_item_returns_expected_date(self):
        itemTestsWrapper('date', 'Fecha de fabricación | Date of issue')

    def test_item_returns_expected_series_number(self):
        itemTestsWrapper('seriesNumber', 'Año de la serie | Series number')

    def test_item_returns_expected_serial_number(self):
        itemTestsWrapper('serialNumber', 'Número de Serie | Serial numbers')

    def test_item_returns_expected_grading(self):
        itemTestsWrapper('grading', 'Estado | Grading')

    def test_item_returns_expected_value(self):
        itemTestsWrapper('value', 'Valor | Value')

    def test_item_returns_expected_cost(self):
        itemTestsWrapper('cost', 'Coste | Cost')
