# Prolog
# Author: David Yurek, Stanley McClister, Evan Whitmer
# Section: 012
# December 4, 2013
# Lab 15 Team


def get_file():
    loop_flag = True
    file_name = input('Enter file name: ')
    while loop_flag:
        file_list = file_name.split('.')
        if file_list[1] == 'txt':
            loop_flag = False
        else:
            file_name = input('Enter valid file name: ')
    return file_name


def get_doc(file_name):
    file = open(file_name, 'r')
    doc = file.read()
    file.close()
    return doc.strip()


def get_words(raw_data):
    words = raw_data.split()
    return words


def get_lines(raw_data):
    line_list = raw_data.split('\n')
    return line_list


def get_average_word_length(words, raw_data):
    characters_no_whitespace = ''.join(raw_data.split())
    #characters_no_whitespace = raw_data.replace(' ', '').replace('\n', '').replace('\t', '')
    return len(characters_no_whitespace)/len(words)


def main():
    file_name = get_file()
    raw_data = get_doc(file_name)
    characters = len(raw_data)
    words = len(get_words(raw_data))
    lines = len(get_lines(raw_data))
    average_word_length = get_average_word_length(get_words(raw_data), raw_data)
    print(characters, ' characters in the file including whitespace.')
    print(words, 'words in the file.')
    print(lines, 'lines in the file.')
    print(average_word_length, 'average words length.')


main()