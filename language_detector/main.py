"""This is the entry point of the program."""

from languages import LANGUAGES


def detect_language(text, languages=LANGUAGES):
    """Returns the detected language of given text."""
    text_lang = "Unknown"
    # implement your solution here
    a_list = text.split()
    length_english = 0
    try:
        eng = [x for x in a_list for y in languages[2]['common_words'] if x==y]
        length_english = len(eng)
    except IndexError:
        pass
    ger = [x for x in a_list for y in languages[1]['common_words'] if x==y]
    length_german = len(ger)
    spa = [x for x in a_list for y in languages[0]['common_words'] if x==y]
    length_spanish = len(spa)
    print length_german, length_spanish
    #if x>y and x>z:
    #    text_lang = "English"
    if length_german>length_spanish and length_german>length_english:
        text_lang = "German"
    elif length_english>length_spanish and length_english>length_german:
        text_lang = "Englih"
    else:
        text_lang = "Spanish"
    return text_lang
