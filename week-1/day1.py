# CS Challenges - Day 1

################
## Exercise 1 ##
################

# 1. How many seconds are there in 21 minutes and 15 seconds?
    
seconds_in_minutes = lambda m, s=None: m * 60 if s == None else m * 60 + s

print(f"There are {seconds_in_minutes(1)} seconds in 1 minute.")
print(f"There are {seconds_in_minutes(21, 15)} seconds in 21 minute and 15 seconds.")

# 2. How many miles are there in 5 kilometers?

miles_in_km = lambda km: km / 1.609344

print(f"There are %0.5f miles in 5 kilometers." % miles_in_km(5))

# 3. If you run a 5 kilometer race in 21 minutes and 15 seconds, 
# what is your average pace (time per mile in minutes and seconds)?

time_per_mile = seconds_in_minutes(21, 15) / miles_in_km(5) # 410.38272
minutes_per_mile = time_per_mile // 60
seconds_per_mile = time_per_mile % 60

print(f"Average pace per mile: {minutes_per_mile:.0f} minutes {seconds_per_mile:.0f} seconds.")

# 4. What is your average speed in miles per hour?

mile_per_hour = 60 / (time_per_mile / 60)

print(f"Average speed in miles per hour: {mile_per_hour:.05f}")

# 5. Suppose the cover price of a book is $19.95, but bookstores get a 25% discount. 
# Shipping costs $2.50 for the first copy and $1 for each additional copy. 
# What is the total wholesale cost for 75 copies?

book_price = 19.95
discounted_price = book_price - (book_price * 25 / 100)
wholesale_cost = (discounted_price + 2.50) + (74 * (discounted_price + 1))

print(f"Total wholesale cost for 75 copies: ${wholesale_cost:.2f}")

################
## Exercise 2 ##
################

# 2. Change do_twice so it takes two arguments, a function object and a value, 
# and calls the function twice, passing the value as an argument.

def do_twice(function, string):
    function(string)
    function(string)
    
def print_spam(string):
    print(string)
    
do_twice(print_spam, "do_twice prints twice")

# 3. Define a function called print_twice that takes one argument and prints 
# the value of that argument twice.

def print_twice(arg):
    print(arg)
    print(arg)
    
print_twice("print_twice prints twice")

# 4. Use the changed version of do_twice to call print_twice twice, 
# passing 'spam' as an argument.

do_twice(print_twice, "spam")

# 5. Define a new function called do_four that takes a function object and a value 
# and calls the function four times, passing the value as a parameter. 
# There should be only two statements in the body of this function, not four.

def do_four(function, value):
    for _ in range(4):
        function(value)

do_four(print_spam, "do_four prints spam 4 times")

################
## Exercise 3 ##
################

# Fermat’s Last Theorem says that there are no positive integers 
# a, b, and c such that a**n + b**n == c**n

# 1. Write a function named check_fermat that takes four parameters—a, b, c and 
# n —and checks to see if Fermat’s theorem holds. If n is greater than 2 and 
# a**n + b**n = c**n the program should print, "Holy smokes, Fermat was wrong!" 
# Otherwise the program should print, "No, that doesn't work."

def check_fermat(a, b, c, n):
    print("Holy smokes, Fermat was wrong!") if n > 2 and a**n + b**n == c**n else print("No, that doesn't work.")
    
# 2. Write a function that prompts the user to input values for a, b, c and n, 
# converts them to integers, and uses check_fermat to check whether they violate 
# Fermat’s theorem.

def fermat_inputs():
    inputs = []
    variables = ('a', 'b', 'c', 'n')
    
    while len(inputs) < 4:
        for i in variables:
            var = input(f"Enter integer value for '{i}': ")
            while not var.lstrip('-').isdigit():
                var = input(f"Try again to enter integer value for '{i}': ")
            inputs.append(int(var))
                
    if len(inputs) == 4:
        a, b, c, n = inputs
        check_fermat(a, b, c, n)    

# fermat_inputs()

#########################
## Objective challenge ##
#########################

# List is a data structure that stores an ordered collection of any number of items that can hold different 
# data types. List allows to have duplicates, it's elements can be selected using indices and list is a mutable
# data type - it can be altered by adding or removing items.

# Tuple is similar data structure to a list in a sense that it holds a sequence of values. The main difference
# is that tuples don't offer same functionality as lists do - values of tuples are immutable. Having this in mind,
# tuples are perfect to hold certain data that is not goint to be altered by the program. Also, they are faster
# than lists.

# Dictionary stores data in a key-value pairs, therefore key has to have unique value. Key-value pairs in dictionary
# do not follow any specific order, so one has to use it's key to access a certain value in dictionary. Dictionaries
# are mutable.

# Set is an unordered collection of simple objects in Python. In addition to being iterable and mutable, 
# a set has no duplicate elements. 

###########
## Lists ##
###########

# 1. Create a list
hey_im_a_list = ['a', 'b', 'c', 'd']

# 2. Access list items
hey_im_a_list[0]

# 3. Change the value of a list item
hey_im_a_list[0] = 'x'

# 4. Loop through a list
for i in hey_im_a_list:
    pass

# 5. Check if a list item exists
'x' in hey_im_a_list

# 6. Get the length of a list
len(hey_im_a_list)

# 7. Add an item to the end of a list
hey_im_a_list.append('z')

# 8. Add an item at a specified index
hey_im_a_list.insert(3, 'B')

# 9. Remove an item
hey_im_a_list.remove('c')

# 10. Remove an item at a specified index
hey_im_a_list.pop(0)

# 11. Empty a list
hey_im_a_list.clear()

# 12. Use the list() constructor to make a list
hey_im_a_new_list = list('qwerty')

##################
## Dictionaries ##
##################

# 1. Create a dictionary
club = {'name': 'Arsenal', 'manager': 'Mikel Arteta'}

# 2. Access the items of a dictionary
club['name']

# 3. Change the value of a specific item in a dictionary
club['name'] = 'Woolwich Arsenal'

# 4. Print all key names in a dictionary, one by one
for keys in club.keys():
    print(keys)
    
# 5. Print all values in a dictionary, one by one
for values in club.values():
    print(values)
    
# 6. Use the values() function to return values of a dictionary
club.values()

# 7. Loop through both keys and values, by using the items() function
for k, v in club.items():
    pass

# 8. Check if a key exists
'name' in club.keys()

# 9. Get the length of a dictionary
len(club)

# 10. Add an item to a dictionary
club.update({'colors': ['red', 'white']})

# 11. Remove an item from a dictionary
club.pop('name')

# 12. Empty a dictionary
club.clear()

# 13. Use the dict() constructor to create a dictionary
new_club = dict()

############
## Tuples ##
############

# 1. Create a tuple
days = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'

# 2. Access tuple items
days[0]

# 3. Change tuple values
print('No, thank you. Tuple values are immutable.')

# 4. Loop through a tuple
for i in days:
    pass

# 5. Check if a tuple item exists
'Monday' in days

# 6. Get the length of a tuple
len(days)

# 7. Delete a tuple
del days

# 8. Use the tuple() constructor to create a tuple
days = tuple()

##########
## Sets ##
##########

# 1. Create a set
months = {'January', 'February', 'March', 'April'}

# 2. Loop through a set
for i in months:
    pass

# 3. Check if an item exists
'January' in months

# 4. Add an item to a set
months.add('May')

# 5. Add multiple items to a set
months.update({'June', 'July'})

# 6. Get the length of a set
len(months)

# 7. Remove an item in a set
months.remove('May')

# 8. Remove an item in a set by using the discard() method
months.discard('June')

# 9. Remove the last item in a set by using the pop() method
print('No, thanks again. Sets are unordered, therefore pop() is going to remove the random item from it.')

# 10. Empty a set
months.clear()

# 11. Delete a set
del months

# 12. Use the set() constructor to create a set
months = set()
