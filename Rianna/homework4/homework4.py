# homework 4!

# 3.1 list operations

my_favorite_foods = ["soup", "bread", "rice", "noodle", "bacon"]
print(my_favorite_foods[1])
print(my_favorite_foods[-1])

my_favorite_foods.append("ice cream")
my_favorite_foods.insert(0, "apple")
my_favorite_foods.remove("rice")

print(my_favorite_foods)
print(len(my_favorite_foods))

def print_food(my_favorite_foods):
    for food in my_favorite_foods:
     print(food.upper())
print_food(my_favorite_foods)

first_and_last = my_favorite_foods[:1] + my_favorite_foods[-1:]
print(first_and_last)

def potato(food):
    if food == "potato":
        return "A potato!"
    else:
        return "No potato!"

print(potato("apple"))

# 3.2 slicing & striding

numbers_first = list(range(0, 21))

def get_first_15(numbers_first):
    return numbers_first[0:15]

def get_every_5th(lst):
    first_15 = get_first_15(lst)   # ✅ call it properly
    return first_15[::5]

def reverse_and_stride(lst):
    every_5th = get_every_5th(lst)
    return every_5th[::-3]

# 3.3 nested lists

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

numbers = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9]
]

print(numbers[2])
print(numbers[2][1])
numbers.append([10, 11, 12])
print(numbers)

print(" I encountered this error:" 
"print(numbers.append[10, 11, 12]) because the syntax didn't match the method-chaining with the print statement")

def sum_nested(numbers):
   total = 0
   for row in numbers:
      for num in row:
         total += num
   return total

print(sum_nested(numbers))

print("I encountered this error:" \
"print(sum_nested(numbers)) didn't run because I had originally defined sum_nested as a function with no input")

print("I encountered this error:" \
"return total would not run because my indentation was incorrect")

# 3.4 create a 5x5 list

def five_by_five():
    numbers = []
    count = 1

    for i in range (5):
        row = []
        for j in range(5):
            row.append(count)
            count += 1
        numbers.append(row)
    return numbers

print("I encountered this error:" \
"I didn't indent the j function inside of the i function so the 5x5 list kept on returning one row because the loop was incomplete")

five_by_five()
for row in five_by_five():
    print(row)

def no_threes():
   threes = []
   for row in five_by_five():
      new_row = []
      for num in row:
         if num % 3 == 0:
            new_row.append("?")
         else:
            new_row.append(num)
      threes.append(new_row)
   return threes

for new_row in no_threes():
    print(new_row)

def non_threes():
   sum = 0
   for new_row in no_threes():
      for num in new_row:
         if num != "?":
            sum += num
   return sum
result = print(non_threes())


# 4 dictionaries

ages = {
   "Katie": 30,
   "Mariam": 42,
   "Safia": 25,
   "Mira": 48
}

print(ages["Katie"])
ages["Mira"] = 100
ages.update({"Milana": 52})
ages.pop("Mariam")

for name, age in ages.items():
   print(name, age)

print("I encountered this error:" \
"when trying to print the key and values in my dictionary, it said there were too many values to unpack")

# 5.1 vs code -- all parts ran
# 5.2 in your vs code terminal
# favorite function:
for row in five_by_five():
    print(row)