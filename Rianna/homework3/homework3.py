# homework 3!!!

# 3.1 say goodbye
def say_goodbye(name):
    return print("goodbye", name)

#3.2 area of a circle
def circle_area(radius):
    return print(3.14 * (radius)**2)
    
# 4 return functions
def subtract(a, b):
    return print(a - b)
def multiply(a, b):
    return print(a * b)

def divide(a, b):
    return print(a / b)

# 5 conditionals
def what_to_wear(readings):
    minimum = min(readings)
    maximum = max(readings)
    return(minimum, maximum)

#5.2 check if it's the weekend
def is_weekday(day):
    if day == 6 or day == 7:
        return "False"
    else:
        return "True"
    
#5.3 fuel efficiency calculator
def fuel_efficiency(a, b):
    return print(a / b) + " miles per gallon"

# 5.4 secret code
def secret_code(num):
    last_digit = num % 10
    following_digits = num // 10
    encrypted = str(last_digit) + str(following_digits)
    return print(encrypted)

# 6 loops
#6.1 oski stole power
def power(x, y):
    result = 1
    count = 0
    while count < y:
        result *= x
        count += 1
    return print(result)

#6.2 min & max w/ loops
#6.2.1 for loops
def min(numbers): # numbers is an array:
    numbers_sorted = sorted(numbers)
    minimum = numbers_sorted[0]
    for number in numbers:
        if number < minimum:
         minimum = number
    return minimum

def max(numbers): # numbers is an array
    numbers_sorted = sorted(numbers)
    maximum = numbers_sorted[-1]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

#6.2.2 while loops
def while_min(numbers):
    i = 0 
    minimum = numbers[0]
    while i < len(numbers):
        if numbers[i] < minimum:
            minimum = numbers[i]
        i += 1
    return minimum

def while_max(numbers):
    i = 0
    maximum = numbers[0]
    while i < len(numbers):
        if numbers[i] > maximum:
            maximum = numbers[i]
        i += 1
    return maximum

#6.3 calculate sum
def sum_digits(num):
    total = 0
    while num > 0: # while num still has digits:
        total += num % 10 # starts with the last digit then will keep adding
    num //= 10
    return total

num = 9287
result = print(secret_code(num))
print(result)




