# Split the Google Data returning the one requested in the view based on it's language
# if the data received is divided by |.
def splitByLanguage(googleData, language):
    if googleData.find(' | ') >= 0:
        if language == 'eng':
            return (googleData.split(' | '))[1]

        return (googleData.split(' | '))[0]
    else:
        return googleData
