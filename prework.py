# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of code has been defined as below.

def hello_name(user_name):
    """Prints a message for the user"""
    print("hello_" + user_name.upper() + "!")

hello_name("username")

# Question 2
# Write a function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
    """Prints the odd numbers from 1-100 and returns nothing"""
    for num in range(1,100,2):
        if num % 2 == 0:
            continue
        else:
            print(num)

first_odds()

# Question 3
# Write a Python function, max_num_in_list to return the max number of a given list.

def max_num_in_list(a_list):
    """Returns the max number of a given list"""
    print(max(a_list))

a_list = [49, 50, 33, 8] 
max_num_in_list(a_list)

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisable by 400. The return should be boolean Type (true/false)

def is_leap_year(a_year):
    """Tells you whether a given year is a leap year"""
    if ((a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0)):
        print(True)
    else:
        print(False)

is_leap_year(2016)

# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. The return should be boolean Type

def is_consectutive(list):
    """Checks to see if all numbers in a list are consecutive""" 
    i = 0
    status = True
    while i < len(list) - 1:
        if list[i] + 1 == list[i + 1]:
            i += 1
        else:
            status = False
            break
    print(status)

list = [5,6,7,9]
is_consectutive(a_list)