import unidecode

# Gets the item name and use the stringToURL helper to generate the link for both languages.
def prepareItemLink(string):
    names = string.split(' | ')

    return stringToURL(names[0]) + ' | ' + stringToURL(names[1])

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
