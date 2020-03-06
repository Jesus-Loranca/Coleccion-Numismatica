import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from smartfile import BasicClient
from models.site import Site
from models.item import Item

class Collection:
    # An instance of the Site class.
    site = ''

    # The language picked to view the site.
    # The default view is Spanish.
    language = 'es'

    # The currency used for the collection based on the picked language.
    # Defaults to EUR as the default view would be Spanish.
    currency = 'EUR'

    # Google Spreadsheet information.
    googleData = ''

    # SmartFile connection.
    smartFileClient = ''

    # Constructor.
    def __init__(self, site):
        self.site = site
        self.language = self.site.language

        # Retrieves the Google Spreadsheet data.
        self.googleSpreadsheet()

        # Conects to SmartFile to retrieve the images.
        self.smartFile()

        if self.language == 'en':
            self.currency = 'GBP'

    # Returns all the collection being readed from the Google Spreadsheet.
    def all(self):
        return self.googleData

    # Returns the collection as a list of Items,
    def asItems(self):
        collectionAsItems = []

        for item in reversed(self.googleData):
            if not all(property == '' for property in item.values()):
                collectionAsItems.append(Item(self.language, item))

        return collectionAsItems

    # Finds an item from the Google Spreadsheet data based on its name.
    def find(self, name = '', field = 'Nombre | Name'):
        return next(
            (
                item for item in self.googleData
                if name in item[field]
            ), {}
        )

    # Authenticates against the Google Spreadsheet to retrieve its information.
    def googleSpreadsheet(self):
        # Use credentials to create a client to interact with the Google Drive API
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        # Private key is being read wrong from the .env so its value have to be replaced
        # Locally spaces are being translated as \\\\n and heroku translates them as \\n
        privateKey = os.getenv('private_key')

        if os.getenv('environment') == 'local':
            privateKey = privateKey.replace('\\\\n', '\n')

        if os.getenv('environment') == 'production':
            privateKey = privateKey.replace('\\n', '\n')

        credentialsFile = {
            'type':                        os.getenv('type'),
            'project_id':                  os.getenv('project_id'),
            'private_key_id':              os.getenv('private_key_id'),
            'private_key':                 privateKey,
            'client_email':                os.getenv('client_email'),
            'client_id':                   os.getenv('client_id'),
            'auth_uri':                    os.getenv('auth_uri'),
            'token_uri'                  : os.getenv('token_uri'),
            'auth_provider_x509_cert_url': os.getenv('auth_provider_x509_cert_url'),
            'client_x509_cert_url':        os.getenv('client_x509_cert_url')
        }

        # In the case the credetails need to be read from a file:
        credentials = ServiceAccountCredentials.from_json_keyfile_dict(credentialsFile, scope)
        client = gspread.authorize(credentials)

        # Find a workbook by name and open the first sheet.
        sheet = client.open('Colección Numismática').sheet1

        # Extract the collection values.
        self.googleData = sheet.get_all_records()

    # Returns the SmartFile connection to be able to use it later on for images.
    def smartFile(self):
        self.smartFileClient = BasicClient(os.getenv('smartfile_api_key'), os.getenv('smartfile_api_password'))

        self.smartFileClient.put('/path/oper/mkdir/Items/Coin/United Kingdom/1997')

    # Returns the collection total value converted into the right country currency.
    def totalValue(self):
        return self.currency
