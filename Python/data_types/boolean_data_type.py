# boolean data type

a = True
b = False
print(type(a))
print(type(b))


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. bool is a SUBCLASS of int (classic interview gotcha)
# -------------------------
print(isinstance(True, int))    # True -> bool inherits from int
print(issubclass(bool, int))    # True

# Internally: True == 1 and False == 0
print(True == 1)     # True
print(False == 0)    # True
print(True + True)   # 2   -> arithmetic works because bool IS an int
print(True * 5)      # 5
print(sum([True, True, False, True]))  # 3 -> counts True values, common trick

print(f"{'*' * 50}")

# -------------------------
# 2. bool has only TWO instances: True and False (singletons)
# -------------------------
x = True
y = True
print(x is y)    # True -> always safe to use 'is' with True/False (unlike other objects)
print(x is True) # True -> preferred check is `if x:` not `if x is True:` (see gotcha below)

print(f"{'*' * 50}")

# -------------------------
# 3. Truthy and Falsy values (VERY common interview topic)
# -------------------------
# Everything in Python has an inherent truth value when used in a boolean context.
# FALSY values in Python (this is the complete list):
#   False, None, 0, 0.0, 0j, '', [], (), {}, set(), range(0)
# Everything else is truthy.

print(bool(0))          # False
print(bool(0.0))        # False
print(bool(""))         # False -> empty string
print(bool([]))         # False -> empty list
print(bool({}))         # False -> empty dict
print(bool(set()))      # False -> empty set
print(bool(None))       # False

print(bool(1))           # True
print(bool(-1))          # True -> any nonzero number is truthy, including negatives
print(bool("False"))     # True -> non-empty string, even the word "False", is truthy!
print(bool([0]))         # True -> non-empty list (even containing falsy items) is truthy
print(bool(" "))         # True -> a single space is a non-empty string -> truthy

print(f"{'*' * 50}")

# -------------------------
# 4. bool() conversion / constructor
# -------------------------
print(bool("hello"))    # True
print(bool(3.14))       # True
print(bool(-0.0))       # False -> -0.0 is still considered zero

print(f"{'*' * 50}")

# -------------------------
# 5. Comparison operators ALWAYS return a bool
# -------------------------
print(type(5 > 3))       # <class 'bool'>
print(5 == 5)             # True
print(5 != 3)              # True
print(3 < 5 < 10)          # True -> CHAINED comparison: equivalent to (3 < 5) and (5 < 10)
print(10 > 5 > 8)          # False -> equivalent to (10 > 5) and (5 > 8) -> True and False

print(f"{'*' * 50}")

# -------------------------
# 6. Logical operators: and, or, not (SHORT-CIRCUIT evaluation)
# -------------------------
# 'and'/'or' don't always return True/False - they return one of the OPERANDS.
print(True and False)   # False
print(1 and 2)           # 2   -> 'and' returns the SECOND operand if the first is truthy
print(0 and 2)           # 0   -> 'and' returns the FIRST operand if it's falsy (short-circuits)
print(1 or 2)             # 1   -> 'or' returns the FIRST operand if it's truthy (short-circuits)
print(0 or 2)             # 2   -> 'or' returns the SECOND operand if the first is falsy
print(not True)           # False
print(not 0)               # True -> not converts to bool first, then inverts

# Practical use: default values via 'or'
name = "" or "Anonymous"
print(name)   # 'Anonymous' -> common pattern, though `x if x else default` is more explicit

# Short-circuit avoids errors - second operand never evaluated if not needed
def risky():
    print("risky() was called")
    return True

print(False and risky())   # False -> risky() is NEVER called, avoids unnecessary/unsafe call
print(True or risky())      # True  -> risky() is NEVER called

print(f"{'*' * 50}")

# -------------------------
# 7. Logical (and/or/not) vs Bitwise (&, |, ~) operators - IMPORTANT distinction
# -------------------------
# and/or/not -> work on truthy/falsy values, short-circuit, meant for booleans/conditionals
# &, |, ~     -> work bit-by-bit on integers (or element-wise on things like numpy arrays/pandas Series)
#                do NOT short-circuit, both sides always evaluated

print(True & False)   # False -> works because bool is int under the hood (bitwise AND: 1 & 0)
print(True | False)   # True
print(~True)           # -2   -> bitwise NOT on int 1 -> -(1+1) = -2 (NOT a bool!)
print(type(~True))     # <class 'int'> -> ~ on a bool returns an int, not a bool

# common bug: using & instead of and for boolean logic in plain Python code
# a = 5
# if a > 0 & a < 10:   # WRONG! & has higher precedence than comparison operators,
#                       # this actually evaluates as: a > (0 & a) < 10 -> unexpected!
# Correct: if a > 0 and a < 10:

print(f"{'*' * 50}")

# -------------------------
# 8. all() and any() - built-ins that work great with booleans/iterables
# -------------------------
print(all([True, True, True]))     # True  -> True if ALL elements are truthy (or iterable is empty)
print(all([True, False, True]))    # False
print(all([]))                      # True  -> vacuously true for empty iterable
print(any([False, False, True]))    # True  -> True if AT LEAST ONE element is truthy
print(any([]))                       # False -> vacuously false for empty iterable

nums = [2, 4, 6, 8]
print(all(n % 2 == 0 for n in nums))   # True -> works great with generator expressions

print(f"{'*' * 50}")

# -------------------------
# 9. Custom objects and truthiness: __bool__ and __len__
# -------------------------
# Python checks __bool__() first; if not defined, falls back to __len__() (0 = falsy);
# if neither is defined, the object is ALWAYS truthy.
class EmptyCart:
    def __len__(self):
        return 0    # no __bool__ defined, so Python uses __len__ to decide truthiness

cart = EmptyCart()
print(bool(cart))    # False -> because len(cart) == 0

class AlwaysTruthy:
    pass   # no __bool__, no __len__ -> defaults to True

print(bool(AlwaysTruthy()))   # True

class CustomBool:
    def __bool__(self):
        return False    # __bool__ takes priority over __len__ if both exist

print(bool(CustomBool()))   # False

print(f"{'*' * 50}")

# -------------------------
# 10. Common anti-pattern: comparing explicitly to True/False
# -------------------------
flag = True
# BAD (not Pythonic):
if flag == True:
    pass
# GOOD:
if flag:
    pass

# This matters MORE than it looks: if flag is something like 1 or "yes" (truthy but
# not literally True), `flag == True` can behave unexpectedly:
print(1 == True)      # True  -> because bool is a subclass of int
print("yes" == True)  # False -> non-bool truthy values are NOT == True!
if "yes":              # this works correctly (truthy check)
    print("this runs")

print(f"{'*' * 50}")

# -------------------------
# 11. Walrus operator (:=) often used alongside boolean conditions (Python 3.8+)
# -------------------------
data = [1, 2, 3, 4, 5]
# assign and test in one expression
if (n := len(data)) > 3:
    print(f"List is long, length = {n}")

print(f"{'*' * 50}")

# -------------------------
# 12. bool() on collections/containers - useful for "is empty" checks
# -------------------------
def process_items(items):
    if not items:              # Pythonic way to check for empty list/None
        print("No items to process")
        return
    print(f"Processing {len(items)} items")

process_items([])       # No items to process
process_items(None)     # No items to process
process_items([1, 2])   # Processing 2 items


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON BOOLEAN DATA TYPE
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. Is bool a separate primitive type in Python, or is it related to another type?
#    What does `issubclass(bool, int)` return, and what are the practical implications?
#
# 2. What are all the "falsy" values in Python? Name the complete list.
#
# 3. Why is `bool("False")` True even though the string literally says "False"?
#
# 4. What do the `and` and `or` operators actually RETURN in Python? Do they always
#    return True/False? Give an example showing otherwise.
#
# 5. What is short-circuit evaluation? Give a practical example where it prevents
#    an error (e.g., checking `x is not None and x.value > 0`).
#
# 6. What is the difference between the logical operators (and, or, not) and the
#    bitwise operators (&, |, ~) when used with booleans?
#
# 7. Why does `~True` return -2 instead of False? Explain what's happening under
#    the hood.
#
# 8. What's wrong with writing `if a > 0 & a < 10:` instead of
#    `if a > 0 and a < 10:`? (Hint: think about operator precedence.)
#
# 9. What do all() and any() return when called on an empty iterable? Why does
#    that make logical sense (vacuous truth)?
#
# 10. How does Python determine the truthiness of a custom object? Explain the
#     role of __bool__ and __len__, and which one takes priority.
#
# 11. Why is `if flag == True:` considered bad practice compared to `if flag:`?
#     Give a scenario where the two behave differently.
#
# 12. What does chained comparison like `3 < 5 < 10` actually evaluate to
#     internally? Is it the same as `(3 < 5) < 10`?
#
# 13. Is `True is True` guaranteed to be True in every case? Why can you safely
#     use 'is' with booleans, unlike with most other objects (e.g., strings, ints > 256)?
#
# 14. What does `sum([True, False, True, True])` return, and why does this work?
#
# 15. How would you check if a list, dict, or string is empty in a Pythonic way,
#     without using `len(x) == 0`?
#
# 16. What is the walrus operator (:=), and how can it be used to simplify a
#     condition that both assigns and Test_Cases a value?
#
# 17. What's the difference in behavior between `0 and some_function()` and
#     `0 & some_function()` in terms of whether some_function() gets called?
#
# 18. If a custom class defines neither __bool__ nor __len__, what is the
#     truthiness of its instances by default?
#
# 19. Why might using `or` for default values (e.g., `value = input_val or default`)
#     be risky in certain cases? (Hint: think about legitimate falsy inputs like 0.)
#
# 20. What does `True + True + False` evaluate to, and what type is the result?