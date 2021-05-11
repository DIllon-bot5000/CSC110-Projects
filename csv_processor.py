###
### Author: Dillon Barr
### Course: CSC 110
### Description: This program opens a csv file containing numbers. It
###              then stores them in a 2D list and after user input can 
###              display the average, minimum or maximum value of a column.


def open_csv(csv_data, file_name):
    '''
    This function opens a csv file and then store the 
    data into a 2D list.
    csv_data is an empty list.
    file_name is the user input for a csv file.
    '''
    csv_file = open(file_name, 'r')
    for line in csv_file:
        line = line.strip('\n')
        values = line.split(',')
        num_vals = []
        for i in values:
            num_vals.append(float(i))
        csv_data.append(num_vals)

def find_average(csv_data, column):
    '''
    This function finds the average value
    of a user selected column in the list.
    csv_data is the list of values.
    column is the user selected column.
    '''
    average = 0
    value = 0
    for i in range(len(csv_data)):
        value += csv_data[i][column - 1]
    average = value / len(csv_data)
    print('The average for column', column, 'is:', average)

def find_minimum(csv_data, column):
    '''
    This function finds the minimum value
    of a user selected column in the list.
    csv_data is the list of values.
    column is the user selected column.
    '''
    min_list = []
    for i in range(len(csv_data)):
        min_list.append(csv_data[i][column - 1])
    minimum_value = min(min_list)
    print('The minimum value in column', column, 'is:', minimum_value)
    
def find_maximum(csv_data, column):
    '''
    This function finds the maximum value
    of a user selected column in the list.
    csv_data is the list of values.
    column is the user selected column.
    '''
    max_list = []
    for i in range(len(csv_data)):
        max_list.append(csv_data[i][column - 1])
    maximum_value = max(max_list)
    print('The maximum value in column', column, 'is:', maximum_value)
    
def main():
    csv_data = []
    file_name = input('Enter CSV file name: \n')
    open_csv(csv_data, file_name)
    column_number = int(input('Enter column number: \n'))
    operation = input('Enter column operation: \n')
    operation = operation.lower()
    if operation == 'avg':
        find_average(csv_data, column_number)
    elif operation == 'min':
        find_minimum(csv_data, column_number)
    elif operation == 'max':
        find_maximum(csv_data, column_number)
    else:
        print('What is a man? A miserable little pile of secrets. -Dracula')
main()