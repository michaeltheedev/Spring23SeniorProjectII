import re

#Input: Sentence, paragraph, or web page data object
#Output: Object containting sentence, paragraph, or web page information w/o punctuation
#Functionality: Use regular expressions to remove non-word and non-whitespace items
def remove_punctuation(string_object):
    string_object_no_punctuation = re.sub(r'[^\w\s]', '', string_object)
    return string_object_no_punctuation