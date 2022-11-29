# 5.2.2 basic function call
# def output_minutes_as_hours(orig_minutes):
#     print(f'{orig_minutes/60}')


# minutes = float(input())
# output_minutes_as_hours(minutes)

# 5.2.3 function call with params: converting measurements
# def print_total_inches(feet, inches):
#     print(f'Total inches: {(feet*12)+inches}')

# feet = int(input())
# inches = int(input())
# print_total_inches(feet, inches)

# 5.3.1 temperature conversion
# def c_to_f():
#     return  temp_c*(9/5)+32

# temp_c = float(input('Enter temperature in Celsius: '))
# temp_f = None

# temp_f = c_to_f()

# print('Fahrenheit:' , temp_f)

# 5.3.2 function call in expression
# def find_max(num_1, num_2):
#    max_val = 0.0

#    if (num_1 > num_2):  # if num1 is greater than num2,
#       max_val = num_1   # then num1 is the maxVal.
#    else:                # Otherwise,
#       max_val = num_2   # num2 is the maxVal
#    return max_val

# max_sum = 0.0

# num_a = float(input())
# num_b = float(input())
# num_y = float(input())
# num_z = float(input())

# max_sum = find_max(num_a,num_b) + find_max(num_y, num_z)

# print('max_sum is:', max_sum)

# 5.3.3 function definition: Volumne of a pyramid
# def calc_pyramid_volume(length, width, height):
#     base_area = length*width
#     return base_area*height*(1/3)

# length = float(input())
# width = float(input())
# height = float(input())
# print('Volume for', length, width, height, "is:", calc_pyramid_volume(length, width, height))

# 5.5.1 functions: factoring out a unit-conversion calculation
'''
Write a function so that the main program below can be replaced by the simpler code that calls function mph_and_minutes_to_miles(). Original main program:
miles_per_hour = float(input())
minutes_traveled = float(input())
hours_traveled = minutes_traveled / 60.0
miles_traveled = hours_traveled * miles_per_hour

print('Miles: {:f}'.format(miles_traveled))

Sample output with inputs: 70.0 100.0

Miles: 116.666667
'''
# def mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):
#     hours_traveled = minutes_traveled / 60.0
#     miles_traveled = hours_traveled * miles_per_hour
#     return miles_traveled

# miles_per_hour = float(input())
# minutes_traveled = float(input())

# print('Miles: {:f}'.format(mph_and_minutes_to_miles(miles_per_hour, minutes_traveled)))

# 5.6.1 function stubs: statistics
# def get_user_num():
#     print('FIXME: Finish get_user_num()')
#     return -1

# def compute_avg(*args):
#     print('FIXME: Finish compute_avg()')
#     return -1

# user_num1 = 0
# user_num2 = 0
# avg_result = 0

# user_num1 = get_user_num()
# user_num2 = get_user_num()
# avg_result = compute_avg(user_num1, user_num2)

# print('Avg:', avg_result)

# 5.7.1 function example
# def calc_ebay_fee(sell_price):
#     """Returns the fees charged by ebay.com given the selling
#     price of fixed-price books, movies, music, or video games.
#     fee is $0.50 to list plus 13% of selling price up to $50.00,
#     5% of amount from $50.01 to $1000.00, and
#     2% for amount $1000.01 or more."""

#     p50 = 0.13  # for amount $50 and lower
#     p50_to_1000 = 0.05  # for $50.01-$1000
#     p1000 = 0.02  # for $1000.01 and higher
#     fee = 0.50  # fee to list item

#     if sell_price <= 50:
#         fee  = fee + (sell_price*p50)
#     elif sell_price <= 1000:
#         fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
#     else:
#         fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
#                   + ((sell_price-1000)*p1000)

#     return fee

# selling_price = float(input('Enter item selling price (ex: 65.00): '))
# print('eBay fee: $', calc_ebay_fee(selling_price))

# 5.7.2 analyzing numbers
# size = 5

# def get_numbers(num):
#     numbers = []
#     user_input = input('Enter {} integers:\n'.format(num))

#     i = 0
#     for token in user_input.split():
#         number = int(token)     # Convert string input into integer
#         numbers.append(number)  # Add to numbers list

#         print(i, number)
#         i += 1

#     return numbers

# def print_all_numbers(numbers):
#     # Print numbers
#     print('Numbers:')

# def print_odd_numbers(numbers):
#     # Print all odd numbers
#     print('Odd numbers:')

# def print_negative_numbers(numbers):
#     # Print all negative numbers
#     print('Negative numbers:')

# nums = get_numbers(size)
# print_all_numbers(nums)
# print_odd_numbers(nums)
# print_negative_numbers(nums)

# 5.7.1 function with branch popcorn
# def print_popcorn_time(bag_ounces):
#     if 3 <= bag_ounces <= 10:
#         print(f'{6*bag_ounces} seconds')
#     elif bag_ounces < 3:
#         print('Too small')
#     else:
#         print('Too large')

# user_ounces = int(input())
# print_popcorn_time(user_ounces)

# 5.7.2 function with loop shampoo
'''
Write a function shampoo_instructions() with parameter num_cycles. 
If num_cycles is less than 1, print "Too few.". If more than 4, print "Too many.". 
Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number, followed by "Done.".

Sample output with input: 2

1 : Lather and rinse.
2 : Lather and rinse.
Done. 
'''
# def shampoo_instructions(num_cycles):
#     if num_cycles < 1:
#         print('Too few.')
#     elif num_cycles > 4:
#         print('Too many.')
#     else:
#         for N in range(num_cycles):
#             print(f'{N+1} : Lather and rinse.')
#         print('Done.')

# user_cycles = int(input())
# shampoo_instructions(user_cycles)

# 5.9.1 function errors: copying one function to create another
# def celsius_to_kelvin(value_celsius):
#     value_kelvin = 0.0

#     value_kelvin = value_celsius + 273.15
#     return value_kelvin

# def kelvin_to_celsius(value_kelvin):
#     value_celsius = 0.0

#     value_celsius = value_kelvin - 273.15
#     return value_celsius

# value_c = 10.0
# print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')

# value_k = float(input())
# print(value_k, 'K is', kelvin_to_celsius(value_k), 'C')

# 5.12.1 list argument modification
# def add_grade(student_grades):
#     print('Entering grade. \n')
#     name, grade = input(grade_prompt).split()
#     student_grades[name] = grade

# #Create delete_name function
# def delete_name():
#     print('Deleting grade.\n')
#     name = input(delete_prompt)
#     del student_grades[name]

# #Create print_grades function
# def print_grades():
#     print('Printing grades.\n')
#     for name, grade in student_grades.items():
#         print(name, 'has a', grade)


# student_grades = {}  # Create an empty dict
# grade_prompt = "Enter name and grade (Ex. 'Bob A+'):\n"
# delete_prompt = "Enter name to delete:\n"
# menu_prompt = ("1. Add/modify student grade\n"
#                "2. Delete student grade\n"
#                "3. Print student grades\n"
#                "4. Quit\n\n")

# command = input(menu_prompt).lower().strip()

# while command != '4':  # Exit when user enters '4'
#     if command == '1':
#         add_grade(student_grades)
#     elif command == '2':
#         delete_name()
#     elif command == '3':
#         print_grades()
#     else:
#         print('Unrecognized command.\n')

#     command = input().lower().strip()

# 5.12.1 change order of elements in function list argument
# def swap(values_list):
#     first = values_list[0]
#     last = values_list[-1]
#     values_list[0] = last
#     values_list[-1] = first
#     return values_list

# values_list = input().split(',')  # Program receives comma-separated values like 5,4,12,19
# print(values_list)
# swap(values_list)

# print(values_list)

# 5.13.1 return number of pennies in total
# def number_of_pennies(dollars, pennies=0):
#     return (dollars*100) + pennies

# print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
# print(number_of_pennies(int(input())))               # Dollars only

# 5.13.2 default params. calculate splitting a check between diners
# FIXME: Write the split_check function. HINT: Calculate the amount of tip and tax,
# add to the bill total, then divide by the number of diners.

# def split_check(amount, num_people, tax_percentage=0.09, tip_percentage=0.15):
#     return round((amount + (amount*tip_percentage) + (amount*tax_percentage))/num_people,2)

# bill = float(input())
# people = int(input())

# # Cost per diner at the default tax and tip percentages
# print('Cost per diner:', split_check(bill, people))

# bill = float(input())
# people = int(input())
# new_tax_percentage = float(input())
# new_tip_percentage = float(input())

# # Cost per diner at different tax and tip percentages
# print('Cost per diner:', split_check(bill, people, new_tax_percentage, new_tip_percentage))

# 5.17.1 function to compute gas volume

# gas_const = 8.3144621

# def compute_gas_volume(pressure, temperature, moles):
#     return (moles*gas_const*temperature)/pressure

# gas_pressure = float(input())
# gas_moles = float(input())
# gas_temperature = float(input())
# gas_volume = 0.0

# gas_volume = compute_gas_volume(gas_pressure, gas_temperature, gas_moles)
# print('Gas volume:', gas_volume, 'm^3')

# 5.18 lab: swapping variables
# def swap_values(val1, val2):
#     temp1 = val1
#     temp2 = val2
#     return (temp2, temp1)

# if __name__ == '__main__':
#     user_val1 = int(input())
#     user_val2 = int(input())
#     user_val1, user_val2 = swap_values(user_val1, user_val2)
#     print(f'{user_val1} {user_val2}')

# 5.19 lab: exact change - functions
def exact_change(val):
    remainder = val
    dollars = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    if remainder >= 100:
        dollars = (remainder - (remainder % 100))/100
        remainder -= dollars * 100
        dollars = round(dollars)

    if 25 <= remainder < 100:
        quarters = (remainder - (remainder % 25))/25
        remainder -= quarters * 25
        quarters = round(quarters)

    if 10 <= remainder < 25:
        dimes = (remainder - (remainder % 10))/10
        remainder -= dimes * 10
        dimes = round(dimes)

    if 5 <= remainder < 10:
        nickels = (remainder - (remainder % 5))/5
        remainder -= nickels * 5
        nickels = round(nickels)

    if 1 <= remainder < 5:
        pennies = round(remainder)

    return (dollars, quarters, dimes, nickels, pennies)


if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(
        input_val)

    if exact_change(input_val) == None:
        print('no change')
    else:
        if num_dollars > 0:
            print(f"{num_dollars} dollar{'s'[:num_dollars^1]}")
        if num_quarters > 0:
            print(f"{num_quarters} quarter{'s'[:num_quarters^1]}")
        if num_dimes > 0:
            print(f"{num_dimes} dime{'s'[:num_dimes^1]}")
        if num_nickels > 0:
            print(f"{num_nickels} nickel{'s'[:num_nickels^1]}")
        if num_pennies > 0:
           text = 'penny' if num_pennies == 1 else 'pennies'
           print(f'{num_pennies} {text}')
        if sum([num_dollars, num_quarters, num_dimes, num_nickels, num_pennies]) <= 0:
            print('no change')