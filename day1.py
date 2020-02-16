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