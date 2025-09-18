File: 'homework1.py'

# ---Variables and Data Types--- #

a = 10
print(a)
print(type(a))

b = 1.5
print(b)
print(type(b))

c = 3j
print(c)
print(type(c))

d = "hello"
print(d)
print(type(d))

e = [1, 2, 3]
print(e)
print(type(e))

f = {"name": "Ellen", "favorite fruit": "strawberry"}
print(f)
print(type(f))

g = (1, 2)
print(g)
print(type(g))

h = ["apple", "banana", "strawberry"]
print(h)
print(type(h))

i = True
print(i)
print(type(i))

j = None
print(j)
print(type(j))

k = [True, "blue", 12]
print(k)
print(type(k))

l = str(14)
print(l)
print(type(l))

m = 1e4
print(m)
print(type(m))

# ---Questions:---
# 1. Nine types 
# 2. integer, float, complex, string, list, dict, tuple, bool, NoneType
# 3. b and m; d and l ; e, h, and k
# 4. l is a string because the "str" function assigned it to be one
# 5. Binary types is a data type not given

n = b"hello, world!"
print(n)
print(type(n))

# ---Booleans---
print(10 > 9) # True, 10 is greater than 9
print (10 == 9) # False, 10 is unequal to 9
print (10 <= 9) # False, 10 is not less than nor equal to 9
bool("abc") # True, any string that contains characters within a bool will be classified as true
bool(123) #True, any nonzero integer is classified as true
bool(["apple", "cherry", "bannana"]) # True, any non-empty list is true
bool(True) # True, literal representation of the true boolean
bool(False) # False, represents false boolean
bool(0) # False, nonzero integer
bool("") # False, empty string
bool(" ") # True, nonempty string
bool(()) # False, empty value
bool ([]) # False, empty list
bool({}) # False, empty dict
bool(True and False) # False, self-contradictory
bool(True and True) # True, support each other
bool (False and False) # False, both represent false boolean
bool(True or False) # True, "or" chooses true if at least one value is true
bool(True or True) # True, both "or" options are true
bool(False or False) # False, "or" operator chose between the two options whihc are both false
bool(not(False)) # True, opposite of false
bool(not(True)) #False, opposite of true

# ---Questions---
# 1. The function prefers to choose true.
# 2. I was surprised by "bool(0)" because I didn't understand why only nonzero integers could be true and not all of them including 0
# 3. bool("Yumyumyum") will return true because it is a nonempty string
# 4. bool(4 > 6) will return false because it is mathematically incorrect

# --- Operators ---
10 + 5 # 15, + performs addition
10 - 5 # 5, - performs subtraction
2 *4 # 8, * performs multiplication
6 / 3 # 2.0 , / performs float division
5 % 2 # 1, % gives division remainder
3 ** 2 # 9, ** raises to the power
15 // 2 # 7, // divides and rounds to the lower integer
5 == 2 # False, = verifies equality or inequality
10 != 10 # False, 10! is unequal to 10
2 < 5 # True, inequality verified
12 > 5 # True, 12 is greater than 5
5 <= 6 # True, 5 is less than or equal to 6
1 >= 10 # False, 1 is not greater than or equal to 10

# ---Assignments Operators ---
x = 5
x += 5
x -= 4
x *= 3

# ---Logical Operators---
# The operator 'and' makes it so both of the items in the boolean connected have to satisfy the same requirements
bool(True and True)
bool(True and False)
# The operator 'or' makes it so the boolean chooses one of the items in the expression
bool(True or False)
bool(False or False)
# The operator "not" makes Python negate the effect an item would typically have
bool(not False)
bool(not True)

# ---More Questions---
# 1. A single backslash calculates division with floats while a double backslash evaluates for integers.
# 2. A % outputs the remainder of the division while // rounds down to the integer value
# 3. % E.G. 15 % 2 = 7
# 4. Assignment operators can assign variables to values or different data types

# ---Strings---
my_string = "hello"
print(my_string) # Prints: hello
print(my_string[0]) # Prints the 0th element of the string
print(my_string[1]) # Prints the 1st element of the string
print(my_string[2]) # Prints the 2nd element of the string
print(my_string[3]) # Prints the 3rd element of the string
print(my_string[4]) # Prints the 4th element of the string
print(my_string[-1]) # Prints the last element of the string
print(my_string[1:3]) # Prints the first and third element of the string
print(my_string[0:5:2]) # Prints the 0th, 5th, and 2nd element of the string
print(len(my_string)) # Outputs the length of the string which is 5
print(my_string + "goodbye") # Places the strings next to each other
print(7 * my_string) # Repeats the string 7 times

# --- Questions ---
# 1. Slicing is when you use colons to pick certain parts of your string to output like in prompt 9 of the last exericse.
name = "Oski"
print("Hello, my name is", name) # 2. It prints the new string with the string that was previously assigned
name = "Oski"
print(f"Hello, my name is {name}") # 3. There is an "f" in front and the name string was enclosed by brackets
# 4. This is an f-string which allows the coder to be more concise with Python

# --- Terminal Commands ---
# 1. A terminal command tells the terminal what language to interact with
# 2. You can use "python" or "python3" to initiate the terminal to start thinking in python
python3 <homework1.py>

credits
list
ls -a
mkdir
classmethod
pwd
cd ..
cd .
cd ~
cd ~
ChildProcessError
memoryview
RuntimeError
clear
grep

# ---Questions---
# 1. The command "pop" removes an element from a specified position on the list
# The command "reverse" reverses elements in a list
# "Discard" removes a specified element from the set
# 2. "ls" doesn't list hidden files "ls -a" does
# 3. A hiddel file is intentionally obscured that it can't be seen right away when opening a directory
# 4. -d enables debugging
# -m runs a module as a script
# --version changes prints the Python version of a script

