"""
dict (Dictionary) in Python

A dictionary is a collection of key-value pairs. Instead of accessing items by position (like lists/tuples), you
    access them by a unique key.

    - Ordered (Python 3.7+) — insertion order is preserved
    - Mutable — you can add, update, remove items
    - Keys must be unique — no duplicate keys allowed
    - Keys must be immutable/hashable — strings, numbers, tuples (not lists)
    - Values can be anything — any data type, duplicates allowed
"""
d = {} ## '{}' is used to create empty dictionary
d1 = dict() ## 'dict()' keyword is used to create empty dictionary
print(type(d)) # <class 'dict'>
print(type(d1)) # <class 'dict'>

# Keys, values, and items
d = {"name": "Alice", "age": 25, "city": "Bangalore"}
print(d.keys())    # dict_keys(['name', 'age', 'city'])
print(d.values())  # dict_values(['Alice', 25, 'Bangalore'])
print(d.items())   # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Bangalore')])

Employee = {"Name": "Rakshith", "Age": 25, "salary": 25000, "Place": "Bangalore"}
print(type(Employee))  # <class 'dict'>

# accessing values of dict
print(Employee["Name"])  # Rakshith
print(Employee["Age"])  # 25
print(Employee.get("Age"))     # 25
print(Employee.get("email", "Not Found"))  # Not Found — custom default value

# check if key is present or not
# Membership check
# Membership checks look at keys by default, not values:
print("Name" in Employee)  # True
print("Age" in Employee)  # True
print("Dubai" in Employee)  # False
print("Rakshith" in Employee.values())  # True — need .values() to check values


# changing/updating value of the key
print(Employee) #
Employee["Age"] = 35
print(Employee) # {'Name': 'Rakshith', 'Age': 35, 'salary': 25000, 'Place': 'Bangalore'}
Employee.update({"Place": "Karnataka"})
print(Employee) # {'Name': 'Rakshith', 'Age': 35, 'salary': 25000, 'Place': 'Karnataka'}

# add item(key,value) to dict
Employee["Bike"] = "KTM"
print(Employee)
Employee.update({"Distance": [10, 20, 30]})
print(Employee)

# delete/remove item using key name
del Employee["Place"]
print(Employee) ## {'Name': 'Rakshith', 'Age': 35, 'salary': 25000, 'Bike': 'KTM', 'Distance': [10, 20, 30]}
Employee.pop("Distance")
print(Employee) ## {'Name': 'Rakshith', 'Age': 35, 'salary': 25000, 'Bike': 'KTM'}

# delete last item
Employee.popitem()
print(Employee) ## {'Name': 'Rakshith', 'Age': 35, 'salary': 25000}

# clear all items
Employee.clear()
print(Employee) ## {}

## Dictionary slicing
import itertools
Employee = {"Name": "Rakshith", "Age": 25, "salary": 25000, "Place": "Bangalore"}
print(dict(itertools.islice(Employee.items(), 2)))      # {'Name': 'Rakshith', 'Age': 25}
print(dict(itertools.islice(Employee.items(), 2, 3)))       # {'salary': 25000}
print(dict(itertools.islice(Employee.items(), 2, 4)))       # {"salary": 25000, "Place": "Bangalore"}
print(dict(itertools.islice(Employee.items(), 5)))      # {'Name': 'Rakshith', 'Age': 25, 'salary': 25000, 'Place': 'Bangalore'}

Employee = {}


# # Accessing the dictionary values
# def fun():
#     Employee["Name"]="Rohith"
#     print(Employee)
#     Employee["Name"]=input("Enter the name: ")
#     print(Employee)
# fun()
"""
{'Name': 'Rohith'}
Enter the name: Rakshith
{'Name': 'Rakshith'}
"""
####################################
# # Adding key:Values dictionary
# def fun():
#     Employee["Company"]='CN'
#     Employee["Employee_Id"]=[1,2,3,4]
#     print(Employee) ## {'Company': 'CN', 'Employee_Id': [1, 2, 3, 4]}
# fun()
####################################
# # Deleting Elements using del Keys name
# def fun():
#     Employee["Company"] = 'CN'
#     Employee["Employee_Id"] = [1, 2, 3, 4]
#     print(Employee) ## {'Company': 'CN', 'Employee_Id': [1, 2, 3, 4]}
#     del Employee["Employee_Id"]
#     print(Employee) ## {'Company': 'CN'}
# fun()
####################################
# # Deleting Elements using pop() Method
# def fun():
#     Employee["Company"] = 'CN'
#     Employee["Employee_Id"] = [1, 2, 3, 4]
#     print(Employee) ## {'Company': 'CN', 'Employee_Id': [1, 2, 3, 4]}
#     Employee.pop("Company")
#     print(Employee) ## {'Employee_Id': [1, 2, 3, 4]}
# fun()
####################################
Employees = {"Name": "Rakshith", "Age": 25, "salary": 25000, "Place": "Bangalore"}
####################################
# # Print the keys in the dictionary
# def fun(Employees):
#     for i in Employees:
#         print(i)
# fun(Employees)
####################################
# # Print the keys in the dictionary by using keys() method
# def fun(Employees):
#     for i in Employees.keys():
#         print(i)
# fun(Employees)

####################################
# # Print all the values of the dictionary
# def fun(Employees):
#     for i in Employees:
#         print(Employees[i])
# fun(Employees)
####################################
# # Print the values of the dictionary by using values() method.
# def fun(Employees):
#     for i in Employees.values():
#         print(i)
# fun(Employees)
####################################
# Print the items of the dictionary by using items() method
# def fun(Employees):
#     for i in Employees.items():
#         print(i)
# fun(Employees)
"""
('Name', 'Rakshith')
('Age', 25)
('salary', 25000)
('Place', 'Bangalore')
"""
####################################
# # Print the items of the dictionary by using items() method
# def fun(Employees):
#     for i, j in Employees.items():
#         print(i, ":", j)
# fun(Employees)
"""
Name : Rakshith
Age : 25
salary : 25000
Place : Bangalore
"""
####################################
# # len() function
# print(len(Employees)) ## 4
#
# # sorted() function will sort the keys and returns in the list
# print(sorted(Employees)) ## ['Age', 'Name', 'Place', 'salary']
#
# # copy() method
# d = Employees.copy()
# print(d) ## {'Name': 'Rakshith', 'Age': 25, 'salary': 25000, 'Place': 'Bangalore'}

############## dict comprehension ##############
# # using zip() method
# """
# The zip() function in Python is used to combine multiple iterables (like lists, tuples, etc.) element-wise into tuples,
#  creating an iterator of tuples.
# """
# def fun():
#     d = {x: y for x, y in zip(key, value)}
#     d1 = dict(zip(key,value))
#     print(d) ## {'p': 56, 'q': 67, 'r': 43, 's': 12, 't': 6}
#     print(d1) ## {'p': 56, 'q': 67, 'r': 43, 's': 12, 't': 6}
# key = ['p', 'q', 'r', 's', 't']
# value = [56, 67, 43, 12, 6]
# fun()
#################################################
# # square of numbers in the list
# def fun():
#     d = {n: n**2 for n in [1, 2, 3, 4, 5]}
#     print(d) ## {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# fun()
#################################################
# # cube of numbers in the list
# def fun():
#     d = {n: n**3 for n in [1, 2, 3, 4, 5]}
#     print(d) ## {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
# fun()
#################################################
# # for string
# def fun():
#     d = {i: i*4 for i in 'string'}
#     print(d) ## {'s': 'ssss', 't': 'tttt', 'r': 'rrrr', 'i': 'iiii', 'n': 'nnnn', 'g': 'gggg'}
# fun()
#################################################
# # using range
# def fun():
#     d = {i: i*2 for i in range(0, 10)}
#     print(d) ## {0: 0, 1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
# fun()
#################################################
# #Conditional statements
# def fun():
#     d = {i: i*2 for i in range(10) if i % 2 == 0}
#     d1 = {i: i*2 for i in range(10) if i % 2 != 0}
#     print(d) ## {0: 0, 2: 4, 4: 8, 6: 12, 8: 16} even
#     print(d1) ## {1: 2, 3: 6, 5: 10, 7: 14, 9: 18} odd
# fun()
#################################################
# def fun():
#     d = dict()
#     for i in range(10):
#         d[i] = i*i
#     print(d) ## {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
#     d1 = {i: i*i for i in range(10)}
#     print(d1)
# fun()
#------------------------------------------------------------------------------------------------
"""
Nested dictionaries
    Dictionaries can hold other dictionaries — useful for structured/JSON-like data:
"""
employee = {
    "name": "Alice",
    "salary": 50000,
    "address": {
        "city": "Bangalore",
        "pincode": 560001
    }
}
print(employee["address"]["city"])  # Bangalore
#---------------------------------------------------------------------------------------------
"""
Why keys must be immutable
    Keys must be hashable (immutable), so they can be strings, numbers, or tuples — but not lists:
"""
d = {(1, 2): "point A"}   # ✅ tuple as key — works
# d = {[1, 2]: "point A"}   # ❌ TypeError — list can't be a key (mutable, unhashable)
#---------------------------------------------------------------------------------------------
# Merging dictionaries
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4, "d": 5}

# 1. Using ** unpacking (Python 3.5+)
merged = {**d1, **d2}       # ** unpacking
print(merged)       # {'a': 1, 'b': 3, 'c': 4, 'd': 5}

# 2. Using | operator (Python 3.9+) — cleanest way
merged_1 = d1 | d2      # | operator
print(merged_1)

# 3. Using dict.update() — modifies in place
d1.update(d2)
print(d1)

# 4. Using dict() constructor with unpacking
merged = dict(d1, **d2)
print(merged)

# 5. Using collections.ChainMap (keeps both dicts separate, doesn't create a new merged copy)
from collections import ChainMap

merged = ChainMap(d1, d2)
print(dict(merged))



"""
Quick summary
Feature	                    Dict
--------------              ---------------------------------------
Ordered?	                ✅ Yes (insertion order, since Python 3.7)
Indexed?	                ❌ No (accessed by key, not position)
Mutable?	                ✅ Yes
Duplicate keys?	            ❌ Not allowed (last one wins if repeated)
Common use	                Storing structured/labeled data, fast lookups by key
"""


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================

# -------------------------
# 1. setdefault() - get-or-insert in a SINGLE call (very commonly asked)
# -------------------------
d = {"a": 1}
val = d.setdefault("a", 100)   # key exists -> returns EXISTING value, doesn't overwrite
print(val, d)                     # 1 {'a': 1}

val2 = d.setdefault("b", 200)    # key missing -> INSERTS 'b': 200 AND returns 200
print(val2, d)                      # 200 {'a': 1, 'b': 200}

# Classic real-world use: grouping items by key without defaultdict
groups = {}
pairs = [("fruit", "apple"), ("veg", "carrot"), ("fruit", "banana")]
for category, item in pairs:
    groups.setdefault(category, []).append(item)   # creates [] only if key is missing
print(groups)   # {'fruit': ['apple', 'banana'], 'veg': ['carrot']}

print(f"{'*' * 60}")

# -------------------------
# 2. dict.fromkeys() - create a dict from a list of keys with a shared default value
# -------------------------
keys = ["a", "b", "c"]
d = dict.fromkeys(keys, 0)
print(d)   # {'a': 0, 'b': 0, 'c': 0}

# GOTCHA: if the default value is MUTABLE (like a list), ALL keys share the
# SAME object - same trap as mutable default arguments!
d_bug = dict.fromkeys(keys, [])
d_bug["a"].append(1)
print(d_bug)   # {'a': [1], 'b': [1], 'c': [1]} -> BUG! all keys point to the SAME list

print(f"{'*' * 60}")

# -------------------------
# 3. Dict views (.keys(), .values(), .items()) are LIVE, not snapshots
# -------------------------
d = {"x": 1, "y": 2}
keys_view = d.keys()
print(keys_view)     # dict_keys(['x', 'y'])
d["z"] = 3
print(keys_view)      # dict_keys(['x', 'y', 'z']) -> automatically reflects the update!

# Dict views also support set-like operations (keys are always unique):
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
print(d1.keys() & d2.keys())   # {'b'}         -> intersection
print(d1.keys() | d2.keys())    # {'a', 'b', 'c'} -> union
print(d1.keys() - d2.keys())     # {'a'}          -> difference

print(f"{'*' * 60}")

# -------------------------
# 4. RuntimeError: modifying a dict's size while iterating over it
# -------------------------
d = {"a": 1, "b": 2, "c": 3}
try:
    for key in d:
        if key == "b":
            del d[key]     # mutating size DURING iteration
except RuntimeError as e:
    print("RuntimeError:", e)   # dictionary changed size during iteration

# SAFE way: iterate over a COPY of the keys if you need to delete during iteration
d = {"a": 1, "b": 2, "c": 3}
for key in list(d.keys()):   # list() takes a snapshot, safe to mutate original
    if key == "b":
        del d[key]
print(d)   # {'a': 1, 'c': 3}

print(f"{'*' * 60}")

# -------------------------
# 5. Dict equality - order-independent (unlike list/tuple)
# -------------------------
d1 = {"a": 1, "b": 2}
d2 = {"b": 2, "a": 1}
print(d1 == d2)   # True -> dict equality only cares about key-value PAIRS, not insertion order

print(f"{'*' * 60}")

# -------------------------
# 6. Sorting a dictionary - by key or by value
# -------------------------
scores = {"bob": 85, "alice": 92, "carol": 78}
by_key = dict(sorted(scores.items()))                          # sort by key
print(by_key)    # {'alice': 92, 'bob': 85, 'carol': 78}

by_value = dict(sorted(scores.items(), key=lambda item: item[1], reverse=True))  # sort by value, descending
print(by_value)   # {'alice': 92, 'bob': 85, 'carol': 78}

print(f"{'*' * 60}")

# -------------------------
# 7. Time complexity - the interview theory behind dict's speed
# -------------------------
# dict is implemented as a HASH TABLE internally:
#   - get/set/delete/'in' check -> O(1) average case
#   - worst case O(n) is theoretically possible with severe hash collisions,
#     but extremely rare in practice with Python's hashing
# Compare with list membership check (`x in my_list`) -> O(n) always, since it
# must potentially scan every element. This is WHY dict/set are preferred for
# fast lookups over lists when checking "does this exist?"

print(f"{'*' * 60}")

# -------------------------
# 8. |= operator - in-place merge (Python 3.9+), companion to the | operator
# -------------------------
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d1 |= d2          # equivalent to d1.update(d2), but using operator syntax
print(d1)           # {'a': 1, 'b': 3, 'c': 4}

print(f"{'*' * 60}")

# -------------------------
# 9. get() with a default vs setdefault() - the key difference
# -------------------------
d = {"a": 1}
print(d.get("z", 0))    # 0 -> returns default, does NOT add 'z' to the dict
print(d)                   # {'a': 1} -> unchanged

print(d.setdefault("z", 0))   # 0 -> returns default AND ADDS 'z' to the dict
print(d)                         # {'a': 1, 'z': 0} -> 'z' was inserted!

print(f"{'*' * 60}")

# -------------------------
# 10. Nested dict comprehension and zip-based construction (recap + extension)
# -------------------------
keys_list = ['p', 'q', 'r']
values_list = [10, 20, 30]
zipped_dict = dict(zip(keys_list, values_list))
print(zipped_dict)   # {'p': 10, 'q': 20, 'r': 30}

# swapping keys and values (common coding-round question)
original = {"a": 1, "b": 2, "c": 3}
swapped = {v: k for k, v in original.items()}
print(swapped)   # {1: 'a', 2: 'b', 3: 'c'}

# nested dict comprehension - multiplication table
mult_table = {i: {j: i * j for j in range(11, 14)} for i in range(1, 4)}
print(mult_table)   # {1: {11: 11, 12: 12, 13: 13}, 2: {11: 22, 12: 24, 13: 26}, 3: {11: 33, 12: 36, 13: 39}}


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON DICTIONARIES
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the difference between dict.get(key, default) and
#    dict.setdefault(key, default)? Which one modifies the dictionary?
#
# 2. Why must dictionary keys be hashable? What types can and cannot be used
#    as dictionary keys, and why?
#
# 3. What is the time complexity of key lookup, insertion, and deletion in a
#    dictionary? How does this compare to a list, and why the difference?
#
# 4. What happens if you try to add or remove a key from a dictionary WHILE
#    iterating over it directly? How would you safely delete keys during
#    iteration?
#
# 5. Are dict.keys(), dict.values(), and dict.items() snapshots or live views?
#    How would you demonstrate this with code?
#
# 6. Since Python 3.7, dicts preserve insertion order. Does this mean two
#    dicts with the same key-value pairs but different insertion order are
#    considered unequal (==)? Why or why not?
#
# 7. What is the gotcha with using dict.fromkeys(keys, some_mutable_default)?
#    How is it similar to the mutable default argument problem in functions?
#
# 8. What are the different ways to merge two dictionaries in Python? What are
#    the differences between {**d1, **d2}, d1 | d2, d1.update(d2), and
#    ChainMap(d1, d2)?
#
# 9. If two dictionaries being merged have overlapping keys, which value wins?
#    Does the order of the dicts in the merge expression matter?
#
# 10. What does dict.keys() support that a regular list doesn't (hint: think
#     set-like operations such as intersection and union)?
#
# 11. How would you sort a dictionary by its values instead of its keys?
#     What built-in function and parameter would you use?
#
# 12. What is the difference between "del d[key]" and "d.pop(key)"? What
#     happens if the key doesn't exist in each case, and how would you avoid
#     a KeyError?
#
# 13. What does dict.popitem() remove, and has its removal order changed
#     across Python versions?
#
# 14. How would you access a deeply nested value in a dictionary (e.g., a
#     JSON-like structure) safely, without raising a KeyError if an
#     intermediate key is missing?
#
# 15. What is ChainMap, and how is it different from actually merging two
#     dictionaries into a new one?
#
# 16. How would you invert a dictionary (swap its keys and values)? What
#     happens if the original dictionary's values are not unique?
#
# 17. Why does a dict literal like {"a": 1, "a": 2} not raise an error? What
#     value ends up being stored for the key "a"?
#
# 18. What is a dictionary comprehension, and how would you write one that
#     filters items based on a condition (e.g., only even values)?
#
# 19. What's the difference between iterating "for key in dict" versus
#     "for key in dict.keys()"? Is there any practical difference?
#
# 20. How is a Python dict implemented internally (at a high level)? Why does
#     this implementation allow O(1) average-case lookups?