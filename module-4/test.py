# nose = '0'  # Looks a little like a nose
# user_value = '-'

# while user_value != 'q':
#     print(' {} {} '.format(user_value, user_value))  # Print eyes
#     print('  {}  '.format(nose))  # Print nose
#     print(user_value*5)  # Print mouth
#     print('\n')

#     # Get new character for eyes and mouth
#     user_input = input("Enter a character ('q' for quit): \n")
#     user_value = user_input[0]

# print('Goodbye.\n')

# year_considered = 2020  # Year being considered
# num_ancestors = 2  # Approx. ancestors in considered year
# years_per_generation = 20  # Approx. years per generation

# user_year = int(input('Enter a past year (neg. for B.C.): '))
# print()

# while year_considered >= user_year:
#     print('Ancestors in {}: {}'.format(year_considered, num_ancestors))

#     num_ancestors = num_ancestors * 2
#     year_considered = year_considered - years_per_generation

# # 4.2.5 while loop iterations
# x = 5
# y = 18
# while y >= x:
#     print(y, end=' ')
#     y = y - x

# # infinite loop
# # x = 10
# # while x != 3:
# #     print(x, end=' ')
# #     x = x / 2

# print('\nnew line\n')
# x = 1
# y = 3
# z = 5
# while not (y < x < z):
#     print(x, end=' ')
#     x = x + 1

# num_a = 15
# num_b = 10

# while num_a != num_b:
#     if num_a > num_b:
#         num_a = num_a - num_b
#     else:
#         num_b = num_b - num_a

# print('GCD is {}'.format(num_a))

'''
Outputs average of list of positive integers
List ends with 0 (sentinel)
Ex: 10 1 6 3 0  yields (10 + 1 + 6 + 3) / 4, or 5
'''

# values_sum = 0
# num_values = 0

# curr_value = int(input())

# while curr_value > 0: # Get values until 0 (or less)
#     values_sum += curr_value
#     num_values += 1
#     curr_value = int(input())

# print('Average: {:.0f}\n'.format(values_sum / num_values))

#######
# entered_value = int(input())

# min_value = entered_value

# while entered_value > 0:
#     if entered_value < min_value:
#         min_value = entered_value
#     entered_value = int(input())

# print('Min value:', min_value, end='')

#######
# final_product = 1

# user_value = int(input())

# while user_value > 0:
#     final_product = final_product * user_value
#     user_value = int(input())

# print('Product:', final_product, end='')

#####
# entered_age = int(input())

# while (entered_age < 16 or entered_age > 30):
#     if entered_age < 16:
#         print('Very young')
#     else:
#          print('Already adult')
#     entered_age = int(input())

# print('Perfect fit', end='')

######
# import random
# random.seed(5)

# keep_going = '-'
# next_bid = 0

# while keep_going != 'n':
#    next_bid = next_bid + random.randint(1, 10)
#    print('I\'ll bid ${}!'.format(next_bid))
#    print('Continue bidding?', end=' ')
#    keep_going = input()

##############
# num_insects = int(input())

# while num_insects <= 100:
#     print(num_insects, end=' ')
#     num_insects = num_insects * 2

# '''Program that calculates savings and interest'''

# initial_savings = 5000
# interest_rate = 0.03

# print('Initial savings of ${}'.format(initial_savings))
# print('at {:.0f}% yearly interest.\n'.format(interest_rate*100))

# years = int(input('Enter years: '))
# print()

# savings = initial_savings
# i = 1  # Loop variable
# while i <= years:  # Loop condition
#     print(' Savings at beginning of year {}: ${:.2f}'.format(i, savings))
#     savings = savings + (savings*interest_rate)
#     i = i + 1  # Increment loop variable

# print('\n')

# ''''print the us presidental election years from 1972 to present day'''
# import datetime
# year = 1792
# current_year = datetime.date.today().year

# while year <= current_year:
#     # Print the election year
#     print(year)
#     year = year + 4

####
# i = 1
# while i <= 9:
#     print(i)
#     i = i + 2

####
# N = int(input())  # Read user-entered number
# total = N
# # Initialize the loop variable
# i = total - 1
# while i >= 1:
#     # Set total to total * (i)
#     # Decrement i
#     total *= i
#     i -=1
# print(total)

#########
# i = 1

# user_num = int(input()) # Assume positive

# while i <= user_num:
#     print(i)
#     i+=1

################
# num_printed = 0

# num_stars = int(input())
# while num_printed < num_stars:
#     print('*')
#     num_printed += 1

##############
# stock_prices = input().split()

# for price in stock_prices:
#     print('$', price)

################
# contact_emails = {
#     'Sue Reyn': 's.reyn@email.com',
#     'Mike Filt': 'mike.filt@bmail.com',
#     'Nate Arty': 'narty042@nmail.com'
# }

# new_contact = input()
# new_email = input()
# contact_emails[new_contact] = new_email

# for contact, email in contact_emails.items():
#     print('{0} is {1}'.format(contact, email))

######################
# c1 = 'a'
# while c1 < 'b':
#     c2 = 'a'
#     while c2 <= 'c':
#         print('{}{}'.format(c1, c2), end=' ')
#         c2 = chr(ord(c2) + 1)
#     c1 = chr(ord(c1) + 1)

##############################
# i1 = 1
# while i1 < 19:
#     i2 = 3
#     while i2 <= 9:
#         print('{}{}'.format(i1,i2), end=' ')
#         i2 = i2 + 3
#     i1 = i1 + 10

######################
# num_rows = int(input())
# num_cols = int(input())

# for row in range(0,num_rows):
#     for col in range(0,num_cols):
#         print('*', end=' ')
#     print()

#################
# num_rows = int(input())
# num_cols = int(input())

# # Note 1: You will need to declare more variables
# # Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

# for row in range(1,num_rows+1):
#     for col in range(1,num_cols+1):
#         print('{}{}'.format(row, chr(ord('@')+col)),end=' ')

# print()

##############
# user_input = input('Enter phone number:\n')
# phone_number = ''

# for character in user_input:
#     if ('0' <= character <= '9') or (character == '-'):
#         phone_number += character
#     elif ('a' <= character.lower() <= 'c'):
#         phone_number += '2'
#     elif ('d' <= character.lower() <= 'f'):
#         phone_number += '3'
#     elif ('g' <= character.lower() <= 'i'):
#         phone_number += '4'
#     elif ('j' <= character.lower() <= 'l'):
#         phone_number += '5'
#     elif ('m' <= character.lower() <= 'o'):
#         phone_number += '6'
#     elif ('p' <= character.lower() <= 's'):
#         phone_number += '7'
#     elif ('t' <= character.lower() <= 'v'):
#         phone_number += '8'
#     elif ('w' <= character.lower() <= 'z'):
#         phone_number += '9'

    
#     #FIXME: Add remaining elif branches
#     else:
#         phone_number += '?'

# print('Numbers only: {}'.format(phone_number))

###########
# a=4
# b=5
# c=20
# mult = 0
# while a < 10:
#     mult = b * a
#     if mult > c:
#         break
#     a = a + 1
# z = a
# print(z)

################
# user_score = 0
# simon_pattern = input()
# user_pattern  = input()

# for index in range(len(simon_pattern)):
#     if user_pattern[index] == simon_pattern[index]:
#         user_score +=1
#     else:
#         break
# print('User score:', user_score)

'''
user_score = 0
simon_pattern = 'RRGBRYYBGY'
user_pattern  = 'RRGBBRYBGY'
for i in range(len(simon_pattern)):
    if user_pattern[i] == simon_pattern[i]:
        user_score += 1
'''

###################
# x = 0
# y = 5
# z = 10
# while x < y:
#     if x == z:
#         print('x == z')
#         break
#     x += 1 
# else:
#     print('x == y')

##################
