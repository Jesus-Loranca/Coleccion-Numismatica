import os
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

    # Returns the site domain taken from the env vars.
    def domain(self):
        return os.environ.get('domain')

    # Builds the page URL for the language change buttons.
    def pageURL(self, language = 'es'):
        page = self.title.lower()

        if page == '' or page == 'inicio' or page == 'home':
            return os.environ.get('domain') + language + '/'

        return os.environ.get('domain') + language + '/' + stringToURL(page) + '/'
