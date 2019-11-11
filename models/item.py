class Item:
    # Google Sheet information containing the data for the Item.
    googleData = ''

    # Constructor.
    def __init__(self, googleData):
        # googleData sctructure:
        # {field:value, field:value}, {field:value, field:value}, {...
        self.googleData = googleData

    # Returns the item back image URL.
    def backImage(self):
        return ''

    # Returns the item cost when it was initially bought.
    def cost(self):
        return ''

    # Returns the item country.
    def country(self):
        return ''

    # Returns the item currency.
    def denomination(self):
        return ''

    # Returns the item front image URL.
    def frontImage(self):
        return ''

    # Returns the item grading.
    def grading(self):
        return ''

    # Returns the item name.
    def name(self):
        return ''

    # Returns the item serial number.
    # Only bank notes have one.
    def serialNumber(self):
        return ''

    # Returns the item series number.
    # Only bank notes have one.
    def seriesNumber(self):
        return ''

    # Returns the item type.
    # It would Bank Note or Coin.
    def type(self):
        return ''

    # Returns the item creation year.
    def year(self):
        return ''

    # Returns the item value.
    def value(self):
        return ''
