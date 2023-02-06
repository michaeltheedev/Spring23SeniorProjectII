from nltk.tokenize import word_tokenize

#Input: Sentence, paragraph, or webpage data object w/o objects (Ouput data from remove_punctuation.py)
#Output:Object containing tokenized sentence, paragraph, or webpage objects
#Functionality: Tokening inputted documents

def tokenize_docs(string_object):
    string_object_after_tokenizing = word_tokenize(string_object)
    return string_object_after_tokenizing
