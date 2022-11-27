"""
Many documents use a specific format for a person's name. Write a program that reads a person's name in the following format:
firstName middleName lastName (in one line)

and outputs the person's name in the following format:
lastName, firstInitial.middleInitial.

Ex: If the input is:
Pat Silly Doe

the output is:
Doe, P.S.

If the input has the following format:

firstName lastName (in one line)

the output is:
lastName, firstInitial.

Ex: If the input is:
Julia Clark

the output is:
Clark, J.
"""

# user_name = input('Enter First Middle & Last Names: ')

# nameList = user_name.split(' ')

# output_name = ''

# if len(nameList) == 3:
#     output_name = '{}, {}.{}.'.format(
#         nameList[2], nameList[0][0], nameList[1][0])
# elif len(nameList) == 2:
#     output_name = '{}, {}.'.format(nameList[1], nameList[0][0])
# else:
#     output_name = 'Invalid name'

# print(output_name) 

"""
Write a program whose input is a string which contains a character and a phrase, and whose output indicates the number of times the character appears in the phrase.
Ex: If the input is:
n Monday
the output is:
1
Ex: If the input is:
z Today is Monday
the output is:
0
Ex: If the input is:
n It's a sunny day
the output is:
2
Case matters.

Ex: If the input is:
n Nobody

the output is:
0
n is different than N.

"""
user_input = input()

searchCharacter = user_input[0]

print(user_input[2:].count(searchCharacter))
