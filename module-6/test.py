# 6.1.1 modify a list
# user_input = input()
# short_names = user_input.split()

# del short_names[0]
# short_names[-1] = 'Joe'

# print(short_names)

# 6.2.1 amusement park ride reservation system
# riders_per_ride = 3  # Num riders per ride to dispatch

# line = []  # The line of riders
# num_vips = 0  # Track number of VIPs at front of line

# menu = ('(1) Reserve place in line.\n'  # Add rider to line
#         '(2) Reserve place in VIP line.\n'  # Add VIP
#         '(3) Dispatch riders.\n'  # Dispatch next ride car
#         '(4) Print riders.\n'
#         '(5) Exit.\n\n')

# user_input = input(menu).strip().lower()

# while user_input != '5':
#     if user_input == '1':  # Add rider
#         name = input('Enter name:').strip().lower()
#         print(name)
#         line.append(name)

#     elif user_input == '2':  # Add VIP
#         line.insert(num_vips, name)
#         num_vips += 1
#         # Add new rider behind last VIP in line
#         # Hint: Insert the VIP into the line at position num_vips.
#         # Don't forget to increment num_vips.

#     elif user_input == '3':  # Dispatch ride
#         for rider in range(riders_per_ride):
#             if len(line) > 0:
#                 del line[0]
#             if num_vips > 0:
#                 num_vips -= 1
#         # Remove last riders_per_ride from front of line.
#         # Don't forget to decrease num_vips, if necessary.

#     elif user_input == '4':  # Print riders waiting in line
#         print('{} person(s) waiting:'.format(len(line)), line)

#     else:
#         print('Unknown menu option')

#     user_input = input('Enter command: ').strip().lower()
#     print(user_input)

# 6.2.1 reverse sort of list
# user_input = input()
# short_names = user_input.split()

# short_names.sort()
# short_names.reverse()

# print(short_names)

# 6.3.1 Guest user guesses
# num_guesses = int(input())
# user_guesses = []

# for num in range(num_guesses):
#     user_guesses.append(int(input()))

# print('user_guesses:', user_guesses)

# 6.3.2 sum extra credit
# user_input = input()
# test_grades = list(map(int, user_input.split())) # test_grades is an integer list of test scores


# sum_extra = 0 # Initialize 0 before your loop

# for grade in test_grades:
#     if grade > 100:
#         sum_extra+= grade - 100


# print('Sum extra:', sum_extra)

# 6.3.3 hourly temperature reporting
# user_input = input()
# hourly_temperature = user_input.split()

# print('{} '.format(' -> '.join(hourly_temperature)))

# 6.5.1 print multiplication table
# user_input= input()
# lines = user_input.split(',')

# # This line uses a construct called a list comprehension, introduced elsewhere,
# # to convert the input string into a two-dimensional list.
# # Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

# mult_table = [[int(num) for num in line.split()] for line in lines]

# for row in mult_table:
#     print(' | '.join(map(str, row)))

# 6.7.3 list modification
# nums = [10, 20, 30, 40, 50]

# for pos, value in enumerate(nums):
#     tmp = value / 2
#     if (tmp % 2) == 0:
#         nums[pos] = tmp

# print(nums[1])

# 6.8.1 list comprehensions
# row 1
# my_list = [-5, -4, -3]
# for i in range(len(my_list)):
#     my_list[ i ] += 10
# print(my_list)

# my_list = [-5, -4, -3]
# my_list = [(i+10) for i in my_list]
# print(my_list)

# row 2
# my_list = [5, 10, 20]
# for i in range(len(my_list)):
#     my_list[ i ] = str(my_list[ i ])
# print(my_list)

# my_list = [5, 10, 20]
# my_list = [float(i) for i in my_list]
# print(my_list)

# row 3
# inp = input('Enter numbers:')
# my_list = []
# for i in inp.split():
#     my_list.append(int(i))
# print(my_list)

# inp = input('Enter numbers:')
# my_list = [int(i) for i in inp.split()]
# print(my_list)

# row 4
# my_list = [[5, 10], [1]]
# sum_list = []
# for row in my_list:
#     sum_list.append(sum(row))
# print(sum_list)

# my_list = [[5, 10], [1]]
# sum_list = [sum(row) for row in my_list]
# print(sum_list)

# row 5
# my_list = [[5, 10, 15], [2, 3, 16], [100]]
# sum_list = []
# for row in my_list:
#     sum_list.append(sum(row))
# min_row = min(sum_list)
# print(min_row)

# my_list = [[5, 10, 15], [2, 3, 16], [100]]
# min_row = sum([sum(row) for row in my_list])
# print(min_row)

# 6.8.3 building list comprehensions
# x = []
# my_list = [i for i in x if ((i < 0) and (i % 2 != 0))]
# print(my_list)

# 6.10.2
# import sys

# if len(sys.argv) != 3:
#     print('Usage: python myprog.py name age\n')
#     sys.exit(1)  # Exit the program, indicating an error with 1.

# name = sys.argv[1]
# age = int(sys.argv[2])

# print('Hello {}. '.format(name))
# print('{} is a great age.\n'.format(age))

# 6.14.1 dictionary example: gradebook

# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'):"
# menu_prompt = ("1. Add/modify student grade\n"
#                "2. Delete student grade\n"
#                "3. Print student grades\n"
#                "4. Quit\n")

# while True:  # Exit when user enters no input
#     command = input(menu_prompt).lower().strip()
#     if command == '1':
#         name, grade = input(grade_prompt).split()
#         student_grades[name] = grade
#     elif command == '2':
#         del student_grades[name]
#     elif command == '3':
#         print(student_grades)
#     elif command == '4':
#         break
#     else:
#         print('Unrecognized command.')

# 6.14.1 delete from dictionary
# user_input = input()
# entries = user_input.split(',')
# country_capital = {}

# for pair in entries:
#     split_pair = pair.split(':')
#     country_capital[split_pair[0]] = split_pair[1]

# if 'Prussia' in country_capital:
#     del country_capital['Prussia']


# print('Prussia deleted?', end=' ')
# if 'Prussia' in country_capital:
#     print('No.')
# else:
#     print('Yes.')

# print ('Spain deleted?', end=' ')
# if 'Spain' in country_capital:
#     print('No.')
# else:
#     print('Yes.')

# print ('Togo deleted?', end=' ')
# if 'Togo' in country_capital:
#     print('No.')
# else:
#     print('Yes.')

# print(country_capital)

# 6.15.1 dictionary methods
# my_dict = dict(bananas=1.59, fries=2.39, burger=3.50, sandwich=2.99)

# my_dict.update(dict(soda=1.49, burger=3.69))
# burger_price = my_dict.get('burger', 0)
# print(burger_price)

# my_dict['burger'] = my_dict['sandwich']
# val = my_dict.pop('sandwich')
# print(my_dict['burger'])

# 6.16.1 iterating over a dictionary

# student_grades contains scores (out of 100) for 5 assignments
# student_grades = {
#     'Andrew': [56, 79, 90, 22, 50],
#     'Nisreen': [88, 62, 68, 75, 78],
#     'Alan': [95, 88, 92, 85, 85],
#     'Chang': [76, 88, 85, 82, 90],
#     'Tricia': [99, 92, 95, 89, 99]
# }

# # Print the name and grade percentage of the student with the highest total points
# highest_grade = 0
# highest_name = ''
# # there are 5 grades for a total of 500 points
# highest_possible_total = 500
# for student, grades in student_grades.items():
#     total_points = sum(grades)
#     if total_points > highest_grade:
#         highest_grade = total_points
#         highest_name = student

# highest_percentage = highest_grade / highest_possible_total
# print(f'Student with the highest grade is: {highest_name} \n percentage points: {highest_percentage}')

# # Find the average score of each assignment
# assignment_averages = {}

# 6.16.1 report country population

# user_input = input()
# entries = user_input.split(',')
# country_pop = {}

# for pair in entries:
#     split_pair = pair.split(':')
#     country_pop[split_pair[0]] = split_pair[1]

#     country = split_pair[0]
#     pop = split_pair[1]
#     print(country, 'has', pop, 'people.')


# 6.12 LAB
'''
Statistics are often calculated with varying amounts of input data. 
Write a program that takes any number of integers as input, and outputs the average and max.
'''
# user_amounts = input()
# user_list = user_amounts.split(' ')
# amounts = list(map(int, user_list))
# average = round(sum(amounts) / len(amounts))
# greatest_amount = sorted(amounts)[-1]

# print(average, greatest_amount)

# 6.13 LAB filter and sort a list
'''
Write a program that gets a list of integers from input, 
and outputs non-negative integers in ascending order (lowest to highest). 
'''

# user_amounts = input()
# user_list = user_amounts.split(' ')
# amounts = list(map(int, user_list))

# filtered_list = filter(lambda amount: amount >=0, amounts)
# filtered_list = sorted(filtered_list)
# string_list = list(map(str,filtered_list))
# print(' '.join(string_list), end=' ')

#### 6.18 LAB word frequencies
'''
Write a program that reads a list of words. 
Then, the program outputs those words and their frequencies. 
'''

# user_words = input()
# words = list(map(str, user_words.split(' ')))

# word_dictionary = {}

# for word in words:
#     if word_dictionary.get(word) == None:
#         word_dictionary[word] = int(1)
#     else:
#         count = int(word_dictionary.get(word)) + 1
#         word_dictionary[word] = count

# for word, count in word_dictionary.items():
#     print(word, count)
# print()

#### 6.19 LAB Replacement words
'''
Write a program that replaces words in a sentence. 
The input begins with word replacement pairs (original and replacement). 
The next line of input is the sentence where any word on the original list is replaced. 
'''

user_replacement_pairs = input()
user_sentence = input()
pairs = list(map(str, user_replacement_pairs.split('   ')))

replacer_list = []

for pair in pairs:
    original_replacement = list(map(str, pair.split(' ')))
    replacer_list.append(
        {'original': original_replacement[0], 'replacement': original_replacement[1]})

replaced_sentence = user_sentence
for dict in replacer_list:
    if dict.get('original') in replaced_sentence:
        replaced_sentence = replaced_sentence.replace(
            dict.get('original'), dict.get('replacement'))

print(replaced_sentence)
