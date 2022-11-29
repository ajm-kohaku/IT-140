# Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. 
# The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies. 

user_pennies = int(input('Amount in pennies: '))
remainder = user_pennies

if remainder == 0:
    print('No change')

if remainder >= 100:
    dollars = (remainder - (remainder % 100))/100
    remainder -= dollars * 100
    if dollars == 1:
        print('1 Dollar')
    else:
        print('{} Dollars'.format(round(dollars)))

if 25 <= remainder < 100:
    quarters = (remainder - (remainder % 25))/25
    remainder -= quarters * 25
    if quarters == 1:
        print('1 Quarter')
    else:
        print('{} Quarters'.format(round(quarters)))

if 10 <= remainder < 25:
    dimes = (remainder - (remainder % 10))/10
    remainder -= dimes * 10
    if dimes == 1:
        print('1 Dime')
    else:
        print('{} Dimes'.format(round(dimes)))

if 5 <= remainder < 10:
    nickels = (remainder - (remainder % 5))/5
    remainder -= nickels * 5
    if nickels == 1:
        print('1 Nickel')
    else:
        print('{} Nickels'.format(round(nickels)))


if 1 <= remainder < 5:
    if remainder == 1:
        print('1 Penny')
    else:
        print('{} Pennies'.format(remainder))
