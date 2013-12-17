# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# November 14, 2013
# Program 4


#__________________________________________________________________________
#Purpose: This functions compresses the file. It calls a slew of other functions
#         to split the data and format it for the .cmp file then writes it.
#
#Pre-conditions: The function receives a file name from the main function.
#
#Post-conditions: The function has no return, but does create a file with a .cmp extension.
#__________________________________________________________________________
def compress(file_name):

    #Open the file and assign it a variable name.
    file = open(file_name, 'r')

    #Read the data as a string into a string variable.
    data = file.read()

    #Close the file.
    file.close()

    #Call the uwords_and_freq_parallel function to get a list of unique words and the corresponding frequencies.
    unique_words, frequencies = uwords_and_freq_parallel(data)

    #Call the sorted_by_frequencies function to sort the unique words by frequencies, highest to lowest.
    sorted_uniques = sort_by_frequencies(unique_words, frequencies)

    #Call the compress_line-list function to get the formatted string with unique words index inplace of words.
    compressed_lines = compress_line_list(data, sorted_uniques)

    #Call the assemble_final_string function to assemble the final string from the unique words and compressed lines.
    final_string = assemble_final_string(sorted_uniques, compressed_lines)

    #Open the new file to write to, open with the 'w' call for write.
    compressed_file = open(raw_file_name(file_name) + '.cmp', 'w')

    #Write the final string to the file.
    compressed_file.write(final_string)

    #Close the file.
    compressed_file.close()


#__________________________________________________________________________
#Purpose: This functions makes a list of unique words based on the data fed as well as
#         creating a frequencies list parallel to the words.
#
#Pre-conditions: The functions has one parameter, the raw data of the file.
#
#Post-conditions: The functions returns a list of unique words and a parallel list of the
#                 frequencies of each word.
#__________________________________________________________________________
def uwords_and_freq_parallel(data):

    #Create a raw data list of words split by white space.
    data_list = data.split()

    #Create a unique words empty list to append into.
    unique_words = []

    #Create a frequencies empty list to append into.
    frequencies = []

    #For each word in the raw data list...
    for word in data_list:

        #Is the word exists in the unique words list already, add one to the corresponding frequency.
        if word in unique_words:
            frequencies[unique_words.index(word)] += 1

        #Else, append the word to the unique word list and append a one to the frequency.
        else:
            unique_words.append(word)
            frequencies.append(1)

    #Return the list of unique words and the frequencies list.
    return unique_words, frequencies


#__________________________________________________________________________
#Purpose: This function sorts the unique words from highest frequency to lowest frequency.
#
#Pre-conditions: This function receives 2 parallel lists, unique_words and frequencies.
#
#Post-conditions: This function returns the unique words sorted from highest frequency to lowest.
#__________________________________________________________________________
def sort_by_frequencies(unique_words, frequencies):

    #For index number in the length of the list of words minus one...
    for i in range(len(unique_words) - 1):

        #Set the max index as the index of the max value in the list.
        max_index = frequencies[i:].index(max(frequencies[i:])) + i

        #If the index is not equal to the max index, swap the values of the max_index and the current for index value.
        if i != max_index:
            frequencies[max_index], frequencies[i] = frequencies[i], frequencies[max_index]
            unique_words[max_index], unique_words[i] = unique_words[i], unique_words[max_index]

    #Return the sorted unique words.
    return unique_words


#__________________________________________________________________________
#Purpose: This functions replaces each word with it's index in the sorted unique words.
#
#Pre-conditions: This functions receives the raw data and the sorted unique words.
#
#Post-conditions: This functions returns a string of lines of integers.
#__________________________________________________________________________
def compress_line_list(data, sorted_uniques):

    #Define a list of lines as the data split by newlines.
    list_of_lines = data.split('\n')

    #Define an empty string variable to concatenate the lines of numbers into.
    compressed_lines = ''

    #For each line in the list of lines...
    for line in list_of_lines:

        #Split each line by whitespace.
        list_of_words_in_lines = line.split()

        #For each word in the list of words in the lines...
        for word in list_of_words_in_lines:

            #Concatenate the string of the number of the index of the unique word followed by a space.
            compressed_lines += str(sorted_uniques.index(word)) + ' '

        #Concatenate a newline after each line.
        compressed_lines += '\n'

    #Return the final compressed line string.
    return compressed_lines


#__________________________________________________________________________
#Purpose: This functions assembles the final text which goes into the compressed file.
#
#Pre-conditions: The functions receives the sorted_unique words and the compressed lines as
#                parameters.
#
#Post-conditions: The functions returns a string that is the final string that will be written to
#                 the compressed file.
#__________________________________________________________________________
def assemble_final_string(sorted_uniques, compressed_lines):

    #Initialize an empty string to concatenate into.
    final_string = ''

    #Concatenate the length of the sorted unique words as the first line, then a new line.
    final_string += str(len(sorted_uniques)) + '\n'

    #For each word in teh sorted unique words...
    for word in sorted_uniques:

        #Concatenate the word folled by a newline.
        final_string += word + '\n'

    #Concatenate the compressed line to the final string.
    final_string += compressed_lines

    #Strip off the trailing white space from teh final string.
    final_string = final_string.rstrip()

    #Return the final string.
    return final_string


#__________________________________________________________________________
#Purpose: This function gets the raw file_name name by striping off the extension.
#
#Pre-conditions: The functions receives the file name as a parameter.
#
#Post-conditions: The functions returns a string with the raw file_name name.
#__________________________________________________________________________
def raw_file_name(file_name):

    #Initialize a raw_file_list varialbe that is the file_name split by the '.'.
    raw_file_list = file_name.split('.')

    #Return the 0'th index of the raw_file_list which is the file name minus the extension.
    return raw_file_list[0]


#__________________________________________________________________________
#Purpose: This functions decompressed the file based on the file name given and creates
#         a file based on the file name.
#
#Pre-conditions: The functions receives the file name as a parameter.
#
#Post-conditions: The functions returns nothing, but does create a file with the .decmp
#                 extension.
#__________________________________________________________________________
def decompress(file_name):

    #Initialize a file variable and open the file based on the file name variable.
    file = open(file_name, 'r')

    #Initialize a data variable and set it to the read file. Creates a string.
    data = file.read()

    #Close the file.
    file.close()

    #Call the recover_unique_words() function with the data as an argument to get a list of sorted unique words.
    sorted_uniques = recover_unique_words(data)

    #Call the recover_lines() functions with the data and words as arguments and assign to a variable. Creates a string.
    decompressed_lines = recover_lines(data, sorted_uniques)

    #Initialize a decompressed file, with a .decmp extension and a call to write. Creates the file.
    decompressed_file = open(raw_file_name(file_name) + '.decmp', 'w')

    #Write the decompressed lines to the decompressed file.
    decompressed_file.write(decompressed_lines)

    #Close the file.
    decompressed_file.close()


#__________________________________________________________________________
#Purpose: This functions recovers the unique words from the raw compressed data.
#
#Pre-conditions: The functions receives one parameter, the raw compressed data.
#
#Post-conditions: The functions returns a lise of sorted unique words.
#__________________________________________________________________________
def recover_unique_words(data):

    #Split the data by whitespace.
    data_list = data.split()

    #Strip off every list index except for the list of words.
    unique_words = data_list[1:int(data_list[0]) + 1]

    #Return the list of words.
    return unique_words


#__________________________________________________________________________
#Purpose: This functions recovers the actual ascii characters for decompression.
#
#Pre-conditions: The functions has 2 parameters, the raw compressed data from the decompression
#                function and the sorted unique words from teh decompression functions.
#
#Post-conditions: The functions returns a string which is the recovered ascii characters from
#                 the decompression functions.
#__________________________________________________________________________
def recover_lines(data, sorted_uniques):

    #Initialize a list of lines variable by splitting the data by newlines.
    list_of_lines = data.split('\n')

    #Reassigns the list or lines variable with the unique words striped out of the list.
    list_of_lines = list_of_lines[int(list_of_lines[0]) + 1:]

    #Initialize an empty string variable to store the decompression text.
    decompressed_lines = ''

    #For each line in the list of lines...
    for line in list_of_lines:

        #Split each line into a list of strings, which are the indices of th unique words.
        list_of_words_in_lines = line.split()

        #For each word in each line...
        for word in list_of_words_in_lines:

            #Concatenate the corresponding word based on the number in it's place followed by a space.
            decompressed_lines += sorted_uniques[int(word)] + ' '

        #Concatenate a newline after each line.
        decompressed_lines += '\n'

    #Return the decompressed lines.
    return decompressed_lines


#__________________________________________________________________________
#Purpose: The functions checks whether or not the file is valid for compression.
#
#Pre-conditions: The functions has one parameter, the file name.
#
#Post-conditions: The functions returns either True or False based on the file name.
#__________________________________________________________________________
def valid_compress(file_name):

    #Default result variable initialized with a value of True.
    result = True

    #Try to open the file, if an error occurs, set the result to False.
    try:
        open(file_name, 'r').read()
    except:
        result = False

    #Return the result variable.
    return result


#__________________________________________________________________________
#Purpose: This function tests whether or not the file name variable is valid for decompression.
#
#Pre-conditions: The functions has one parameter, the file name.
#
#Post-conditions: The function returns either True or False.
#__________________________________________________________________________
def valid_decompress(file_name):

    #Default result variable is initialized as True
    result = True

    #If the file name ends with '.cmp' then it tries to read the file. If an error occurs, set the result to False
    if file_name[-4:] == '.cmp':
        try:
            open(file_name, 'r').read()
        except:
            result = False

    #Else, if the file name does not end with '.cmp', set the return variable to False.
    else:
        result = False

    #Return the result variable.
    return result


#__________________________________________________________________________
#Purpose: This function gets a valid 'c' or 'd' string flag to signal the program for
#         compression or decompression.
#
#Pre-conditions: The function gets no parameters and calls no functions.
#
#Post-conditions: The functions returns a lowercase 'c' or 'd' string.
#__________________________________________________________________________
def get_c_or_d():

    #Initialize a loop flag variable as True.
    loop_flag = True

    #Ask the user for a 'c' or 'd' string variable.
    c_d = input('Enter "C" for compression or "D" for decompression: ')

    #While loop based on the loop_flag variable to get a valid 'c' or 'd'.
    while loop_flag:

        #If the input from the user is an upper or lowercase 'c' or 'd', set the loop flag variable to False.
        if c_d.lower() == 'c' or c_d.lower() == 'd':
            loop_flag = False

        #Else ask the user for a valid c_d variable.
        else:
            c_d = input('Enter a valid input; "C" for compression or "D"  for decompression: ')

    #Return the lowercase c_d variable.
    return c_d.lower()


#__________________________________________________________________________
#Purpose: This function gets a valid file name string variable from the user.
#
#Pre-conditions: The function gets one argument, a 'c' or 'd' string, and also asks the user
#                for a file name string variable.
#
#Post-conditions: The function returns a valid file name variable for compression or decompression.
#__________________________________________________________________________
def get_file(c_d):

    #Initialize a loop_flag variable and set to true.
    loop_flag = True

    #If the c_d parameter is 'c', ask for a file to be compressed and assign to file_name.
    if c_d == 'c':
        file_name = input('Enter file for compression: ')

    #Else, ask for a file to be decompressed and assign to file_name.
    else:
        file_name = input('Enter file for decompression: ')

    #While loop based on loop_flag. Tests for a valid file_name.
    while loop_flag:

        #If the c_d variable is 'c' and the valid_compress() function returns True, set the loop_flag to False.
        if c_d == 'c' and valid_compress(file_name):
            loop_flag = False

        #Elif the c_d variable is 'c' and the valid_compress() returns False, ask for a valid file_name for compression.
        elif c_d == 'c' and not valid_compress(file_name):
            file_name = input('Enter valid file name for compression: ')

        #Elif the c_d variable is 'c' and the valid_compress() returns True, set the loop flag to False.
        elif c_d == 'd' and valid_decompress(file_name):
            loop_flag = False

        #Else, ask for a valid file_name for decompression.
        else:
            file_name = input('Enter valid file for decompression: ')

    #Return the file_name variable.
    return file_name


#__________________________________________________________________________
#Purpose: This program is used to compress and decompress files.
#
#Pre-conditions: The program calls functions that get the user to enter in a 'c' or 'd' for
#                compression or decompression and a file name for the same.
#
#Post-conditions: The program outputs either a compressed or decompressed file based on user
#                 input.
#__________________________________________________________________________
def main():

    #Print the opening message.
    print('Big Blue Compressor/Decompressor')

    #Call the get_c_or_d() function to get a valid compression or decompression string variable.
    c_d = get_c_or_d()

    #Call the get_file() function with the c_d variable to get a valid file name string.
    file_name = get_file(c_d)

    #If c_d is a 'c', call the compress function with the file_name as the argument.
    if c_d == 'c':
        compress(file_name)

    #Else, call the decompress function with the file_name as the argument.
    else:
        decompress(file_name)

    #Print completed.
    print('Completed!')


#Call main().
main()