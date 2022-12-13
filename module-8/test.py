#### 8.2.1: Declaring a class
# class PatientData:
#     def __init__(self):
#         self.height_inches = 0
#         self.weight_pounds = 0


# patient = PatientData()
# print('Patient data (before):', end=' ')
# print(patient.height_inches, 'in,', end=' ')
# print(patient.weight_pounds, 'lbs')


# patient.height_inches = int(input())
# patient.weight_pounds = int(input())

# print('Patient data (after):', end=' ')
# print(patient.height_inches, 'in,', end=' ')
# print(patient.weight_pounds, 'lbs')

#### 8.2.2: Access a class' attributes.
# class InventoryTag:
#     def __init__(self):
#         self.item_id = 0
#         self.quantity_remaining = 0

# red_sweater = InventoryTag()
# red_sweater.item_id = int(input())
# red_sweater.quantity_remaining = int(input())

# print('ID:', red_sweater.item_id)
# print('Qty:', red_sweater.quantity_remaining)

# ### 8.3.1: Adding a method to a class
# class Employee:
#     def __init__(self):
#         self.wage = 0
#         self.hours_worked = 0

#     def calculate_pay(self):
#         return self.wage * self.hours_worked

# #        ...

# alice = Employee()
# alice.wage = 9.25
# alice.hours_worked = 35
# print('Alice:\n Net pay: {:.2f}'.format(alice.calculate_pay()))

# barbara = Employee()
# barbara.wage = 11.50
# barbara.hours_worked = 20
# print('Barbara:\n Net pay: {:.2f}'.format(barbara.calculate_pay()))

#### 8.3.1: Creating a method object.
# class PersonInfo:
#     def __init__(self):
#         self.num_kids = 0

#     def inc_num_kids(self):
#         self.num_kids += 1

# person1 = PersonInfo()

# print('Kids:', person1.num_kids)
# person1.inc_num_kids()
# print('New baby, kids now:', person1.num_kids)

#### 8.5.1: using classes to implement an airline seat reservation system.
# class Seat:
#     def __init__(self):
#         self.first_name = ''
#         self.last_name = ''
#         self.paid = 0.0

#     def reserve(self, fn, ln, pd):
#         self.first_name = fn
#         self.last_name = ln
#         self.paid = pd

#     def make_empty(self):
#         self.first_name = ''
#         self.last_name = ''
#         self.paid = 0.0

#     def is_empty(self):
#         return self.first_name == ''

#     def print_seat(self):
#         print('{} {}, Paid: {:.2f}'.format(self.first_name, self.last_name, self.paid))


# def make_seats_empty(seats):
#     for s in seats:
#         s.make_empty()


# def print_seats(seats):
#     for s in range(len(seats)):
#         print('{}:'.format(s), end=' ')
#         seats[s].print_seat()

# num_seats = 5

# available_seats = []
# for i in range(num_seats):
#     available_seats.append(Seat())

# command = input('Enter command (p/r/q): ')
# while command != 'q':
#     if command == 'p':  # Print seats
#         print_seats(available_seats)
#     elif command == 'r':  # Reserve a seat
#         seat_num = int(input('Enter seat num:\n'))
#         if not available_seats[seat_num].is_empty():
#             print('Seat not empty')
#         else:
#             fname = input('Enter first name:\n')
#             lname = input('Enter last name:\n')
#             paid = float(input('Enter amount paid:\n'))
#             available_seats[seat_num].reserve(fname, lname, paid)
#     else:
#         print('Invalid command.')

#     command = input('Enter command (p/r/q):\n')

#### 8.6.1: Defining a class constructor.
# class PhonePlan:
#     # FIXME add constructor

#     def __init__(self, num_mins=0, num_messages=0):
#         self.num_mins = num_mins
#         self.num_messages = num_messages

#     def print_plan(self):
#         print('Mins:', self.num_mins, end=' ')
#         print('Messages:', self.num_messages)


# my_plan = PhonePlan(int(input()), int(input()))
# dads_plan = PhonePlan()
# moms_plan = PhonePlan(int(input()))

# print('My plan...', end=' ')
# my_plan.print_plan()

# print('Dad\'s plan...', end=' ')
# dads_plan.print_plan()

# print('Mom\'s plan...', end= ' ')
# moms_plan.print_plan()

#### 8.8.1 Customization of printing a class instance.
# class Car:
#     def __init__(self, make, model, year, miles, price):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.miles = miles
#         self.price = price

#     def __str__(self):
#         return f'{self.year} {self.make} {self.model}:\n  Mileage: {self.miles}\n  Price: ${self.price:}'

# cars = []
# cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
# cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
# cars.append(Car('Nissan', 'Maxima', 2012, 25000, 15750))

# for car in cars:
#     print(car)

##### 8.8.2: Rich comparisons for a quarterback class.

# class Quarterback:
#     def __init__(self, yrds, tds, cmps, atts, ints, wins):
#         self.wins = wins

#         # Calculate quarterback passer rating (NCAA)
#         self.rating = ((8.4*yrds) + (330*tds) + (100*cmps) - (200 * ints))/atts

#     def __le__(self, other):
#         if (self.rating <= other.rating) or (self.wins <= other.wins):
#             return True
#         return False

#     def __gt__(self, other):
#         return True
#         # Complete the method...

# peyton = Quarterback(yrds=4700, atts=679, cmps=450, tds=33, ints=17, wins=10)
# eli = Quarterback(yrds=4002, atts=539, cmps=339, tds=31, ints=25, wins=9)

# if peyton > eli:
#     print('Peyton is the better QB')
# elif peyton < eli:
#     print('Eli is the better QB')
# else:
#     print('It is not clear who the better QB is...')

#### 8.8.1: Defining __str__
# class CarRecord:
#     def __init__(self):
#         self.year_made = 0
#         self.car_vin = ''

#     # FIXME add __str__()

#     def __str__(self):
#         return f'Year: {self.year_made}, VIN: {self.car_vin}'

# my_car = CarRecord()
# my_car.year_made = int(input())
# my_car.car_vin = input()

# print(my_car)

##### 8.13.1: Extending the hash example

# FIXME: Import sha224 also
import hashlib
from hashlib import md5, sha1, sha224

text = input("Enter text to hash ('q' to quit): ")

# Add sha224 to prompt
algorithm = input('\nEnter algorithm (md5/sha1): ')
if algorithm == 'md5':
    output = md5(text.encode('utf-8'))
elif algorithm == 'sha1':
    output = sha1(text.encode('utf-8'))
    # FIXME: Add check for sha224
elif algorithm == 'sha224':
    output = sha224(text.encode('utf-8'))

else:
    output = 'Invalid algorithm selection'

print('\nHash value:', output.hexdigest())

