# To Filter the words in a sentence or from a text file and store it in lists

def word_len_find(string, word_size):
    count = 0
    word_size = (int(word_size))
    word_list = []
    words = string.split()
    for word in words:
        if (len(word)) == word_size:
            count += 1
            word_list.append(word)

    return word_list, count, word_size


# Use this to check in a text file that contains a lot of paragraphs
string = (open('your_file.txt', 'r', encoding='utf-8')).read()

# Now to get the return value individually from a function
word_list, count, word_size = word_len_find(string, 8)

print(f'List of {word_size} letter words in the Given sentence: \n {word_list}')
print(f'Total number of {word_size} letter words in the given sentence: {count}')
