class Site:
    # The language picked to view the site.
    # The default view is Spanish.
    language = 'es'

    # The page name.
    # It would be different depending on the view and the language.
    pageName = 'es'

    # Constructor.
    def __init__(self, language, pageName):
        self.language = language
        self.title = pageName

    def name(self):
        if self.language == 'en':
            return 'Numismatic Collection'

        return 'Colección Numismática'
