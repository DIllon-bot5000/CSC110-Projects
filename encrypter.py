###
### Author: Dillon Barr
### Course: CSC 110
### Description: This program takes a text file and swaps lines of the
###              file to encrypt the file. It stores the encrypted file and
###              the corresponding indexes as separate text files


import random


def get_file(file_contents, index_list):
    '''
    This function gets the user input for a text file and then writes the lines
    to a list as well as a corresponding list of indexes that represent the line
    positions.
    file_contents and index_list are both lists.
    '''
    file_name = input('Enter a name of a text file to mix:  \n')
    file = open(file_name, 'r')
    file_contents = file.readlines()
    index = 0
    while index < len(file_contents):
        file_contents[index] = file_contents[index].rstrip('\n')
        index_list.append(index + 1)
        index += 1
    return file_contents, index_list

def shuffle_file(file_contents, index_list):
    '''
    This function shuffles the lines of the text file and changes the 
    indexes to represent the new positions of the lines.
    file_contents and index_list are both lists.
    '''
    line_count = len(file_contents)
    i = 0
    while i < (line_count * 5):
        x = random.randint(0, line_count - 1)
        y = random.randint(0, line_count - 1)
        temp1 = file_contents[x]
        temp2 = file_contents[y]
        temp_index = index_list[x]
        temp_index2 = index_list[y]
        file_contents[x] = temp2
        file_contents[y] = temp1
        index_list[x] = temp_index2
        index_list[y] = temp_index
        i += 1

def save_file(file_contents, index_list):
    '''
    This function takes the shuffled lines list from the text file as well as
    the corresponding index list and writes them to separate files.
    file_contents and index_list are both lists.
    '''
    encrypted = open('encrypted.txt', 'w')
    index_key = open('index.txt', 'w')
    for i in range(len(file_contents)):
        encrypted.write(file_contents[i] + '\n')
    for i in range(len(index_list)):
        index_key.write(str(index_list[i]) + '\n')
    encrypted.close()
    index_key.close()

def main():
    random.seed(125)
    file_contents = []
    index_list = []
    file_contents, index_list = get_file(file_contents, index_list)
    shuffle_file(file_contents, index_list)
    save_file(file_contents, index_list)
    
main()
