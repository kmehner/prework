#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print("Hello " + user_name + "!")
  
hello_name('kmehner')

#Question 2: Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():
# Unsure what is meant by return nothing
def first_odds():
    num = 1
    while num <= 100:
        print(num)
        num += 2 

first_odds()


#Question 3: Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):
    print(max(a_list))

list = [1, 2,10, 78, 98, 3, 84]
max_num_in_list(list)


#Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 100 or a_year % 400 != 0):
        leap_year = True 
    else:
        leap_year = False 
    print(leap_year)

is_leap_year(2022)
is_leap_year(2020)

print(" --- next --- ")

#Question 5: Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):
# help from geeksforgeeks.org - only way I could get it to work but I understand it 

unconfirmed_consecutive = [1,2,3,4,5,6,7]
not_consecutive = [1,5,4,3,4]

import numpy as np
# diff() calculates the n-th discrete difference along the given axis 
# find the difference of the sorted list and check if equal to 1 

def is_consecutive(a_list):
    n = len(a_list) - 1
    return(sum(np.diff(sorted(a_list)) == 1 ) >= n)

print(is_consecutive(unconfirmed_consecutive))
print(is_consecutive(not_consecutive))
    

# was also trying to set value = value before + 1 
# for value in a_list: 
    # if num = num + 1:
        # consecutive = True 

# found a way to do it with range as well but could not convert the range to a string like other examples I saw 
    # rangelist = string(range(max(a_list), max(a_list) + 1))
    # if a_list.sorted() == rangelist:
    #   consecutive = True  


#Stack overflow help* More similar to example from quiz 8 

def check_is_consecutive(list_B):
    counter = [0] * len(list_B)
    limit = len(list_B)
    for element in list_B:
        if not 1 <= element <= limit:
            return False
        else: 
            if counter[element - 1] != 0:
                return False
            else: counter[element - 1] = 1
    return True

print(check_is_consecutive(unconfirmed_consecutive))
print(check_is_consecutive(not_consecutive))


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

