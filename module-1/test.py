# Here you can practice and get help on the exercise to find the smallest of 3 integers. Add code to do what the comments describe.

# For each of three numbers, prompt for it to be input and assign a variable to the integer value of what was input.
user_num1 = int(input('Enter First Number: '))
user_num2 = int(input('Enter Second Number: '))
user_num3 = int(input('Enter Third Number: '))
# Add conditional logic to calculate the smallest number. Your code should work even if two or all three of the numbers are equal.
num_list = [user_num1, user_num2, user_num3]
# num_list.sort()
smallest_number = user_num1
if user_num2 >= user_num1 <= user_num3:
    smallest_number = user_num1
elif smallest_number <= user_num1 >= user_num2 <= user_num3:
    smallest_number = user_num2
elif smallest_number <= user_num1 >= user_num3 <= user_num2:
    smallest_number = user_num3
# Print the smallest number.
print('The smallest number is: {}'.format(smallest_number))
