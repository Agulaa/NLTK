from nltk.corpus import reuters
from nltk.stem.porter import *
from nltk.corpus import stopwords



__dic = dict()
__re_dic = {}
__freq = {}
__word_freq_vector_file = {}
__freq_vector_file = {}
__all_freq = {}


def preprocessing(words):
    #delete ending
    stemmer = PorterStemmer()
    singles = [stemmer.stem(word) for word in words]

    #to lower all word
    lower_single_words = [word.lower() for word in singles]

    # delte stop words
    stop_words = set(stopwords.words('english'))
    words_without_stop = [word for word in lower_single_words if not word in stop_words]

    #removing punctuations
    clean_words = [word for word in words_without_stop if word.isalpha() or word.isdigit() or word.isalnum()]
    return  clean_words



def create_global_dictionary_words(words, iterator):
    #do global dictionary with all words in corups
    for word in words:
        if word not in __dic:
            __dic[word] = iterator
            __re_dic[iterator] = word
            iterator += 1

def create_gloal_dictionary_freq_word_file(words, file):
    all_freq = {}
    for word in words:
        if word not in all_freq:
            all_freq[word] = 1
        else:
            all_freq[word] += 1

    __word_freq_vector_file[file] = all_freq



def do_dicts_for_all_file():
    #fill global dict with words and fill global dic freq and fill
    iterator = 0
    i = 0
    for category in reuters.categories():
        for file in reuters.fileids(category):
            words = reuters.words(file)
            clean_words = preprocessing(words)
            create_global_dictionary_words(clean_words, iterator)
            create_gloal_dictionary_freq_word_file(clean_words,file)


def create_document_word_freq_matrix():
    for file, words in __word_freq_vector_file.items():
        vec = []
        for index, w in __re_dic.items():
            if w in words:
                vec.append(words[w])
            else:
                vec.append(0)
        __freq_vector_file[file] = vec



if __name__ == '__main__':
    do_dicts_for_all_file()
    create_document_word_freq_matrix()



