# homework 3!!!

def say_goodbye(name):
    return print("goodbye", name)

def circle_area(radius):
    return print(3.14 * (radius)**2)
    
def subtract(a, b):
    return print(a - b)
def multiply(a, b):
    return print(a * b)

def divide(a, b):
    return print(a / b)

def what_to_wear(readings):
    minimum = min(readings)
    maximum = max(readings)
    return(minimum, maximum)


def is_weekday(day):
    if day == 6 or day == 7:
        return "False"
    else:
        return "True"
    
def fuel_efficiency(a,b):
    return print(a / b) + " miles per gallon"

def secret_code(num):
    last_digit = num % 10
    following_digits = num // 10
    encrypted = str(last_digit) + str(following_digits)
    return print(encrypted)

def power(x, y):
    result = 1
    count = 0
    while count < y:
        result *= x
        count += 1
    return print(result)

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

def sum_digits(num):
    total = 0
    while num > 0 # loop continues as long as num still has digits
    total += num % 10 # starts with the last digit then will keep adding
    num //= 10
    return total

num = 9287
result = print(secret_code(num))
print(The result of secret_number with num = 9287 is) + result





