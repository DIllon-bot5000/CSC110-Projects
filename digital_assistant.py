###
### Author: Dillon Barr
### Course: CSC 110
### Description: This program stores info given by the user and is
###              able to recall the info when prompted by the user.

def read_file(memory):
    '''
    This function reads in the file da.txt and stores the info in
    the dictionary named memory.
    '''
    file = open('da.txt', 'r')
    for line in file:
        line = line.strip('\n')
        components = line.split('|')
        question = components[0] + ' ' + components[1]
        answer = components[2]
        memory[question] = answer
    return memory

def store_data(statement, memory):
    '''
    This function splits the user input and stores it in the
    dictionary for later use.
    statement is a string made up of user input.
    memory is the dictionary used to store everything.
    '''
    print('DA: OK!')
    if 'is' in statement:
        statement = statement.split('is ')
        statement[0] += 'is'
        key = statement[0]
        value = statement[1]
        memory[key] = value
        return memory
    elif 'was' in statement:
        statement = statement.split('was ')
        statement[0] += 'was'
        key = statement[0]
        value = statement[1]
        memory[key] = value
        return memory
    elif 'will be' in statement:
        statement = statement.split('will be ')
        statement[0] += 'will be'
        key = statement[0]
        value = statement[1]
        memory[key] = value
        return memory

def answer_question(statement, memory):
    '''
    This function takes the user input and modifies it to 
    match a key in a dictionary if it exists. If it does it print the answer
    to the question. If not it replies I don't know.
    statement is a string made up of user input.
    memory is the dictionary used to store everything. 
    '''
    if 'is' in statement:
        statement = statement.strip('?')
        statement = statement.split('what is ')
        del statement[0]
        statement[0] += ' is'
        key = statement[0]
        
    elif 'was' in statement:
        statement = statement.strip('?')
        statement = statement.split('what was ')
        del statement[0]
        statement[0] += ' was'
        key = statement[0]

    elif 'will be' in statement:
        statement = statement.strip('?')
        statement = statement.split('what will be ')
        del statement[0]
        statement[0] += ' will be'
        key = statement[0]
    
    if key in memory:
        if 'my' in key:
            temp_key = key.replace('my', 'your')
            print('DA:',temp_key, memory[key])
        elif 'your' in key:
            temp_key = key.replace('your', 'my')
            print('DA:',temp_key, memory[key])
        else:
            print('DA:',key, memory[key])
    if key not in memory:
        print("DA: I don't know.")
        
    



def main():
    '''
    This function continues asking the user for input
    until the user types bye was input.
    '''
    memory = {}
    read_file(memory)
    print("DA: Hi there, let's talk. . .")
    user_input = input('USER: \n')
    while user_input != 'bye':
        if 'what' in user_input:
            answer_question(user_input, memory)
        else:
            store_data(user_input, memory)
        user_input = input('USER: \n')
    print('DA: bye!')
main()