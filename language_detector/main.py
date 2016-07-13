from languages import LANGUAGES

def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    text_lang = "Unknown"
    a_list = text.split()
    
    # For each language, check every word and see if it can be found in the
    # languages.py file, if so add that word to a list.
    # Finally, get the length of each of these lists.
    try:
        eng = [x for x in a_list for y in languages[2]['common_words'] if x==y]
        length_english = len(eng)
    except IndexError:
        length_english = 0
    ger = [x for x in a_list for y in languages[1]['common_words'] if x==y]
    length_german = len(ger)
    spa = [x for x in a_list for y in languages[0]['common_words'] if x==y]
    length_spanish = len(spa)

    # Check to see which language had the most words in the text
    if length_german>length_spanish and length_german>length_english:
        text_lang = "German"
    elif length_english>length_spanish and length_english>length_german:
        text_lang = "English"
    else:
        text_lang = "Spanish"
    return text_lang