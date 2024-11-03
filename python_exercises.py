# Install and Setup

# REPL

# VSCode & Extension


# 1. Variables / Types

4 # Integer
5 
200

"Travis" # String
"birthday"

4.5 # Float
300.2

True # Boolean
False

my_age = 41
my_name = "Travis"
my_location = "Virginia"
is_teaching = True

# print (is_teaching)

# print ("Hi my name is " + my_name + " and my location is " + my_location)


# Challenge 1 - Variables

# Python has a bunch of pre-made, built-in tools which you can use to perform tasks. 
# One is these tools is the input() function which allows us to retrieve a user input. 
# You can see these here, including the input() function: https://www.w3schools.com/python/python_ref_functions.asp

# Read about the input() function, try out the example to see how it works, and then only proceed.

# For this challenge, use this input function to ask “What is your favorite color?”. 
# Save the response into a variable named my_input. 
# Then print “Your favorite color is my_input”. 
# So if I type red as my favorite color, it will print “Your favorite color is red”. 

# WORK OUT YOUR SOLUTION HERE


# print("What is your favorite color?")
# my_input = input()
# print("Your favorite color is " + my_input)

# 2. Conditional Logic

#my_number = int(input("Enter a number: "))

# if my_number < 5:
#    print("Your number is less than 5")
#elif my_number > 5:
#    print("Your number is greater than 5")
#else:
#    print("Your number is 5")

#if my_number > 0 and my_number < 10:
 #   print("Single digit")
#else:
#    print("Double digit")
    
#if my_number == 8 or my_number == 4:
#    print("Your number is 8 or 4")


# Challenge 2 - Conditionals - Rock, Paper, Scissors

# We'll use what we've so far to create the Rock, Paper, Scissors game. Here's how:

# First, you'll need to capture inputs for both Player 1 and Player 2. 

# Next, you'll use conditionals to check the two answers and see who wins. This seems pretty
# complicated on the surface but don't overthink it. Here's some help: 
# If Player 1 plays Paper, then there are only two conditionals to check against (Rock, Scissors).
# This means for each element, there should be two checks, totalling 6 checks overall. Each check 
# should print "Player x wins" with the correct player based on the condition. 

# Finally, there should be a check for the same element being played, i.e. if both players play rock
# then an error message should be printed like "Error, you aren't allowed to play the same thing".

# WORK OUT YOUR SOLUTION HERE

#player_1 = input("Player 1: ")
#player_2 = input("Player 2: ")

#if player_1 == player_2:
#    print("Error, you aren't allowed to play the same thing")

#elif player_1 == 'paper' and player_2 == 'rock':
#    print("Player 1 wins with " + player_1)
#elif player_1 == 'paper' and player_2 == 'scissors':
#    print("Player 2 wins with " + player_2)

#elif player_1 == 'rock' and player_2 == 'scissors':
#    print("Player 1 wins with " + player_1)
#elif player_1 == 'rock' and player_2 == 'paper':
#    print("Player 2 wins with " + player_2)

#elif player_1 == 'scissors' and player_2 == 'rock':
#    print("Player 2 wins with " + player_2)
#elif player_1 == 'scissors' and player_2 == 'paper':
#    print("Player 1 wins with " + player_1)

#else: 
#    print("Something went wrong, Please try again.")


# 3. Lists

#birds = ["robin", "bluebird", "sparrow"]
#things =[4, "food", 4.3, False]

#books = ["A Tale of Two Cities", "The Lord of the Rings", "The Little Prince", "Harry Potter and the Sorcerer's Stone", "And Then There Were None", "The Dream of the Red Chamber", "The Hobbit"]

#books_slice = books[-3:]
#print(books_slice)

# Challenge 3 - Lists

# Find the solutions using this list

#birds = ["robin", "bluebird", "sparrow", "cardinal"]


# 1. Save "bluebird" in a variable

# WORK OUT YOUR SOLUTION HERE

#bluebird = birds[1]
#print(bluebird)

# 2. Save "cardinal" in a variable

# WORK OUT YOUR SOLUTION HERE

#cardinal = birds[3]
#print(cardinal)


# 3. Insert "woodpecker" directly behind sparrow in the list

# WORK OUT YOUR SOLUTION HERE

#birds.insert(3, "woodpecker")
#print(birds)


# 4. Reverse the birds list and print it out

# WORK OUT YOUR SOLUTION HERE

#birds.reverse()
#print(birds)

# 5. Save the first two birds only into a new variable called two_birds

# WORK OUT YOUR SOLUTION HERE

#two_birds = birds[0:2]
#print(two_birds)

# 6. Print ["sparrow", "cardinal"] using negative indices

# WORK OUT YOUR SOLUTION HERE

#print(birds[-2:])



# 4. Loops



# Challenge 4 - Loops
#For Loop

#numbers = [0, 1, 2, 3, 4, 5, 6]

#for number in numbers: 
#    number = number * 2
#    print(number)

#While Loop

#counter = 0

#while counter < 10:
#    counter = counter + 1
#    print(counter)

items = ["steak", "apple", "bread", "butter", "pineapple"]

# 1. Write a 'for loop' that loops through the above list and prints "item is a fruit" or "item is not a fruit" depending on whether it is or not. 
#    Note that it should not say item but the name of the fruit. So 'steak is not a fruit', 'apple is a fruit', etc. 

# WORK OUT YOUR SOLUTION HERE

#for item in items:
#    if item == "apple" or item == "pineapple":
#        print(item + " is a fruit")

#    else: 
#        print(item + " is not a fruit")

# 2. Write a while loop starting with a counter = 1 that multiplies two to your counter, prints the counter, but breaks the loop after the counter reaches 1000. 

# WORK OUT YOUR SOLUTION HERE

#def counter_loop(start, end):
#    counter = start
#    while counter < end:
#        counter *= 2
#        print(counter)

#counter_loop(50, 2500)

#while True:
#    counter *= 2
 #   print(counter)
 #   if counter > 1000:
  #      break




# 5. Functions



# Challenge 5 - Functions

#def make_some_eggs(quantity, egg_type):
#    print("New order for " + quantity + " " + egg_type + " eggs" )

# make_some_eggs("6", "over-easy")

# Write a function that takes a list of numbers and prints a new list with only the numbers less than 10 in it.

# WORK OUT YOUR SOLUTION HERE

#def under_ten_list(list_of_numbers):
#    new_numbers = []
#    for number in list_of_numbers:
#        if number < 10:
#            new_numbers.append(number)
#    print(new_numbers)

#under_ten_list([1, 81, 45, 3, 9, 35, 87, 44, 6, 2, 8])



# 6. Dictionaries

# Challenge 6 - Dictionaries

#teacher = ["Travis", 41, "Virginia", True, 1981, False, 12]

#teacher = {
#    "name": "Travis",
#    "age": 41,
#    "language": "Python",
#    "isTeaching": True
#}

#print(teacher.items())


# print("Bob" in teacher.values())

college = {
      "name": "Yale",
      "founded": "1701",
      "motto": "Light and truth",
      "location": "New Haven, Connecticut",
      "students": 12060
 }

# 1. Loop through dictionary and print all the values (values only)

# WORK OUT YOUR SOLUTION HERE

#for c in college.values():
#    print(c)

# 2. Loop through dictionary and print all the keys and values

# WORK OUT YOUR SOLUTION HERE

#for c in college.items():
#    print(c)


# 3. Print the "founded" year of the college

# WORK OUT YOUR SOLUTION HERE

#print(college["founded"])


# FINAL PROJECT - Password Checker

# 1. Get password input
# 2. Check if password has lowercase, uppercase, a number, and a special character. 
# 3. If the password doesn't meet all four conditions, then reject with the conditions they still need to meet.
# 4. Only accept if all four conditions are met.
# 5. Add a condition to check that password length is greater than 9 digits. If 9 or less, it fails.

# Hints/Suggestions:
# - Break password into list of letters and loop through to check type (upper, lower, etc.). Check out
#   the Python string package for help with upper, lower, and digits. https://docs.python.org/3/library/string.html. Import this package by
#   putting 'import string' at the top of your file. This will import the library and give you access to its methods.
# - Consider creating a function or two to clean up any repetitiveness. 
# - Remember that there are many ways to complete this task. Many programmers will provide many different solutions. Some will
#   be more "efficient" or more "clean" than others. Who cares at this point. Find what solutions works for you AND successfully
#   checks passwords and call it a win!

import string

my_password = input("Enter your password: ")
my_password_list = list(my_password)

qualifications = ["lowercase", "uppercase", "digits", "special characters"]

lower = 0
upper = 0
digit = 0
special = 0

for char in my_password_list:
    if char in string.ascii_lowercase:
        lower += 1
        if "lowercase" in qualifications:
            qualifications.remove("lowercase")
    elif char in string.ascii_uppercase:
        upper += 1
        if "uppercase" in qualifications:
            qualifications.remove("uppercase")
    elif char in string.digits:
        digit += 1
        if "digits" in qualifications:
            qualifications.remove("digits")
    else: 
        special += 1
        if "special characters" in qualifications:
            qualifications.remove("special characters")        

print("Your Results")
print("+============+")
print("Lower: " + str(lower))
print("Upper: " + str(upper))
print("Digits: " + str(digit))
print("Special Characters: " + str(special))

if len(qualifications) == 0 and len(my_password_list) > 9:
    print("Your password is strong. Good job")

if len(my_password_list) <= 9:
    print("Error: Your password is too short. it must be greater than 9 characters.")

if len(qualifications) != 0:
    print("Your password is not strong enough. The following requirements are not met: " + ", ".join(qualifications))