from models.site import Site

class Collection:
    # An instance of the Site class.
    site = ''

    # The language picked to view the site.
    language = ''

    # Constructor.
    def __init__(self):
        self.site = Site()
        self.language = self.site.language()

    # Returns the collection total value converted into the right country currency.
    def totalValue(self):
        if self.language == 'esp':
            self.currency = '€'
        else:
            self.currency = '£'

        return self.currency
