import unidecode

# Gets the item type, country, date, and name and use the stringToURL helper to generate the link for both languages.
def prepareItemLink(type, country, date, name):
    types     = type.split(' | ')
    countries = country.split(' | ')
    names     = name.split(' | ')

    return stringToURL(types[0]) + '/' + stringToURL(countries[0]) + '/' +  date + '/' +  stringToURL(names[0]) + ' | ' + stringToURL(types[1]) + '/' + stringToURL(countries[1]) + '/' + date + '/' + stringToURL(names[1])

# Split the Google Data returning the one requested in the view based on it's language
# if the data received is divided by |.
def splitByLanguage(data, language):
    if not isinstance(data, int) and data.find(' | ') >= 0:
        if language == 'en':
            return (data.split(' | '))[1]

        return (data.split(' | '))[0]

    return data

# Receives an string and sanitise it to generate a URL param.
def stringToURL(string):
    return unidecode.unidecode(string.strip().lower().replace(' ', '-'))
