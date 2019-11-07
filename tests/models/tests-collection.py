import pytest
from models.collection import Collection

class TestCollection:

    def test_total_value_returns_expected_total_value_in_spanish(self):
        collection = Collection()

        assert collection.totalValue() == '200 €'
