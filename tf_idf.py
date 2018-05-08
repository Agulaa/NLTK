from nltk.corpus import reuters
from nltk.stem.porter import *
from nltk.corpus import stopwords
from nltk.stem.lancaster import LancasterStemmer



__dic = dict()
__re_dic = {}
__freq = {}
__all_files = {}
__word_vector_file = {}
__binary_vector_file = {}



def preprocessig_stemming_and_lower_words(words):
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

def create_dictionary(words, iterator):
    for word in words:
        if word not in __dic:
            __dic[word] = iterator
            __re_dic[iterator] = word
            iterator += 1
            __freq[word] = 1
        else:
            __freq[word] += 1


def do_dict_for_all_file():
    iterator = 0
    i = 0
    for category in reuters.categories():
        for file in reuters.fileids(category):
            __all_files[i] = file
            words = reuters.words(file)
            lower_single = preprocessig_stemming_and_lower_words(words)
            all_word = []
            for word in lower_single:
                if word not in all_word:
                    all_word.append(word)

            __word_vector_file[file] = all_word
            i += 1
            create_dictionary(lower_single, iterator)



def create_document_word_matrix():

    for file,words in __word_vector_file.items():
        binary = []
        for index, word in __re_dic.items():
            if word not in words:
                binary.append(0)
            else:
                binary.append(1)
        __binary_vector_file[file] = binary



if __name__ == '__main__':
    do_dict_for_all_file()
    i = 0
    for k,v in __word_vector_file.items():
        print(k,v)
        if i == 5:
            break
        else: i+=1
    #print('vector \n',__word_vector_file)

    # print('Dictionary \n',__dic)
    # print('Re_dictionary \n', __re_dic)
    # print('Frequency \n', __freq)
    print('All files', len(__all_files))
