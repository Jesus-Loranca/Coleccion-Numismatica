from helpers.utilities import stringToURL

class Site:
    # The language picked to view the site.
    # The default view is Spanish.
    language = 'es'

    # The page name.
    # It would be different depending on the view and the language.
    title = ''

    # Constructor.
    def __init__(self, language, pageName):
        self.language = language
        self.title = pageName

    # Returns the name of the site.
    # It is thought to be used on the SEO title.
    def name(self):
        if self.language == 'en':
            return 'Numismatic Collection'

        return 'Colección Numismática'

    # Builds the page URL for the language change buttons.
    def pageURL(self, language = 'es'):
        page = self.title.lower()

        if page == 'inicio' or page == 'home':
            page = ''

        return 'http://127.0.0.1:5000/' + language + '/' + stringToURL(page)
