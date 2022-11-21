# To remove all the special characters in a text file

import re


# if facing decode error use encoding=uft-8 command to resolve.

original_file = open('original_file.txt', encoding='utf-8').read()


def remove_spl_chr(original_file):
    original_string = original_file
    final_string = re.sub('[^A-Za-z0-9\s\n]', '', original_string)
    open('output.txt', 'w').write(final_string)
    text = open('output.txt')
    return text


# Replace all multiple white spaces with single white space using re module.

text = remove_spl_chr(original_file)


def remove_all_space(file):

    data = file.read().split()
    data = ' '.join(data)
    open('output.txt', 'w').write(data)
    final_file = open('output.txt', 'w').write(data)
    return  final_file


remove_all_space(text)
