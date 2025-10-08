# File: lists_and_dictionaries

numbers = [1, 2, 3, 4, 5, 5]
fruits = ["apple", "banana", "cherry"]
mixed = ["hello", 5, True, None]

# indexing: [start:stop:step]

#fruits.append("date")
#fruits.insert(2, "blueberry")
#fruits.remove("blueberry")
#fruits.pop(3)

#print(fruits)

#Slicing Lists
print(numbers[2:5])
print(numbers[:4])
print(numbers[4:])

print(numbers[::2]) # double colon gives every other number
print(numbers[2::])
print(numbers[:2:])
print(numbers[2:2:2]) # stop is non-inclusive

#Dictionaries

star = {"name": "Vega", "magnitude": 0.57, "distance": 25.05}
print(star)
star["class"] = "A0V"
print(star)
star.clear()
print(star)

star.keys()
star.values()
star.items()

#engagement 7 

list = [10, 15, 20, 25, 30, 40, 50, 55]
# print(list[2])
# print(list*-1)
# print(list[1:4])
# list.insert(5, 35)
# print(list)
list.insert(5, 35)
print(list)
print(list[5::2])