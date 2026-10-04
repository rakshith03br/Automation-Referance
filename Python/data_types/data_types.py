"""
## Python Data Types

Data Type	    Example	            Ordered?	            Mutable?	        Duplicates?	        Indexed?
---------       -----------         --------                -----------         -----------         --------------
int	            10	                —	                    ❌ No	            —	                —
float	        3.14	            —	                    ❌ No	            —	                —
str	            "hello"	            ✅ Yes	                ❌ No	            ✅ Yes	            ✅ Yes
bool	        True, False	        —	                    ❌ No	            —	                —
list	        [1, 2, 3]	        ✅ Yes	                ✅ Yes	            ✅ Yes	            ✅ Yes
tuple	        (1, 2, 3)	        ✅ Yes	                ❌ No	            ✅ Yes	            ✅ Yes
set	            {1, 2, 3}	        ❌ No	                ✅ Yes	            ❌ No	            ❌ No
frozenset	    frozenset([1,2,3])	❌ No	                ❌ No	            ❌ No	            ❌ No
dict	        {"a": 1, "b": 2}	✅ Yes (insertion order)✅ Yes	            ❌ No (keys unique)	❌ No (accessed by key)
NoneType	    None	            —	                    —	                —	                —

## Grouped by category
    Numeric: `int`, `float`, `complex`
    Text: `str`
    Sequence: `list`, `tuple`, `range`
    Set: `set`, `frozenset`
    Mapping: `dict`
    Boolean: `bool`
    Binary: `bytes`, `bytearray`, `memoryview`
    None: `NoneType`

## Mutable vs Immutable — the key divide

Mutable ✅    | Immutable ❌
`list`        | `int`, `float`
`dict`        | `str`
`set`         | `tuple`
 -            | `frozenset`
 -            | `bool`

Key takeaway:
    When picking a data type, ask two questions —
        1. do I need order/position?
        2. will this data change after creation?
    That decision tree gets you to the right type almost every time:
        - Need key-based lookup → dict
        - Need order + changeable → list
        - Need order + fixed/safe → tuple
        - Need uniqueness + fast lookup → set
"""

## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION
## ==========================================================
# The table above is a great reference, but interviewers usually want you to
# PROVE these properties with code and explain WHY they matter. Below is a
# runnable walkthrough of every type in the table, plus commonly-missed types.

# -------------------------
# 1. Checking type() and confirming the table's claims with code
# -------------------------
print(type(10))                 # <class 'int'>
print(type(3.14))               # <class 'float'>
print(type("hello"))            # <class 'str'>
print(type(True))               # <class 'bool'>
print(type([1, 2, 3]))          # <class 'list'>
print(type((1, 2, 3)))          # <class 'tuple'>
print(type({1, 2, 3}))          # <class 'set'>
print(type(frozenset([1, 2, 3])))  # <class 'frozenset'>
print(type({"a": 1, "b": 2}))    # <class 'dict'>
print(type(None))                 # <class 'NoneType'>

print(f"{'*' * 60}")

# -------------------------
# 2. Proving mutability vs immutability with id()
# -------------------------
# Immutable: any "change" actually creates a NEW object (id() changes)
s = "hello"
print(id(s))
s += " world"
print(id(s))     # DIFFERENT id -> a new string object was created, original untouched

# Mutable: changing in place keeps the SAME id()
lst = [1, 2, 3]
print(id(lst))
lst.append(4)
print(id(lst))    # SAME id -> modified in place, no new object created

print(f"{'*' * 60}")

# -------------------------
# 3. Ordered vs unordered - proving list/tuple/dict preserve order, set does not
# -------------------------
ordered_list = [3, 1, 2]
print(ordered_list)          # [3, 1, 2] -> insertion order preserved, always
ordered_dict = {"z": 1, "a": 2, "m": 3}
print(list(ordered_dict))     # ['z', 'a', 'm'] -> insertion order preserved (3.7+ guarantee)

unordered_set = {3, 1, 2}
print(unordered_set)           # order NOT guaranteed - may print in any order,
                                 # and should never be relied upon for sequence

print(f"{'*' * 60}")

# -------------------------
# 4. Duplicates - list/tuple allow, set/frozenset/dict-keys don't
# -------------------------
print([1, 1, 2, 2])         # [1, 1, 2, 2] -> duplicates kept
print({1, 1, 2, 2})          # {1, 2}       -> automatically deduplicated
d = {"a": 1, "a": 2}          # dict literal with duplicate key
print(d)                        # {'a': 2} -> LAST value wins, no error raised!

print(f"{'*' * 60}")

# -------------------------
# 5. Indexed vs not indexed - accessing elements by position vs key vs membership only
# -------------------------
lst = [10, 20, 30]
print(lst[0])          # 10 -> indexed access works

s = {10, 20, 30}
# print(s[0])            # TypeError: 'set' object is not subscriptable

d = {"a": 1}
print(d["a"])            # 1 -> accessed by KEY, not by integer position
# print(d[0])              # KeyError (unless 0 happens to be an actual key)

print(f"{'*' * 60}")

# -------------------------
# 6. Numeric types beyond int/float - complex (from the "grouped by category" list)
# -------------------------
c = 3 + 4j
print(type(c), c.real, c.imag)   # <class 'complex'> 3.0 4.0

print(f"{'*' * 60}")

# -------------------------
# 7. range - a memory-efficient sequence type (often forgotten in this list)
# -------------------------
r = range(5)
print(type(r))         # <class 'range'>
print(list(r))          # [0, 1, 2, 3, 4] -> materializes lazily, doesn't store all values upfront
print(r[2])              # 2 -> range IS indexed, despite being a lazy sequence
print(len(range(1_000_000_000)))   # instant! range doesn't actually build a billion-item list

print(f"{'*' * 60}")

# -------------------------
# 8. Binary types - bytes, bytearray, memoryview (also often forgotten)
# -------------------------
b = bytes([65, 66, 67])
print(b, type(b))            # b'ABC' <class 'bytes'> -> IMMUTABLE sequence of integers (0-255)

ba = bytearray([65, 66, 67])
print(ba, type(ba))            # bytearray(b'ABC') <class 'bytearray'> -> MUTABLE version of bytes
ba[0] = 90
print(ba)                        # bytearray(b'ZBC') -> can modify in place, unlike bytes

mv = memoryview(ba)
print(mv, type(mv))              # <memory at ...> <class 'memoryview'> -> view into the buffer
                                    # WITHOUT copying it - useful for large binary data / performance

print(f"{'*' * 60}")

# -------------------------
# 9. frozenset - the immutable counterpart to set (worth demonstrating directly)
# -------------------------
fs = frozenset([1, 2, 3])
# fs.add(4)          # AttributeError: 'frozenset' object has no attribute 'add'
print(fs)              # frozenset({1, 2, 3})

# frozenset is HASHABLE (regular set is NOT) - so it CAN be used as a dict key
# or nested inside another set, unlike a regular set:
d = {frozenset([1, 2]): "pair"}
print(d)                 # {frozenset({1, 2}): 'pair'}
# d2 = {set([1, 2]): "pair"}   # TypeError: unhashable type: 'set'

print(f"{'*' * 60}")

# -------------------------
# 10. NoneType and identity checks
# -------------------------
x = None
print(type(x))          # <class 'NoneType'>
print(x is None)         # True -> ALWAYS use 'is' for None comparisons, not =='
print(x == None)          # True, but considered bad practice (custom __eq__ could break this)

print(f"{'*' * 60}")

# -------------------------
# 11. Choosing the right type - practical decision-making examples
# -------------------------
# Need key-based lookup -> dict
user = {"name": "Alice", "age": 30}

# Need order + changeable -> list
shopping_cart = ["milk", "eggs", "bread"]
shopping_cart.append("butter")

# Need order + fixed/safe (e.g. coordinates that shouldn't change) -> tuple
coordinates = (12.9716, 77.5946)

# Need uniqueness + fast membership testing -> set
seen_ids = {101, 102, 103}
print(104 in seen_ids)   # O(1) average time -> much faster than `104 in [101,102,103]` for large data

print(f"{'*' * 60}")

# -------------------------
# 12. Type conversion between the major types (very common in real code/interviews)
# -------------------------
print(list((1, 2, 3)))        # [1, 2, 3] -> tuple to list
print(tuple([1, 2, 3]))        # (1, 2, 3) -> list to tuple
print(set([1, 1, 2, 3]))        # {1, 2, 3} -> list to set (dedupes)
print(list({1, 2, 3}))           # [1, 2, 3] -> set to list
print(dict([("a", 1), ("b", 2)]))  # {'a': 1, 'b': 2} -> list of pairs to dict
print(list({"a": 1, "b": 2}.items()))  # [('a', 1), ('b', 2)] -> dict to list of pairs


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON DATA TYPES
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What are Python's built-in data types, grouped by category (numeric, text,
#    sequence, set, mapping, boolean, binary, none)?
#
# 2. What is the difference between a list and a tuple? Given that both are
#    ordered and allow duplicates, why would you choose one over the other?
#
# 3. Why is a tuple generally faster to create and iterate over than a list of
#    the same elements?
#
# 4. What's the difference between a set and a frozenset? Why is frozenset
#    hashable while set is not, and what practical difference does that make?
#
# 5. Why does a dict allow duplicate VALUES but not duplicate KEYS? What
#    happens if you write a dict literal with the same key twice?
#
# 6. How would you prove, using id(), that strings are immutable and lists are
#    mutable in Python?
#
# 7. What is the time complexity of membership testing (`x in y`) for a list
#    versus a set? Why the difference?
#
# 8. What is `range()`, and why is `range(10**9)` created instantly without
#    consuming huge memory? How is it different from a list of the same
#    numbers?
#
# 9. What are bytes, bytearray, and memoryview used for? Which one is mutable,
#    and when would you reach for memoryview specifically?
#
# 10. Why can't you use a list or a set as a dictionary key, but you CAN use a
#     tuple or a frozenset?
#
# 11. Since Python 3.7, dict preserves insertion order. Does that mean dict is
#     now considered an "ordered" type in the same sense as list? What's the
#     nuance here?
#
# 12. Given a mix of data (e.g., needing uniqueness AND insertion order AND
#     mutability), how would you decide between list, set, and dict as your
#     underlying structure?
#
# 13. What does `x == None` do differently from `x is None`? Why is `is`
#     preferred, and can `==` ever give a misleading answer here?
#
# 14. Why is `complex` considered a numeric type in Python but not commonly
#     used in typical business/backend code? Give a domain where it IS useful.
#
# 15. What is the practical difference between deep equality (`==`) and
#     identity (`is`) when comparing two different data type instances that
#     look equal (e.g., two lists with the same elements)?
#
# 16. How would you convert a list of (key, value) tuples into a dictionary,
#     and vice versa?
#
# 17. Why does converting a list to a set (e.g., `set(my_list)`) sometimes
#     change the order of elements when converted back to a list?
#
# 18. If you need both fast lookups AND to preserve insertion order AND to
#     store key-value pairs, which built-in type do you reach for, and why?
#
# 19. Is `bool` considered a distinct data type, or is it more accurately
#     described as something else in Python's type system? What evidence
#     supports your answer?
#
# 20. When would choosing a mutable type (like a list) for a function's
#     default argument value cause a bug? How does this connect back to the
#     mutable/immutable distinction in this table?