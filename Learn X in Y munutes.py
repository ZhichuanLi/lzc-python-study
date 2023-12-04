#****************** 2023-11-27 *************************

# Single line comments start with a number symbol.

""" Multiline strings can be written
    using three "s, and are often used 
    as documentation.
"""

################################################
## 1. Primitive Datatypes and Operators
################################################

# You have numbers
3 # => 3

# Math is what you would expect
1 + 1  # => 2
8 - 1  # => 7
10 * 2 # => 20
35 / 5 # =>7.0

# Integer division rounds down for both positive and negative numbers
5 // 3      # => 1
-5 // 3     # => -2
5.0 // 3.0  # => 1.0 # works on floats too
-5.0 // 3.0 # => -2.0

# The result of division is always a float
10.0 // 3   # => 3.0

# Modulo operation
7 % 3   # => 1
# i % j have the same sign as j, unlike C
-7 % 3  # => 2

# Exponentiation (x**y, x to the yth power)
2**3   # => 8

# Enforce precedence with parentheses
1 + 3 * 2   # => 7
(1 + 3) * 2 # => 8

# Boolean values are primitives (Note: the capitalization)
True    # => True
False   # => False

# negate with not
not True    # => False
not False   # => True

# Boolean Operators
# Note "and" and "or" are case-sensitive
True and False  # => False
False and True  # => True

# True and False are actually 1 and 0 but with different keywords
True + True # => 2
True * 8    # => 8
False - 5   # => -5

# Comparison operators look at the numerical value of True and False
0 == False  # => True
2 > True    # => True
2 == True   # => False
-5 != False # => True

# None, 0, and empty strings/lists/dicts/tuples/sets all evaluate to False
# All other values are True
bool(0)     # => False
bool("")    # => False
bool([])    # => False
bool({})    # => False
bool(())    # => False
bool(set()) # => False
bool(4)     # => True
bool(-6)    # => True

# Using boolean logical operators on ints casts them to booleans for evaluation,
# but their non-cast value is returned. Don't mix up with bool(ints) and bitwise
# and/or (&, |)
bool(0)     # => False
bool(2)     # => True
0 and 2     # => 0
bool(-5)    # => True
bool(2)     # => True
-5 or 0     # => -5

# Equality is ==
1 == 1  # => True
2 == 1  # => False

# Inequality is !=
1 != 1  # => False
2 != 1  # => True

# More comparisons
1 < 10  # => True
1 > 10  # => False
2 <= 2  # => True
2 >=2   # => True

# Seeing whether a value is in a range
1 < 2 and 2 < 3 # => True
2 < 3 and 3 < 2 # => False
# Chaining makes this look nicer
1 < 2 < 3   # => True
2 < 3 < 2   # => False

# (is vs. ==) is checks if two variables refers to the same objet,
# but == checks if the objects pointed to have the same values.
a = [1, 2, 3, 4]    # Point a at a new list, [1, 2, 3, 4]
b = a               # Point b at what a is pointing to
b is a              # => True, a and b refer to the same object
b == a              # => True, a's and b's objects are equal
b = [1, 2, 3, 4]    # Point b at a new list, [1, 2, 3, 4]
b is a              # => False, a and b do not refer to the same object
b == a              # => True, a's and b's objects are equal


#****************** 2023-11-28 *************************
# Strings are created with " or '
"This is a string."
"This is also a string."

# Strings can be added too
"Hello" + "world!"  # => "Hello world!"
# Strings literals (but not variables) can be concatenated without using '+'
"Hello" "world"     # => "Hello world!"

# A string can be treated like a list of characters
"Hello world!"[0]   # => 'H'

# You can find the length of a string
len("This is a string") # => 16

# Since Python 3.6, you can use f-strings or formatted string literals
name = "Reiko"
f"She said her name is {name}."  # => "She said her name is Reiko"

# Any valid Python expression inside these braces is returned to the string.
f"{name} is {len(name)} charcters long." # => "Reiko is 5 characters long."

# None is an object
None    # => None

# Don't use the equality "==" symbol to compare objects to none
# Use "is" instead. This checks for equality of object identify.
"etc" is None   # => False
None is None    # => True

############################################################
## 2. Variables and Collections
############################################################

# Python has a print function
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# By default the print function also prints out a newline at the end.
# use the optional argument end to change the end string.
print("Hello, world", end="!")  # => Hello, world!

# Simple way to get input data from console
input_string_var = input("Enter some data: ")   # => Returns the data as a string

# There are no declarations, only assignments.
# Convention is to use lower_case_with_underscores
some_var = 5
some_var    # => 5

# Accessing a previously unassigned variable is an exception.
# See Control Flow to learn more about exception handling.
some_unknown_var    # => Raises a NameError

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yay!" if 0 > 1 else "nay!"     # => "nay!"

# Lists store sequences
li = []
# You can start with a prefilled list
other_li = [4, 5, 6]

# Add stuff to the end of a list with append
li.append(1)    # => Li is now [1]
li.append(2)    # => Li is now [1, 2]
li.append(4)    # => li is now [1, 2, 4]
li.append(3)    # => li is now [1, 2, 4, 3]
# Remove from the end with pop
li.pop()        # => 3 and li is now [1, 2, 4]
# Let's put it back
li.append(3)    # => li is now [1, 2, 4, 3] again.

# Access a list like you would any array
li[0]   # => 1
# Look at the last element
li[-1]  # => 3

# Looking out of bounds is an IndexError
li[4]   # => Raises an IndexError

# You can look at ranges with slice syntax.
# The start index is included, then end index is not
# (It's a closed/open range fro you mathy types.)
li[1:3]     # => Return list from index 1 to 3 => [2, 4]
li[2:]      # => Return list starting from index 2 => [4, 3]
li[:3]      # => Return list from beginning until index 3 => [1, 2, 4]
li[::2]     # => Return list selecting elements with a step size of 2 => [1, 4]
li[::-1]    # => Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:] # => li2 = [1, 2, 4, 3] 
li2 is li   # => False

# Remove arbitrary elements from a list with "del"
del li[2]   # => li is now [1, 2, 3]

# Remove first occurrence of a value
li.remove(2)    # li is now [1, 3]
li.remove(2)    # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2) # li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2)     # => 1
li.index(4)     # Raises a ValueError as 2 is not in the list

# You can add lists
# Note: values for li and for other_li are not modified.
li + other_li # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li) # Now li is [1, 2, 3, 4, 5, 6]

# Check for existence in a list with "in"
1 in li # => True

# Examine the length with "len()"
len(li) # => 6


# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]  # => 1
tup[0] = 3  # Raise a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# You can do most of the list operations on tuples too
len(tup)    # => 3
tup + (4, 5, 6) # => (1, 2, 3, 4, 5, 6)
tup[:2]     # => (1, 2)
2 in tup    # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3) #  a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4) # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6   # Tuple 4, 5, 6 is unpacked into variables d, e and f
# respectively such that d = 4, e =5, f = 6
# Now look how easy it is to swap two values
e, d = d, e # d is now 5 and e is now 4


# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
invalid_dict = {[1,2,3]: "123"} # => Yield a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3): [1,2,3]} # Values can be of any type, however.

# Look up values with []
filled_dict["one"]  # => 1

# Get  all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later. Note - for Python
# versions < 3.7, dictionary key ordering is not guaranteed. Your results might
# not match the example below exactly. However, as of Python 3.7, dictionary
# items maintain the order at which they are inserted into the dictionary.
list(filled_dict.keys())    # => ["three", "two", "one"] in Python < 3.7
list(filled_dict.keys())    # => ["one", "two", "three"] in Python 3.7+


