"""
list in Python

A list is an ordered, mutable collection of items. It's probably the most commonly used data structure in
    Python — flexible enough to hold almost anything.

    - Ordered — items maintain a defined position (indexed)
    - Mutable — you can change, add, remove elements after creation
    - Allows duplicates — same value can appear multiple times
    - Can hold mixed data types — ints, strings, other lists, etc. all in one list
"""
l1 = [1, 2, 3, 4]
l2 = ["apple", "banana", "cherry"]
l3 = [1, "hello", 3.14, True]      # mixed types allowed
l4 = []                            # empty list
l5 = list()                        # also empty list
l6 = list((1, 2, 3))               # convert a tuple to a list

# list data type
l = ['India', 10, 20.33, "hello", 55, 66]

# +ve indexing numbers
#   [0        1  2         3       4   5]
# +ve indexing numbers
#   [-6        -5  -4         -3       -2   -1]
print(type(l))

# slicing used to access particular elements in list
print(l[1:4])
print(l[-1])
print(l[-3: -1])

## indexing
print(l[0])
print(type(l[0]))
# changing the value of the index
print(l)
l[1] = "changed"
print(l)

# inserting new item at specified index
l.insert(6, "new value")
print(l)
'''
l = [1, 2, 3]
l.append(4)          # adds single item to the end
print(l)              # [1, 2, 3, 4]

l.insert(1, 99)       # inserts 99 at index 1
print(l)              # [1, 99, 2, 3, 4]

l.extend([5, 6])      # adds multiple items to the end
print(l)              # [1, 99, 2, 3, 4, 5, 6]

l = [1, 2, 3]
l.append([4, 5])      # adds the WHOLE list as a single item
print(l)               # [1, 2, 3, [4, 5]]

l = [1, 2, 3]
l.extend([4, 5])       # adds EACH item individually
print(l)                # [1, 2, 3, 4, 5]
'''
# removing item by item name
l.remove("hello")
print(l)

# remove item by index using pop()
l.pop(1)
print(l)

"""
l = [1, 2, 3, 4, 5]

l.remove(3)      # removes first occurrence of the VALUE 3
print(l)          # [1, 2, 4, 5]

l.pop()           # removes and returns the LAST item
print(l)          # [1, 2, 4]

l.pop(0)          # removes and returns item at index 0
print(l)          # [2, 4]

del l[0]          # deletes item at given index
l.clear()         # empties the entire list
"""

# Common methods
l = [3, 1, 4, 1, 5, 9, 2]

len(l)          # 7 — length
l.count(1)      # 2 — how many times 1 appears
l.index(4)      # 2 — position of first occurrence of 4
l.sort()        # sorts in place → [1, 1, 2, 3, 4, 5, 9] # modifies original list
l.reverse()     # reverses in place
sorted(l)       # returns a NEW sorted list, doesn't modify original


# Membership check
l = [1, 2, 3]
print(2 in l)    # True
print(10 in l)   # False


# iterating through list and print index and item
for value in range(len(l)):
    print(value, ':', l[value])

## concatination of sequences
a = [0, 1, 2, 3, 4]
b = [6, 7, 8, 9, 10]
print(a + b)

# TypeError: can only concatenate list (not "str") to list
#print(a + "Hello")


def fun():
    l=[n**2 for n in [1,2,3,4,5]]
    print(l) # [1, 4, 9, 14, 25]
fun()

def fun():
    l=[i for i in "python"]
    print(l) # ['p','y','t','h','o','n']
fun()

def fun():
    l=[n for n in range(30) if n % 2 != 0]
    print(l) # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
fun()

def fun():
    l=[[i+j for i in range(5)] for j in range(3)]
    print(l)
fun()
'''
[
    [0,1,2,3,4],
    [1,2,3,4,5],
    [2,3,4,5,6]
]
'''
print('---------')
d = []
for i in range(10):
    d.append(i)
    print(d)
print()
print(d)

#-----------------------------------------------------------
# List comprehension
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0]
print(evens)    # [0, 2, 4, 6, 8]

#-----------------------------------------------------------
# Nested lists (list of lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # 6 — row 1, column 2

#-----------------------------------------------------------
# Copying a list — the classic pitfall
a = [1, 2, 3]
b = a              # b points to SAME list — not a copy!
b.append(4)
print(a)            # [1, 2, 3, 4] — a changed too!

# To make an actual copy:
c = a.copy()         # or a[:] or list(a)
c.append(5)
print(a)              # [1, 2, 3, 4] - unaffected

"""
List vs Tuple — quick comparison
Feature	            List	            Tuple
---------           ----------          -----------
Mutable?	        ✅ Yes	            ❌ No
Syntax	            [1, 2, 3]	        (1, 2, 3)
Speed	            Slower	            Faster
Use as dict key?	❌ No	            ✅ Yes
Common use	        Data that changes	Fixed data
"""
"""
Quick summary
Feature	                List
---------------         --------------------------------
Ordered?	            ✅ Yes
Indexed?	            ✅ Yes
Mutable?	            ✅ Yes
Duplicates allowed?	    ✅ Yes
Common use	            General-purpose, dynamic collections that grow/shrink/change
"""


## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. Slicing in depth - step, negative step, and slice assignment
# -------------------------
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[::2])       # [0, 2, 4, 6, 8] -> every 2nd element
print(nums[1::2])       # [1, 3, 5, 7, 9] -> every 2nd starting from index 1
print(nums[::-1])        # [9,8,7,6,5,4,3,2,1,0] -> reversed copy (doesn't mutate original)
print(nums[::-2])         # [9, 7, 5, 3, 1] -> reversed, every 2nd

# Slice ASSIGNMENT - can replace a chunk of the list (even with a different length!)
nums2 = [1, 2, 3, 4, 5]
nums2[1:3] = [99, 100, 101]   # replaces 2 elements with 3 -> list GROWS
print(nums2)                    # [1, 99, 100, 101, 4, 5]

nums3 = [1, 2, 3, 4, 5]
del nums3[1:3]                   # deletes a whole slice at once
print(nums3)                       # [1, 4, 5]

print(f"{'*' * 60}")

# -------------------------
# 2. List repetition (*) and the classic nested-list SHARED REFERENCE trap
# -------------------------
repeated = [0] * 5
print(repeated)          # [0, 0, 0, 0, 0] -> fine, ints are immutable, no sharing issue

# DANGER: repeating a MUTABLE object (like an inner list) shares ONE object!
grid_buggy = [[0] * 3] * 3     # creates 3 REFERENCES to the SAME inner list!
grid_buggy[0][0] = 99
print(grid_buggy)                 # [[99,0,0],[99,0,0],[99,0,0]] -> BUG! all rows changed

# CORRECT way to build a 2D grid - a fresh list for each row:
grid_fixed = [[0] * 3 for _ in range(3)]   # list comprehension creates a NEW list each iteration
grid_fixed[0][0] = 99
print(grid_fixed)                            # [[99,0,0],[0,0,0],[0,0,0]] -> only row 0 changed, correct!

print(f"{'*' * 60}")

# -------------------------
# 3. Sorting with key= and reverse= (recap, tailored to list.sort())
# -------------------------
words = ["banana", "kiwi", "apple", "fig"]
words.sort(key=len)                # sort in place by string length
print(words)                          # ['fig', 'kiwi', 'apple', 'banana']
words.sort(key=len, reverse=True)    # longest first
print(words)                            # ['banana', 'apple', 'kiwi', 'fig']

print(f"{'*' * 60}")

# -------------------------
# 4. List comprehension with MULTIPLE conditions, if-else, and nested loops
# -------------------------
# multiple 'if' conditions (acts like AND)
nums4 = [x for x in range(30) if x % 2 == 0 if x % 3 == 0]
print(nums4)   # [0, 6, 12, 18, 24] -> divisible by BOTH 2 and 3

# if-else INSIDE the expression (different from a filtering 'if' at the end!)
labeled = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(labeled)   # ['even', 'odd', 'even', 'odd', 'even']

# nested loops in a single comprehension (flattening a matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"{'*' * 60}")

# -------------------------
# 5. Extended unpacking with * when assigning from a list
# -------------------------
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

a, b, *rest = [10, 20, 30, 40]
print(a, b, rest)              # 10 20 [30, 40]

print(f"{'*' * 60}")

# -------------------------
# 6. List as a stack vs queue - performance implications (VERY common interview point)
# -------------------------
# STACK (LIFO) - list works great, both ends are O(1) at the END:
stack = []
stack.append(1)     # push -> O(1)
stack.append(2)
print(stack.pop())    # pop from end -> O(1)

# QUEUE (FIFO) - list is a BAD choice for this!
queue = [1, 2, 3]
# queue.pop(0)       # removes from the FRONT -> O(n)! every remaining item must shift left
# INSERT at the front is also O(n):
# queue.insert(0, 0)  # O(n)

# Use collections.deque instead for O(1) operations at BOTH ends:
from collections import deque
queue2 = deque([1, 2, 3])
queue2.popleft()   # O(1) -> deque is a doubly linked list internally

print(f"{'*' * 60}")

# -------------------------
# 7. Time complexity cheat-sheet for common list operations
# -------------------------
"""
Operation                  Time Complexity
------------------------   ------------------
index access lst[i]        O(1)
append(x)                  O(1) amortized
pop() (from end)            O(1)
pop(0) (from front)          O(n)
insert(0, x) (front)          O(n)
insert(i, x) (middle)          O(n)
remove(x)                       O(n) - must search for the value first
x in lst (membership test)       O(n)
len(lst)                           O(1) - length is cached, not recomputed
lst.sort()                          O(n log n) - Timsort
lst[a:b] (slicing)                    O(k) - k = size of the slice
"""

print(f"{'*' * 60}")

# -------------------------
# 8. copy() vs deepcopy() - recap specific to nested lists
# -------------------------
import copy
nested = [1, [2, 3], 4]
shallow = nested.copy()          # or nested[:] or list(nested)
deep = copy.deepcopy(nested)

nested[1].append(99)              # mutate the NESTED list
print(nested)                       # [1, [2, 3, 99], 4]
print(shallow)                        # [1, [2, 3, 99], 4] -> AFFECTED, shares the inner list
print(deep)                             # [1, [2, 3], 4]     -> NOT affected, fully independent

print(f"{'*' * 60}")

# -------------------------
# 9. enumerate() and zip() with lists - very common in real code and interviews
# -------------------------
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):        # gives (index, value) pairs
    print(index, fruit)

for i, fruit in enumerate(fruits, start=1):    # can start counting from a custom number
    print(i, fruit)

names = ["Alice", "Bob"]
ages = [30, 25]
for name, age in zip(names, ages):              # pairs elements from multiple lists together
    print(name, age)

# zip() stops at the SHORTEST iterable - no error, just truncates silently
print(list(zip([1, 2, 3], ["a", "b"])))            # [(1, 'a'), (2, 'b')] -> 3 is dropped, no error!

print(f"{'*' * 60}")

# -------------------------
# 10. bisect module - efficient insertion/search in an ALREADY SORTED list
# -------------------------
import bisect
sorted_list = [1, 3, 4, 4, 6, 8]
pos = bisect.bisect_left(sorted_list, 4)     # finds the LEFTMOST position to insert 4
print(pos)                                     # 2

bisect.insort(sorted_list, 5)                   # inserts 5 while KEEPING the list sorted
print(sorted_list)                                # [1, 3, 4, 4, 5, 6, 8]
# bisect operations are O(log n) for the SEARCH part (binary search), but the
# actual insertion is still O(n) because the rest of the list must shift.

print(f"{'*' * 60}")

# -------------------------
# 11. List equality vs identity (recap tailored to lists specifically)
# -------------------------
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(l1 == l2)   # True  -> same VALUES
print(l1 is l2)    # False -> different OBJECTS in memory

# nested equality also works recursively:
print([1, [2, 3]] == [1, [2, 3]])   # True -> compares nested structures element by element


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON LISTS
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. What is the time complexity of appending to the END of a list versus
#    inserting/removing at the FRONT of a list? Why the difference?
#
# 2. Why is `[[0] * 3] * 3` a common bug when trying to create a 2D grid/
#    matrix? What's the correct way to create an independent 2D list?
#
# 3. What is the difference between list.sort() and sorted()? Which one
#    returns None, and what mistake does that commonly cause?
#
# 4. How would you reverse a list without using the built-in reverse() method
#    or [::-1] slicing?
#
# 5. What does slice assignment do (e.g., `lst[1:3] = [10, 20, 30]`)? Can it
#    change the overall LENGTH of the list?
#
# 6. Why is `collections.deque` generally preferred over a plain list when
#    implementing a queue (FIFO)? What specific list operation is the
#    bottleneck?
#
# 7. What is the difference between list.remove(x) and list.pop(i)? What
#    happens if the value passed to remove() doesn't exist in the list?
#
# 8. How would you flatten a nested list of lists into a single flat list
#    using a list comprehension?
#
# 9. What does zip() do when given lists of DIFFERENT lengths? Does it raise
#    an error?
#
# 10. What is the difference between a shallow copy and a deep copy of a
#     nested list? Give an example where a shallow copy leads to unintended
#     shared mutation.
#
# 11. What is the bisect module used for? Why would bisect.insort() be more
#     efficient than appending and then re-sorting the whole list?
#
# 12. What's the time complexity of checking `x in my_list` for a list with n
#     elements? How does this compare to checking membership in a set?
#
# 13. How would you remove duplicates from a list while preserving the
#     original order of first occurrence?
#
# 14. What does extended unpacking like `first, *rest = my_list` do? What
#     type is `rest`?
#
# 15. What is the difference between list.append(x) and list.extend(iterable)?
#     What happens if you accidentally use append() when you meant extend()?
#
# 16. Why does `my_list.sort()` return None instead of the sorted list? What
#     design principle does this follow (compare with sorted())?
#
# 17. How would you efficiently find the index of the first element in a
#     SORTED list that is greater than or equal to a target value?
#
# 18. What happens internally when a Python list needs to grow beyond its
#     current allocated capacity (why is append() described as "O(1)
#     amortized" rather than strictly O(1))?
#
# 19. How would you safely remove elements from a list WHILE iterating over
#     it, without skipping elements or causing unexpected behavior?
#
# 20. Given two lists of equal length representing keys and values, how would
#     you combine them into a dictionary in one line?