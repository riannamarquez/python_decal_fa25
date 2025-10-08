import platform
# print("Hello, Ria!")
# name = 'Ria'
# print('Hello,', name)
# def add(a, b):
#     print(a + b)

# add(42, 69)
# def add(a, b):
#     return a + b

# c = add(42, 69)
# print(c)

#def check_number(num):
 #   if num > 0:
  #      return "Positive"
   # elif num < 0:
    #    return "Negative"
    #else
     #   return "Zero"

# print(check_number(0))

def can_vote(age, is_citizen):
    if age >= 18 and is_citizen:
        print("You can vote!")
    else:
        print("You cannot vote")

# can_vote(18, False)

#def is_weekend(day):
   # if day == "Saturday" or day == "Sunday":
  #      return "It's the weekend!"
  #  else:
  #      return "It's not the weekend"
    
# print(is_weekend("Sunday"))

# for i in range(5):
  #  print(i)

  
# fruits = ["apple", "banana", "cherry"]
# def print_fruits(fruits):
#    for fruit in fruits
# print_fruits(fruits)

def countdown(start):
    while start > 0:
        print(start)
        start = start - 1
    print("Lift off!")

countdown(5)
