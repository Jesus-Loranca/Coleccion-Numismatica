import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from models.site import Site

class Collection:
    # Use credentials to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    credentialsFile = {
        'type':                        os.environ.get('type'),
        'project_id':                  os.environ.get('project_id'),
        'private_key_id':              os.environ.get('private_key_id'),
        'private_key':                 os.environ.get('private_key'),
        'client_email':                os.environ.get('client_email'),
        'client_id':                   os.environ.get('client_id'),
        'auth_uri':                    os.environ.get('auth_uri'),
        'auth_provider_x509_cert_url': os.environ.get('auth_provider_x509_cert_url'),
        'client_x509_cert_url':        os.environ.get('client_x509_cert_url')
    }

    credentials = ServiceAccountCredentials.from_json_keyfile_name('Coleccion Numismatica-3639760c8254.json', scope)
    # credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentialsFile, scope)
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

    # Finds an item from the google spreadsheet data based on its name.
    def find(self, name = ''):
        return next(
            (
                item for item in self.googleData
                if name in item['Nombre | Name']
            ), {}
        )

    # Returns the collection total value converted into the right country currency.
    def totalValue(self):
        return self.currency
