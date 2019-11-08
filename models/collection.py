from models.site import Site

class Collection:
    # An instance of the Site class.
    site = ''

    # The language picked to view the site.
    # The default view is Spanish.
    language = 'esp'

    # The currency used for the collection based on the picked language.
    # Defaults to € as the default view would be Spanish.
    currency = '€'

    # Constructor.
    def __init__(self):
        self.site = Site()
        self.language = self.site.language()

        if self.language == 'eng':
            self.currency = '£'

    # Returns the collection total value converted into the right country currency.
    def totalValue(self):
        return self.currency
