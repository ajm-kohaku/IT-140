"""
Amber Murphy
IT-140: 22EW22
Module Two Assignment: Part A

In PyCharm, write a program that prompts the user for their name and age. 
Your program should then tell the user the year they were born. 
"""

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import datetime

current_year = datetime.date.today().year
user_name = input('What is your name? ')
user_age = int(input('How old are you? '))
user_birth_year = current_year - user_age
print('Hello {}! You were born in {}.'.format(user_name, user_birth_year))