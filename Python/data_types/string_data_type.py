"""
str (String) in Python:- str()

String: String is set of characters that are together and enclosed with single,double and triple quotes.
A string is a sequence of characters used to represent text. It's one of the most commonly used data types in Python.
    Immutable — once created, a string cannot be changed in place
    Ordered — characters have a fixed position (indexed)
    Iterable — you can loop through characters one by one
"""

# Creating strings
s1 = 'Hello'
s2 = "World"
s3 = '''This is a
multi-line string'''
s4 = """This also works
for multiple lines"""
# Single quotes, double quotes — both work the same way. Triple quotes (''' or """) let you span multiple lines.

# Indexing and slicing
# Strings are ordered, so each character has a position (index), starting at 0.
# s[start:stop:step]
s = "Python"
print(s[0])     # 'P'
print(s[-1])    # 'n'  (negative index counts from the end)
print(s[1:4])   # 'yth'  (slicing: start included, end excluded)
print(s[::-1])  # 'nohtyP'  (reverses the string)
print(s[0::2])


# Strings are immutable
# You cannot change a character in place:
# s = "Hello"
# s[0] = "J"   # ❌ TypeError — strings don't support item assignment
# # Instead, you create a new string:
# s = "Hello"
# s = "J" + s[1:]
# print(s)  # "Jello"

# Common string methods
s = "  Hello World  "

s.strip()        # "Hello World"        — removes leading/trailing spaces
s.lower()        # "  hello world  "    — lowercase
s.upper()        # "  HELLO WORLD  "    — uppercase
s.replace("Hello", "Hi")  # "  Hi World  "
s.split()        # ['Hello', 'World']   — splits into a list
s.find("World")  # index where "World" starts # 8
len(s)           # length of the string # 15

# Concatenation and repetition
a = "Hello"
b = "World"
print(a + " " + b)  # "Hello World"  — concatenation
print(a * 3)          # "HelloHelloHello"  — repetition

# String formatting
name = "Alice"
age = 25
# f-strings (recommended, Python 3.6+)
print(f"My name is {name} and I am {age} years old.")

# .format()
print("My name is {} and I am {} years old.".format(name, age))

# % operator (older style)
print("My name is %s and I am %d years old." % (name, age))

# Checking string content
"123".isdigit()     # True
"abc".isalpha()     # True
"abc123".isalnum()  # True
" ".isspace()       # True

# Iterating through a string
for ch in "Python":
    print(ch)

# Membership check
s = "Hello World"
print("World" in s)   # True
print("Bye" in s)     # False


# Joining strings
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)  # "Python is fun"

## escape character(/)
print('Hello\'world')


## concatination of str and int
a = "Hi "
b = 100
print(a + str(b))

"""
 Quick summary
Feature	                String
--------                ----------------------------------------
Ordered?	            ✅ Yes
Indexed?	            ✅ Yes
Mutable?	            ❌ No (immutable)
Duplicates allowed?	    ✅ Yes (characters can repeat)
Common use	            Text storage, manipulation, formatting
"""

## ==========================================================
## ADDITIONAL NOTES FOR INTERVIEW PREPARATION (4 YOE LEVEL)
## ==========================================================

# -------------------------
# 1. find() vs index() vs count()  (common confusion point)
# -------------------------
s = "Hello World"
print(s.find("Bye"))     # -1  -> returns -1 if not found, never raises
# print(s.index("Bye"))  # ValueError: substring not found -> raises exception
print(s.index("World"))  # 6   -> works like find() but raises on failure
print(s.count("o"))      # 2   -> counts non-overlapping occurrences

print(f"{'*' * 50}")

# -------------------------
# 2. startswith() / endswith() (better than slicing for prefix/suffix checks)
# -------------------------
filename = "report.pdf"
print(filename.startswith("report"))   # True
print(filename.endswith(".pdf"))       # True
print(filename.endswith((".pdf", ".doc")))  # True -> accepts a tuple of options

print(f"{'*' * 50}")

# -------------------------
# 3. split() vs rsplit() vs splitlines() vs partition()
# -------------------------
path = "a,b,c,d"
print(path.split(","))         # ['a', 'b', 'c', 'd']
print(path.split(",", 1))      # ['a', 'b,c,d']  -> maxsplit limits number of splits
print(path.rsplit(",", 1))     # ['a,b,c', 'd']  -> splits from the right

text = "line1\nline2\nline3"
print(text.splitlines())       # ['line1', 'line2', 'line3'] -> splits on line boundaries, no trailing empty string

# partition() splits into exactly 3 parts: (before, separator, after)
print("key=value".partition("="))   # ('key', '=', 'value')
print("no-sep-here".partition("="))  # ('no-sep-here', '', '') -> sep not found

print(f"{'*' * 50}")

# -------------------------
# 4. Padding and alignment methods (useful for formatted output, tables, reports)
# -------------------------
print("42".zfill(5))       # '00042'   -> zero-pads on the left, handles sign correctly e.g. "-42".zfill(5) -> '-0042'
print("hi".ljust(10, "-")) # 'hi--------'
print("hi".rjust(10, "-")) # '--------hi'
print("hi".center(10, "-"))# '----hi----'

print(f"{'*' * 50}")

# -------------------------
# 5. strip() variants
# -------------------------
s = "xxHelloxx"
print(s.strip("x"))    # 'Hello'      -> strips given characters from both ends
print(s.lstrip("x"))   # 'Helloxx'    -> strips from the left only
print(s.rstrip("x"))   # 'xxHello'    -> strips from the right only

print(f"{'*' * 50}")

# -------------------------
# 6. Advanced f-string features (Python 3.8+)
# -------------------------
value = 3.14159
name = "Bob"
print(f"{value:.2f}")        # '3.14'     -> format specifier: 2 decimal places
print(f"{value:>10.2f}")     # '      3.14' -> right-align in a width-10 field
print(f"{name=}")            # "name='Bob'" -> self-documenting expressions (3.8+), great for debugging
number = 1000000
print(f"{number:,}")         # '1,000,000' -> thousands separator

print(f"{'*' * 50}")

# -------------------------
# 7. Raw strings (r-strings) — important for regex and file paths
# -------------------------
path = r"C:\Users\name\Documents"   # backslashes are NOT treated as escape characters
print(path)                          # C:\Users\name\Documents
normal = "C:\\Users\\name\\Documents"  # without raw string, need to escape each backslash
print(normal)

print(f"{'*' * 50}")

# -------------------------
# 8. String <-> character code conversions
# -------------------------
print(ord('A'))    # 65  -> character to its Unicode code point
print(chr(65))     # 'A' -> code point to character
print(ord('a'))    # 97

print(f"{'*' * 50}")

# -------------------------
# 9. Encoding / decoding (str vs bytes) — common interview topic
# -------------------------
s = "café"
encoded = s.encode("utf-8")       # str -> bytes
print(encoded)                     # b'caf\xc3\xa9'
decoded = encoded.decode("utf-8")  # bytes -> str
print(decoded)                     # 'café'
print(type(encoded))               # <class 'bytes'>

# NOTE: In Python 3, str is Unicode by default (unlike Python 2 where str was bytes).

print(f"{'*' * 50}")

# -------------------------
# 10. String immutability & efficient concatenation (performance gotcha)
# -------------------------
# BAD (in a loop): creates a new string object on every iteration -> O(n^2) time
result = ""
for word in ["Python", "is", "fun"]:
    result += word + " "

# GOOD: build a list and join once at the end -> O(n) time
parts = []
for word in ["Python", "is", "fun"]:
    parts.append(word)
result = " ".join(parts)
print(result)

print(f"{'*' * 50}")

# -------------------------
# 11. String interning (identity vs equality — similar to int caching)
# -------------------------
a = "hello"
b = "hello"
print(a is b)      # True -> CPython interns short, identifier-like string literals

c = "hello world!"
d = "hello world!"
print(c is d)      # may be False -> strings with spaces/special chars aren't always interned
print(c == d)       # True -> always use == to compare string VALUES, not 'is'

import sys
e = sys.intern("hello world!")
f = sys.intern("hello world!")
print(e is f)       # True -> sys.intern() forces interning manually

print(f"{'*' * 50}")

# -------------------------
# 12. String comparison rules (lexicographic, based on Unicode code points)
# -------------------------
print("apple" < "banana")   # True  -> compared character by character
print("Apple" < "apple")    # True  -> uppercase letters have smaller code points than lowercase
print("10" < "9")           # True  -> STRING comparison, not numeric! ("1" < "9")

print(f"{'*' * 50}")

# -------------------------
# 13. translate() and maketrans() — bulk character replacement (faster than chained replace())
# -------------------------
table = str.maketrans("abc", "xyz")
print("aabbcc".translate(table))   # 'xxyyzz'

# removing characters using translate
remove_table = str.maketrans("", "", "aeiou")
print("hello world".translate(remove_table))  # 'hll wrld'

print(f"{'*' * 50}")

# -------------------------
# 14. Checking content: additional is* methods
# -------------------------
print("Hello World".istitle())   # True  -> each word starts with uppercase
print("HELLO".isupper())          # True
print("hello".islower())          # True
print("123".isnumeric())          # True
print("  ".isspace())             # True
print("".isalpha())               # False -> empty string returns False for all is* checks

print(f"{'*' * 50}")

# -------------------------
# 15. String multiplication and repetition edge cases
# -------------------------
print("ab" * 0)     # ''  -> empty string
print("ab" * -1)    # ''  -> negative repeat also gives empty string (no error)

print(f"{'*' * 50}")

# -------------------------
# 16. Common interview coding patterns using strings
# -------------------------
def is_palindrome(text: str) -> bool:
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_palindrome("Nurses Run"))   # True

def is_anagram(s1: str, s2: str) -> bool:
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("listen", "silent"))  # True

def reverse_words(sentence: str) -> str:
    return " ".join(sentence.split()[::-1])

print(reverse_words("Python is fun"))   # "fun is Python"

def count_vowels(text: str) -> int:
    return sum(1 for ch in text.lower() if ch in "aeiou")

print(count_vowels("Hello World"))   # 3

print(f"{'*' * 50}")

# -------------------------
# 17. String module (predefined character sets — handy for validation/generation tasks)
# -------------------------
import string
print(string.ascii_lowercase)   # 'abcdefghijklmnopqrstuvwxyz'
print(string.ascii_uppercase)   # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(string.digits)            # '0123456789'
print(string.punctuation)       # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'


## ==========================================================
## INTERVIEW QUESTIONS ON PYTHON STRING DATA TYPE
## (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
## ==========================================================

# 1. Why are strings immutable in Python? What are the benefits and drawbacks of this design?
#
# 2. What happens internally when you do `s += "text"` in a loop? Why is this considered
#    inefficient, and what's the better alternative?
#
# 3. What is string interning in CPython? Why does `"hello" is "hello"` return True but
#    `"hello world!" is "hello world!"` may return False?
#
# 4. What is the difference between find(), index(), and count()? What happens when the
#    substring is not found in each case?
#
# 5. Explain the difference between split(), rsplit(), and partition(). When would you
#    use partition() over split()?
#
# 6. How would you reverse a string in Python? Can you do it without using slicing?
#
# 7. How do you check if two strings are anagrams of each other? What's the time
#    complexity of your approach?
#
# 8. What's the difference between str and bytes in Python 3? When would you need to
#    encode/decode between them?
#
# 9. What is a raw string (r"...")? Give a real-world scenario where you'd need one.
#
# 10. Explain Python's f-string formatting. How would you format a float to 2 decimal
#     places, or add thousands separators to a large number?
#
# 11. Why does `"10" < "9"` evaluate to True? Explain how string comparison works
#     under the hood.
#
# 12. What is the time complexity of string concatenation (+) vs "".join() when combining
#     many strings? Why does the difference exist given strings are immutable?
#
# 13. How would you check if a string is a palindrome? How would you handle
#     case-sensitivity and spaces?
#
# 14. What does str.translate() do, and how is it different/faster than chaining
#     multiple replace() calls?
#
# 15. What's the difference between isdigit(), isnumeric(), and isdecimal()? Give an
#     example where they differ (hint: think Unicode fraction characters or superscripts).
#
# 16. How is Unicode handled in Python 3 strings compared to Python 2? What was the
#     "str vs unicode" split in Python 2 about?
#
# 17. Given a string, how would you count the frequency of each character efficiently?
#     What data structure would you use?
#
# 18. What does the `maxsplit` parameter do in split()? Give an example use case.
#
# 19. How would you remove all occurrences of specific characters from a string
#     efficiently (e.g., removing all vowels)?
#
# 20. What's the difference between `%` formatting, `.format()`, and f-strings?
#     Which is preferred in modern Python and why?
#
# 21. Can you slice a string with a step value? How would you get every 2nd character,
#     or reverse a string using slicing?
#
# 22. What happens when you try to do `s[0] = 'X'` on a string? Why does this fail, and
#     how would you achieve the same effect (replacing one character)?
#
# 23. How would you check if a string contains only whitespace, or is empty vs
#     contains only whitespace? What methods distinguish these cases?
#
# 24. What's the difference between shallow copying and just reassigning a string
#     variable, given strings are immutable? Does copy.copy() even make sense for strings?