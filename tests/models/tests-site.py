import pytest
from models.site import Site


class TestSite:

    def test_site_name_returns_expected_string(self):
        site = Site('es', '')

        # Check site name when language is es.
        assert site.name() == 'Colección Numismática'

        # Check site name when language is unknown.
        site.language = 'random'
        assert site.name() == 'Colección Numismática'

        # Check site name when language is en.
        site.language = 'en'
        assert site.name() == 'Numismatic Collection'

    def test_site_page_url_returns_expected_string(self):
        site = Site('es', '')

        # Check site page URL when language is es and page is home.
        assert site.pageURL() == 'http://127.0.0.1:5000/es/'

        # Check site page URL when language is en and page is home.
        assert site.pageURL('en') == 'http://127.0.0.1:5000/en/'

        # Check site page URL when language is en and page is not home.
        site.title = 'Random Text'
        assert site.pageURL('es') == 'http://127.0.0.1:5000/es/random-text'

        # Check site page URL when language is en and page is not home.
        assert site.pageURL('en') == 'http://127.0.0.1:5000/en/random-text'
