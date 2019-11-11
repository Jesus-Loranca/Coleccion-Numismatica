# Split the Google Data returning the one requested in the view based on it's language.
def splitByLanguage(googleData, language):
    if language == 'eng':
        return (googleData.split(' | '))[1]

    return (googleData.split(' | '))[0]
