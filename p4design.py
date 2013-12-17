# Prolog
# Author: David Yurek
# Email: dayure2@g.uky.edu
# Section: 012
# Nov. 21, 2013
# Programming Assignment 4 Design


#Define a list sorter function with 2 parameters(lists), frequencies and unique words:
    #Initialize a new blank list for sorted words.
    #Initizlize a new blank list for sorted frequencies.
    #For loop to sort the frequencies from highest to lowest.
        #Initialize max variable to the value of the max value in the frequencies list.
        #Append the sorted frequencies list with the max value.
        #Append the sorted unique word list with the index of the unique words list equal to the index of the frequency.
        #Pop off the max value from the frequency list.
    #Return 2 lists, sorted frequencies and sorted unique words.


#Define compressor function with one string parameter (file_name):

    #Initialize a file_to_compress variable with an open() call with arguments file_name and 'r' for read.
    #Initialize a data variable and set it equal to the .read() call on the file_to_compress variable.
    #Close the file.
    #Initialize a list variable and set equal to the data split by white space.
    #Initialize a list variable to keep track of lines. Set equal to data split by new lines.
    #Initialize a list variable and set equal to a blank list to add unique words to.
    #Initialize a list variable to keep track of the frequency of the words.
    #Initialize final string.
    #For loop to iterate over every item in the data list.
        #If a word is in the unique word list:
            #Add one to the value of the index of the unique word list in the frequency list.
        #Else:
            #Append the unique word list with the word from the data list.
            #Append a one to the frequency list.
    #For loop to iterate through line list.
        #Line list index equals line list index split  on white space making a list of lists.
        #For loop to iterate through each index of the line list.
            #Line list index's index equals the index of the word in the unique word list.
    #Call the sort list function with and pass it the unique words list and frequencies list. 2 return values, 2 lists
    #   that will be stored in 2 new list variables of sorted words and frequencies.
    #Final string is the concatenation of the length of the unique words list, sorted frequencies, sorted words, and
    #   the line list.
    #Write to .cmp file with the file_name minus the .txt extension.


#Define the decompressor function with one string parameter (file_name):
    #Initialize a file_to_decompress variable with an open() call with arguments file_name and 'r' for read.
    #Initialze a data variable and set equal to the .read() call of the file_to_decompress variable.
    #Close the file.
    #Initialize a list variable and set equal to the data variable split by white space.
    #Initialize a list variable and set equal to an empty list for the unique words.
    #Initialize a line list variable and set equal to the data split by '\n'.
    #Initialize a final string variable.
    #For loop to iterate range(1, datalist[0]+1):
        #Append unique word list with the value of the index of the data list based on the for loop.
    #Slice off the number of lines of the index of the data list variable +1.
    #For loop to turn each line list value into a list of its own:
        #For each line value of each index of that list:
            #Concatenate the final string variable with the unique word index of the list value followed by a space.
        #Slice off the last space.
        #Add in a new line.
    #Write to .txt file with the file_name minus the .cmp extension.


#Define main():
    #Print opening message.
    #Initialize a c_d string variable. Set equal to input from user from compression prompt: 'c' or 'd'
    #Initialize a loop flag set equal to True:
        #While loop flag is true:
            #If lowercase c_d == 'c':
                #Print 'Compress'
                #Initialize file_name equal to the string input from the user.
                #If file is valid for compression:
                    #Call compression function with argument equal to the file name.
                    #Loop flag to False.
                    #Print completed.
            #Elif lowercase c_d == 'd'
                #Print 'Decompress'
                #Initialize file_name equal to the string input from the user.
                #If file is valid for decompression:
                    #Call decompression function with argument equal to the file name.
                    #loop flag = False
                    #Print completed
            #Else:
                #Print 'Please enter c or d'

#Call main().