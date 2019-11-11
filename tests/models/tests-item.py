import pytest
from models.item import Item

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
        'Estado | Grading': '',
        'Valor | Value': '2 EUR',
        'Coste | Cost': '6,99 EUR',
    }

class TestItem:

    def test_item_returns_expected_name_in_spanish(self):
        item = Item('esp', googleData())

        assert item.name() == []
