import nltk

vocab = list(nltk.corpus.cmudict.entries())

#Takes every pronunciation of the word, checks rhymes
def rhyme(word):
    word_exists = 0
    for entry, pron in vocab:
        if entry == word:
            print(word.title() + ': ' + ' '.join(pron))
            print(' '.join(checkpron(pron)) + '\n')
            word_exists = 1
    if word_exists != 1:
        print('The word is not in this dictionary')

#Returns words with same pronounciation after stress
def checkpron(rhpron):
    return [word.title() for word, pron in vocab if rhpron[stress(rhpron):] == pron[stress(pron):]]

#Checks stress indications in pronounciation, 1 = main stress 
def stress(pron):
    for phone in pron:
        for num in phone:
            if num == '1':
                return pron.index(phone)
