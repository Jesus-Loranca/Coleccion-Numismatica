import gspread
from oauth2client.service_account import ServiceAccountCredentials
from models.site import Site

class Collection:
    # Use credentials to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name('Coleccion Numismatica-3639760c8254.json', scope)
    client = gspread.authorize(credentials)

    # Find a workbook by name and open the first sheet.
    sheet = client.open('Colección Numismática').sheet1

    # Extract the collection values.
    googleData = sheet.get_all_records()

    # An instance of the Site class.
    site = ''

    # The language picked to view the site.
    # The default view is Spanish.
    language = 'es'

    # The currency used for the collection based on the picked language.
    # Defaults to EUR as the default view would be Spanish.
    currency = 'EUR'

    # Constructor.
    def __init__(self, site):
        self.site = site
        self.language = self.site.language

        if self.language == 'en':
            self.currency = 'GBP'

    # Returns all the collection being readed from the google spreadsheet.
    def all(self):
        return self.googleData

    # Returns the collection total value converted into the right country currency.
    def totalValue(self):
        return self.currency
