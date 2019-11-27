from helpers.utilities import splitByLanguage

class Item:
    # The language picked to view the site.
    # The default view is Spanish.
    language = 'es'

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
        return splitByLanguage(self.googleData['Imagen Dorso | Back Image'], self.language)

    # Returns the item cost when it was initially bought.
    def cost(self):
        return splitByLanguage(self.googleData['Coste | Cost'], self.language)

    # Returns the item country.
    def country(self):
        return splitByLanguage(self.googleData['País | Country'], self.language)

    # Returns the item date of issue.
    def date(self):
        return splitByLanguage(self.googleData['Fecha de fabricación | Date of issue'], self.language)

    # Returns the item currency.
    def denomination(self):
        return splitByLanguage(self.googleData['Denominación | Denomination'], self.language)

    # Returns the item front image URL.
    def frontImage(self):
        return splitByLanguage(self.googleData['Imagen Cara | Front Image'], self.language)

    # Returns the item grading.
    def grading(self):
        return splitByLanguage(self.googleData['Estado | Grading'], self.language)

    # Returns the item's page link.
    def link(self):
        return splitByLanguage(self.googleData['Link'], self.language)

    # Returns the item link to its mint page.
    def mintLink(self):
        return splitByLanguage(self.googleData['Link de la Ceca | Mint\'s Link'], self.language)

    # Returns the item name.
    def name(self):
        return splitByLanguage(self.googleData['Nombre | Name'], self.language)

    # Returns the item serial number.
    # Only bank notes have one.
    def serialNumber(self):
        return splitByLanguage(self.googleData['Número de Serie | Serial numbers'], self.language)

    # Returns the item series number.
    # Only bank notes have one.
    def seriesNumber(self):
        return splitByLanguage(self.googleData['Año de la serie | Series number'], self.language)

    # Returns the item type.
    # It would Bank Note or Coin.
    def type(self):
        return splitByLanguage(self.googleData['Tipo | Type'], self.language)

    # Returns the item value.
    def value(self):
        return splitByLanguage(self.googleData['Valor | Value'], self.language)
