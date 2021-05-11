###
### Author: Dillon Barr
### Course: CSC 110
### Description: This program opens a text file containing contact information and
###              allows the user to search for contacts matching input, add contacts
###              and then save the contacts to the text file upon exiting the program.



def read_file(contacts):
    '''
    This function reads in a file called contacts.txt and then 
    stores the contents into a set populated with tuples.
    Contacts is the name of the set.
    '''
    file = open('contacts.txt', 'r')
    for line in file:
        line = line.strip('\n').split(' | ')
        tuple_list = tuple(line)
        contacts.add(tuple_list)

def add_contacts(contacts):
    '''
    This function gets the user input for a new contact to 
    be put into a tuple and then added to the contacts set.
    Contacts is the name of the set.
    '''
    name = input('name: \n')
    email = input('email: \n')
    number = input('phone: \n')
    new_contact = (name, email, number)
    new_contact = tuple(new_contact)
    if new_contact in contacts:
        print('Contact already exists!')
    else:
        contacts.add(new_contact)
        print('Contact added!')
    
def search_contacts(command, contacts):
    '''
    This function takes the user input and splits it into a list.
    It then takes the item to be searched for and loops through the tuples in
    the set and prints the corresponding info if there is any. Otherwise it
    outputs 'None.'
    command is a string user input.
    contacts is the set being used.
    '''
    if 'name' in command:
        command = command.split('name ')
    elif 'email' in command:
        command = command.split('email ')
    elif 'phone' in command:
        command = command.split('phone ')
    command = command[1]
    counter = 0
    for i in contacts:
        counter += 1
        for j in i:
            if command in j:
                print(i[0] + "'s contact info:")
                print('  email: ' + i[1])
                print('  phone: ' + i[2])
                counter -= 1
    
    if counter >= len(contacts):
        print('None')
    counter = 0

def save_contacts(contacts):
    '''
    This function takes the contacts set and overwrites the existing
    contacts.txt file so it stays up to date.
    contacts is the set being used.
    '''
    contact_file = open('contacts.txt', 'w')
    for i in contacts:
        contact_file.write(i[0] + ' | ' + i[1] + ' | ' + i[2])
        contact_file.write('\n')
    contact_file.close()
    
    
    
def main():
    contacts = set()
    read_file(contacts)
    print('Welcome to the contacts app!')
    command = input('> \n')
    while command != 'exit':
        if command.startswith('show'):
            search_contacts(command, contacts)
        elif command.startswith('add'):
            add_contacts(contacts)
        else:
            print('huh?')
        command = input('> \n')
    save_contacts(contacts)
    print('Goodbye!')

            


main()