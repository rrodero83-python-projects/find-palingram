"""Remove single-letter words from dictionary

:argument
-a list of words

:returns
-a list without single-letter words

"""


def cleanup(words_list):
    return [word for word in words_list if len(word) > 1]
