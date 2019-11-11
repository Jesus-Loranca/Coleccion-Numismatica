class Item:
    # The language picked to view the site.
    # The default view is Spanish.
    language = 'esp'

    # Google Sheet information containing the data for the Item.
    googleData = ''

    # Constructor.
    def __init__(self, language, googleData):
        self.language = language

        # googleData sctructure:
        # {field:value, field:value}, {field:value, field:value}, {...
        self.googleData = googleData

    # Returns the item back image URL.
    def backImage(self):
        return self.googleData['Image Dorso | Back Image']

    # Returns the item cost when it was initially bought.
    def cost(self):
        return self.googleData['Coste | Cost']

    # Returns the item country.
    def country(self):
        return self.googleData['País | Country']

    # Returns the item date of issue.
    def date(self):
        return self.googleData['Fecha de fabricación | Date of issue']

    # Returns the item currency.
    def denomination(self):
        return self.googleData['Denominación | Denomination']

    # Returns the item front image URL.
    def frontImage(self):
        return self.googleData['Image Cara | Front Image']

    # Returns the item grading.
    def grading(self):
        return self.googleData['Estado | Grading']

    # Returns the item name.
    def name(self):
        return self.googleData['Nombre | Name']

    # Returns the item serial number.
    # Only bank notes have one.
    def serialNumber(self):
        return self.googleData['Número de Serie | Serial numbers']

    # Returns the item series number.
    # Only bank notes have one.
    def seriesNumber(self):
        return self.googleData['Año de la serie | Series number']

    # Returns the item type.
    # It would Bank Note or Coin.
    def type(self):
        return self.googleData['Tipo | Type']

    # Returns the item value.
    def value(self):
        return self.googleData['Valor | Value']
