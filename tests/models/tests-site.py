import pytest
from models.site import Site


class TestSite:

    def test_site_name_returns_expected_string(self):
        site = Site('es', '')
        assert site.name() == 'Colección Numismática'

        site.language = 'random'
        assert site.name() == 'Colección Numismática'

        site.language = 'en'
        assert site.name() == 'Numismatic Collection'
