###
### Author: Dillon Barr
### Course: CSC 110
### Description: This program decrypts a text file that contains
###              shuffled lines created by the encrypter program.


def decrypt():
    '''
    This function takes the user input to get an encrypted file as well
    as the list of indexes. It then reads the content of both into lists and 
    decrypts them and writes the result to a decrypted text file.
    '''
    file_name = input('Enter the name of a mixed text file: \n')
    index = input('Enter the mix index file: \n')
    encryped_file = open(file_name, 'r')
    index_list = open(index, 'r')
    encrypted = encryped_file.readlines()
    index_list = index_list.readlines()

    for i in range(len(encrypted)):
        encrypted[i] = encrypted[i].rstrip('\n')
        index_list[i] = int(index_list[i].rstrip('\n'))
    
    decrypted = []

    for i in range(1, len(encrypted) + 1):
        line = index_list.index(i)
        decrypted.append(encrypted[line])

    decrypted_file = open('decrypted.txt', 'w')
    for i in range(len(decrypted)):
        decrypted_file.write(decrypted[i] + '\n')
    
    decrypted_file.close()

def main():
    decrypt()
    
main()
    