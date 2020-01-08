from helpers.utilities import splitByLanguage
from helpers.utilities import stringToURL
from helpers.utilities import prepareItemLink

class TestUtilities:

    def test_split_by_language_returns_expected_string(self):
        data = 'Spanish | English'

        # Split String separated by |
        assert splitByLanguage(data, 'es') == (data.split(' | '))[0]
        assert splitByLanguage(data, 'en') == (data.split(' | '))[1]

        # Split String without separator
        assert splitByLanguage('String', 'es') == 'String'

        # Split Int
        assert splitByLanguage(1992, 'es') == 1992

    def test_string_to_url_returns_expected_url(self):
        assert stringToURL('Historia del Progreso Tecnológico') == 'historia-del-progreso-tecnologico'

    def test_prepare_item_link(self):
        assert prepareItemLink('Historia del Progreso Tecnológico | Historia del Progreso Tecnológico') == 'historia-del-progreso-tecnologico | historia-del-progreso-tecnologico'
