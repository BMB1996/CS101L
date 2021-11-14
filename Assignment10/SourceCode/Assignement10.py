

def open_txt_file(user_file):
    while True:
        try:
            with open(user_file) as new_file:
                read_file = new_file.read()
                return read_file
        except FileNotFoundError:
            print('Could not find file: {}'.format(user_file))
        user_file = input('\nEnter a new file name: ')

def clean_text(text):
    words = text.split()
    for index in range (len(words)):
        words[index] = words[index].strip('.,')
    return words

def count_words(lst):
    dct = {}
    for word in lst:
        if len(word) > 3:
            if word.lower() in dct:
                dct[word.lower()] += 1
            elif word.lower() not in dct:
                dct[word.lower()] = 1
    return dct

def most_common_words(dct):
    new_dict = {}
    for i in range (10):
        high_count = 0
        high_word = ''
        for word in dct:
            if word in new_dict:
                pass
            elif dct[word] > high_count:
                high_count = dct[word]
                high_word = word
        new_dict[high_word] = high_count
    return new_dict

user_file = input('Enter a file: ')
my_file = open_txt_file(user_file)
words = clean_text(my_file)
word_count_dict = count_words(words)
top_words = most_common_words(word_count_dict)
print('\nMost frequently used words')
print('\n{:<5}{:<15}{:<5}'.format('#', 'Word', 'Freq.'))
print('=' * 25)
counter = 1
for word in top_words:
    print('{:<5}{:<15}{:<5}'.format(counter, word, top_words[word]))
    counter += 1
once_used = 0
for word in word_count_dict:
    if word_count_dict[word] == 1:
        once_used += 1
print('There are', once_used, 'words that occur only once.')
print('There are {} unique words.'.format(len(word_count_dict)))