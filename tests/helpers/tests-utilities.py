from helpers.utilities import splitByLanguage

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
