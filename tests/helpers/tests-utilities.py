from helpers.utilities import splitByLanguage

class TestUtilities:

    def test_split_by_language_returns_expected_string(self):
        data = 'Spanish | English'

        assert splitByLanguage(data, 'es') == (data.split(' | '))[0]
        assert splitByLanguage(data, 'en') == (data.split(' | '))[1]
