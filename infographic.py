###
### Author: Dillon Barr
### Course: CSC 110
### Description: This program reads in a text file and then prints out
###              an infographic showing word counts of various categories.
###

import sys
import os 
import random
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

def read_file(counts):
    '''
    This function reads in a text file and stores the unique contents into
    a dictionary labeled text.
    Counts is an empty dictionary passed in to be filled.
    '''
    file_name = input('Enter a file name to open \n')
    file = open(file_name, 'r')
    for lines in file:
        word = lines.strip('\n')
        lines = word.split()
        for i in lines:
            if i not in counts:
                counts[i] = 0
            counts[i] += 1
    unique_words = len(counts)
    return file_name, unique_words

def count_occurrences(counts):
    '''
    This function takes the counts dictionary and then stores the number of
    unique small, medium and large words as well as the most common of those words and
    the amount of times that they appear.
    '''
    small_words = 0
    medium_words = 0
    long_words = 0
    small_count = 0
    medium_count = 0
    long_count = 0
    common_small = ''
    common_medium = ''
    common_long = ''
    
    for key, value in counts.items():
        if len(key) <= 4:
            small_words += 1
            if value > small_count:
                small_count = value
                common_small = key
        elif len(key) <= 7:
            medium_words += 1
            if value > medium_count:
                medium_count = value
                common_medium = key
        else:
            long_words += 1
            if value > long_count:
                long_count = value
                common_long = key
    totals = (str(common_small) + ' (' + str(small_count) + 'x) ' + str(common_medium) 
              + ' (' + str(medium_count) + 'x) ' + str(common_long) + ' (' + str(long_count) + 'x)')
            
    return small_words, medium_words, long_words, totals
        
def count_capitals(counts):
    '''
    This function takes the counts dictionary and counts the amount of
    words that are captial vs. non-capital.
    Counts is a dictionary.
    '''
    capital = 0
    non_capital = 0
    for key, value in counts.items():
        if key[0].isupper():
            capital += 1
        else:
            non_capital += 1
    return capital, non_capital

def count_punctuation(counts):
    '''
    This function takes the counts dictionary and counts the amount of
    words that are punctualized vs. non-punctualized.
    Counts is a dictionary.
    '''
    punc_words = 0
    non_punc_words = 0
    for key, value in counts.items():
        if key.endswith('.') or key.endswith('?') or key.endswith('!') or key.endswith(','):
            punc_words += 1
        else:
            non_punc_words += 1
    return punc_words, non_punc_words
    
def print_display(file_name, unique_words, totals, small, medium, large, capital, non_capital, punc_words, non_punc_words):
    '''
    This function prints out the infographic made up of text and bar graphs showing the 
    unique words, small, medium and large words, capital and non-capital words and punctualized
    and non punctualized words. 
    '''
    gui = graphics(650, 700, 'Infographic')
    gui.rectangle(0, 0, 650, 700, 'gray34')
    gui.text(91, 30, file_name, 'turquoise3', 15)
    gui.text(197, 70, 'Total Unique Words:', 'white', 25)
    gui.text(380, 70, unique_words, 'white', 35)
    gui.text(163, 105, 'Most used words (s/m/l):', 'white', 15)
    gui.text(435, 105, totals, 'turquoise3', 15)
    gui.text(115, 140, 'Word Lengths', 'white', 16)
    gui.text(310, 140, 'Cap/Non-Cap', 'white', 16)
    gui.text(528, 140, 'Punct/Non-Punct', 'white', 16)
    gui.rectangle(51, 160, 135, ((450 / unique_words) * small),  'turquoise3')
    gui.rectangle(51, 160 + (450 / unique_words) * small, 135, (450 / unique_words) * medium, 'green')
    gui.rectangle(51, (160 + (450 / unique_words) * medium 
                  + (450 / unique_words) * small), 135, (450 / unique_words) * large, 'turquoise3')
    gui.rectangle(250, 160, 135, (450 / unique_words) * capital, 'turquoise3')
    gui.rectangle(250, 160 + (450 / unique_words) * capital, 
                  135, (450 / unique_words) * non_capital, 'green')
    gui.rectangle(450, 160, 135, (450 / unique_words) * punc_words, 'turquoise3')
    gui.rectangle(450, 160 + (450 / unique_words) 
                  * punc_words, 135, (450 / unique_words) * non_punc_words, 'green')
    gui.text(86, 170, 'small words', 'white', 10)
    gui.text(94, 170 + (450 / unique_words) * small, 'medium words', 'white', 10)
    gui.text(86, 170 + (450 / unique_words) * medium 
             + (450 / unique_words) * small, 'long words', 'white', 10)
    gui.text(285, 170, 'Capitalized', 'white', 10)
    gui.text(297, 170 + (450 / unique_words) * capital, 'Non Capitalized', 'white', 10)
    gui.text(490, 170, 'Punctualized', 'white', 10)
    gui.text(505, 170 + + (450 / unique_words) * punc_words, 'Non Punctualized', 'white', 10)

def main():
    counts = {}
    file_name = ''
    small = 0
    medium = 0
    large = 0
    capital = 0
    non_capital = 0
    punc_words = 0
    non_punc_words = 0
    unique_words = 0
    
    file_name, unique_words = read_file(counts)
    small, medium, large, totals = count_occurrences(counts)
    capital, non_capital = count_capitals(counts)
    punc_words, non_punc_words = count_punctuation(counts)
    
    print_display(file_name, unique_words, totals, small, medium, large, capital, non_capital, punc_words, non_punc_words)
    
    
main()