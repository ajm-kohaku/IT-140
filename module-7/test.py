''''
#### 7.8 LAB: Word frequencies (lists)
Write a program that first reads in the name of an input file and then reads the file using the csv.reader() method. 
The file contains a list of words separated by commas. 
Your program should output the words and their frequencies (the number of times each word appears in the file) without any duplicates.
'''

# import csv
# import sys
# import os

# def word_count(words):
#     word_dictionary = {}
#     for word in words:
#         if word_dictionary.get(word) == None:
#             word_dictionary[word] = int(1)
#         else:
#             count = int(word_dictionary.get(word)) + 1
#             word_dictionary[word] = count
#     return word_dictionary

# def get_file(filename):
#     if not os.path.exists(filename):
#         print('File {} does not exist.'.format(filename))
#         sys.exit(1)

#     with open(filename, 'r') as csvfile:
#         records = []
#         for row in csv.reader(csvfile):
#             records.append(row)
#         if len(records) == 1:
#             records = records[0]
#         return records

# def print_words_from_file(filename):
#     dict = word_count(get_file(filename))
#     for word, count in dict.items():
#         print(word, count)

# print_words_from_file(input())

'''
#### 7.9 LAB: Word frequencies (dictionaries)
Write a program that first reads in the name of an input file and then reads the input file using the file.readlines() method. 
The input file contains an unsorted list of number of seasons followed by the corresponding TV show. 
Your program should put the contents of the input file into a dictionary where the number of seasons are the keys, 
    and a list of TV shows are the values (since multiple shows could have the same number of seasons).

Sort the dictionary by key (least to greatest) and output the results to a file named output_keys.txt, 
    separating multiple TV shows associated with the same key with a semicolon (;). 
    Next, sort the dictionary by values (alphabetical order), and output the results to a file named output_titles.txt.
'''
import os, sys

def get_file(filename):
    if not os.path.exists(filename):
        print('File {} does not exist.'.format(filename))
        sys.exit(1)

    with open(filename, 'r') as f:
        records = []
        for line in f.readlines():
            records.append(line.strip())
        if len(records) == 1:
            records = records[0]
        return records

def even_items(items):
    return items[1::2]

def odd_items(items):
    return items[::2]

def create_dictionary(list1, list2):
    dictionary = {}
    for i in range(len(list1)):
        if dictionary.get(list1[i]) == None:
            dictionary[list1[i]] = list2[i]
        else:
            dictionary[list1[i]] = dictionary[list1[i]] + '; ' + list2[i]
    return dictionary

def write_output_keys_file(dictionary):
    key_pairs = sorted(dictionary.items(), key=lambda key: key[0])
    with open('output_keys.txt', 'w') as file:
        for key, value in key_pairs:
            file.write(f'{int(key)}: {value}\n')

def write_output_titles_file(dictionary):
    titles = list(sort_titles(dictionary))

    with open('output_titles.txt', 'w') as file:
        for value in titles:
            file.write(f'{value}\n')

def sort_titles(dictionary):
    titles = list(dictionary.values())
    split_string = list(filter(lambda title: ';' in title, titles))
    for title in split_string:
        titles.remove(title)
        split_titles = title.split('; ')
        for split_title in split_titles:
            titles.append(split_title)
    titles.sort()
    return titles

file = get_file('file1.txt')
sorted_dictionary = create_dictionary(odd_items(file), even_items(file))

write_output_keys_file(sorted_dictionary)
write_output_titles_file(sorted_dictionary)