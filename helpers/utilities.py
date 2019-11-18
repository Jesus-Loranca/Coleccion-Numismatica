# Split the Google Data returning the one requested in the view based on it's language
# if the data received is divided by |.
def splitByLanguage(data, language):
    if data.find(' | ') >= 0:
        if language == 'en':
            return (data.split(' | '))[1]

        return (data.split(' | '))[0]

    return data
