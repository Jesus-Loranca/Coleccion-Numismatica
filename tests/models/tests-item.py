import pytest
from models.item import Item

class TestItem:

    def test_item_returns_expected_total_value_in_spanish(self):
        item = Item([])

        assert item.name() == []
