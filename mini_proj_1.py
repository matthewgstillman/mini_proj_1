#Mini Project #1 (BONUS. Up to 3 points)
#Due: 10/11
#1. Your program needs to do the following:
# Inputs: a series of numbers
# The program then selects 2 numbers from the series and generate new numbers using the 4
#mathematical operations
# Outputs: All the new numbers it can generate using the 4 basic mathematical operations (+, -, x
#and /)
# Don’t forget about warning messages. What are the error conditions?
#o The numbers input from the users are not int or float
#o Users enter less than 2 numbers
#o etc
#o etc
#For example:
#Series of numbers = 1,2,3
# to select=2
#Let’s say the 2 numbers selected are 1 and 3
#The program returns the following:
#4 (Addition: 1+3)
#2 and -2 (Subtraction: 3-1, 1-3)
#3 (Multiplication: 1x3)
#3, 0.3333 (Division: 3/1 and 1/3)
import random
print("Mini Project: Random Numbers")
numbers_input = 0
number_series = ""
number_list = []
random_numbers_list = []
first_input = int(input("Please input your first number"))
if type(first_input) == 'float' or type(first_input) == 'int':
  print("Please input a properly formatted number")
else:
  number_series += str(first_input) + ","
  numbers_input += 1
second_input = int(input("Please input your second number"))
if type(second_input) == 'float' or type(second_input) == 'int':
  print("Please input a properly formatted number")
else:
  number_series += str(second_input) + ","
  numbers_input += 1
third_input = int(input("Please input your third number"))
if type(third_input) == 'float' or type(third_input) == 'int':
  print("Please input a properly formatted number")
else:
  number_series += str(third_input)
  numbers_input += 1
print("Number Series: {}".format(number_series))

print("Numbers Input: {}".format(numbers_input))

if numbers_input != 3:
  print("Error! I don't know how you circumvented my program and got here without inputting three numbers, but you have to input three numbers! Please try again!")
else:
  pass

for i in range(0, len(number_series)):
  if number_series[i] != ",":
    number_list.append(int(number_series[i]))
print("Number List: {}".format(number_list))

for number in range(0, len(number_list)):
  if number == 0:
    random_number_one = random.choice(number_list)
    print("Random Number One: {}".format(random_number_one))
    random_numbers_list.append(random_number_one)
  if number == 1:
    random_number_two = random.choice(number_list)
    print("Random Number Two: {}".format(random_number_two))
    if random_number_two == random_number_one:
      print("The Two numbers can't be equal")
      random_number_two = random_number_two = random.choice(number_list)
    else:
      print("Random Number Two: {}".format(random_number_two))
      random_numbers_list.append(random_number_two)
print("Random Numbers List: {}".format(random_numbers_list))

first = random_numbers_list[0]
second = random_numbers_list[1]
print("First: {}, Second: {}".format(first, second))

addition = int(first) + int(second)
print("Addition: {} + {} = {}".format(first, second,addition))

subtraction_1 = int(first) - int(second)
subtraction_2 = int(second) - int(first)
print("Subtraction 1: {} - {} = {}".format(first, second, subtraction_1))
print("Subtraction 2: {} - {} = {}".format(second, first, subtraction_2))

multiplication = int(first) * int(second)
print("Multiplication: {} * {} = {}".format(first, second, multiplication))

division_1 = int(first) / int(second)
division_2 = int(second) / int(first)
print("Division 1: {}/{} = {}".format(first, second, division_1))
print("Division 2: {}/{} = {}".format(second, first, division_2))

