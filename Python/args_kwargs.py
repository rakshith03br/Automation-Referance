# ==============================================================================
# *ARGS, **KWARGS & UNPACKING
# ==============================================================================
"""
NOTES:
- *args:- collects extra positional args into a tuple.
- **kwargs:- collects extra keyword args into a dict.

- Order in function def: def f(pos, default=val, *args, kw_only, **kwargs)
- DANGER: mutable default arguments (e.g. def f(x, items=[])) are created ONCE
  when the function is DEFINED, not each call - so they persist/accumulate
  across calls! Fix: use items=None, then `items = items or []` inside.
- Unpacking with * and ** when CALLING a function spreads a list/dict into args.
"""

def log_call(*args, **kwargs):
    print("Positional args:", args)
    print("Keyword args:", kwargs)


def buggy_append(x, items=[]):  # DANGEROUS - shared default!
    items.append(x)
    return items


def fixed_append(x, items=None):  # SAFE
    if items is None:
        items = []
    items.append(x)
    return items


def args_kwargs_demo():
    print("\n--- *ARGS, **KWARGS & UNPACKING ---")

    log_call(1, 2, 3, name="Alice", age=30)
    print(f"{'*' * 80}")

    # Mutable default argument bug
    print("buggy_append(1):", buggy_append(1))
    print("buggy_append(2):", buggy_append(2))  # [1, 2] NOT [2] - the bug!
    print(f"{'*' * 80}")

    print("fixed_append(1):", fixed_append(1))
    print("fixed_append(2):", fixed_append(2))  # correctly just [2]
    print(f"{'*' * 80}")

    # Unpacking when CALLING
    nums = [1, 2, 3]
    print("sum via unpacking:", sum(nums))

    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = {**dict1, **dict2}  # unpack-merge two dicts
    print("Merged dicts:", merged)

    def keyword_only_example(a, *, b):
        """ '*' forces 'b' to be keyword-only - can't call as positional. """
        return a, b
    print("keyword-only call:", keyword_only_example(1, b=2))


if __name__ == "__main__":
    args_kwargs_demo()


# ==============================================================================
# ADDITIONAL NOTES FOR INTERVIEW PREPARATION
# ==============================================================================

# -------------------------
# 1. Full parameter ordering rules in a function definition
# -------------------------
# The ONLY valid order is:
#   def f(positional_only, /, positional_or_keyword, *args, keyword_only, **kwargs):
# Violating this order raises a SyntaxError at definition time.

def full_signature_demo(pos_only, /, normal, *args, kw_only, **kwargs):
    """
    pos_only  -> can ONLY be passed positionally (before the '/')
    normal    -> can be passed positionally OR by keyword
    *args     -> extra positional args, collected as a tuple
    kw_only   -> must be passed by keyword (after *args or bare '*')
    **kwargs  -> extra keyword args, collected as a dict
    """
    return pos_only, normal, args, kw_only, kwargs


print(full_signature_demo(1, 2, 3, 4, kw_only=5, extra="x"))
# (1, 2, (3, 4), 5, {'extra': 'x'})

print(f"{'*' * 80}")

# -------------------------
# 2. Positional-only parameters using '/' (Python 3.8+)
# -------------------------
def divide(a, b, /):
    """Everything before '/' MUST be passed positionally - cannot use a= or b=."""
    return a / b

print(divide(10, 2))     # 5.0
# divide(a=10, b=2)      # TypeError: divide() got some positional-only arguments
                          # passed as keyword arguments

# Why it exists: lets library authors rename parameters later without breaking
# callers (e.g. len(obj) - you can't call len(obj=x)).

print(f"{'*' * 80}")

# -------------------------
# 3. Keyword-only parameters using bare '*' (Python 3+, already partly shown above)
# -------------------------
def create_user(name, *, is_admin=False):
    """Bare '*' with no name - everything after it MUST be passed as keyword."""
    return {"name": name, "is_admin": is_admin}

print(create_user("Bob", is_admin=True))
# create_user("Bob", True)   # TypeError - is_admin can't be positional

# Why it's useful: prevents confusing calls like create_user("Bob", True)
# where the meaning of `True` isn't obvious at the call site.

print(f"{'*' * 80}")

# -------------------------
# 4. Unpacking with * and ** when CALLING (spreading), shown with more depth
# -------------------------
def add3(a, b, c):
    return a + b + c

nums = [1, 2, 3]
print(add3(*nums))          # 6  -> list unpacked into 3 positional args

nums_dict = {"a": 1, "b": 2, "c": 3}
print(add3(**nums_dict))    # 6  -> dict unpacked into keyword args (keys must match param names)

# combining both in one call
def combo(a, b, *args, **kwargs):
    return a, b, args, kwargs

print(combo(*[1, 2, 3, 4], **{"x": 10}))
# (1, 2, (3, 4), {'x': 10})

print(f"{'*' * 80}")

# -------------------------
# 5. Extended iterable unpacking with * in assignments (NOT function-related,
#    but commonly asked alongside *args since it uses the same '*' syntax)
# -------------------------
first, *middle, last = [1, 2, 3, 4, 5]
print(first, middle, last)   # 1 [2, 3, 4] 5

a, *rest = (10, 20, 30)
print(a, rest)                # 10 [20, 30]

*head, tail = "abcd"
print(head, tail)             # ['a', 'b', 'c'] 'd'

print(f"{'*' * 80}")

# -------------------------
# 6. Forwarding *args/**kwargs to another function - VERY common in real code
#    (decorators, subclassing, wrapper functions)
# -------------------------
def wrapper(*args, **kwargs):
    print("Before calling wrapped function")
    result = wrapped(*args, **kwargs)   # forward everything through unchanged
    print("After calling wrapped function")
    return result

def wrapped(x, y, z=0):
    return x + y + z

print(wrapper(1, 2, z=3))    # 6

# Same pattern shows up in class inheritance:
class Base:
    def __init__(self, name, **kwargs):
        self.name = name
        super().__init__(**kwargs)

class Child(Base):
    def __init__(self, name, age, **kwargs):
        super().__init__(name, **kwargs)   # forward remaining kwargs up the chain
        self.age = age

print(f"{'*' * 80}")

# -------------------------
# 7. *args and **kwargs are just conventional NAMES, not keywords
# -------------------------
# The '*' and '**' are what matter; you could name them anything.
def flexible(*values, **options):
    print(values, options)

flexible(1, 2, key="val")   # (1, 2) {'key': 'val'}

print(f"{'*' * 80}")

# -------------------------
# 8. Real-world use case: decorators that work on ANY function signature
# -------------------------
import functools
import time

def timer(func):
    @functools.wraps(func)   # preserves func.__name__, __doc__, etc.
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.6f}s")
        return result
    return inner

@timer
def slow_add(a, b):
    return a + b

print(slow_add(2, 3))
print(slow_add.__name__)   # 'slow_add' -> preserved thanks to functools.wraps

print(f"{'*' * 80}")

# -------------------------
# 9. Other mutable default argument traps (not just lists)
# -------------------------
def buggy_dict_default(key, value, cache={}):   # DANGEROUS - same trap with dict
    cache[key] = value
    return cache

print(buggy_dict_default("a", 1))   # {'a': 1}
print(buggy_dict_default("b", 2))   # {'a': 1, 'b': 2}  -> leaked from previous call!

# Rule of thumb: NEVER use a mutable object (list, dict, set, or a custom mutable
# class instance) as a default argument value.

print(f"{'*' * 80}")

# -------------------------
# 10. TypeErrors you should recognize instantly (common interview trick questions)
# -------------------------
# def f(a, b): pass
# f(1, 2, 3)          # TypeError: f() takes 2 positional arguments but 3 were given
# f(a=1)              # TypeError: f() missing 1 required positional argument: 'b'
# f(1, a=2)           # TypeError: f() got multiple values for argument 'a'

# def g(*, a): pass
# g(1)                 # TypeError: g() takes 0 positional arguments but 1 was given

print(f"{'*' * 80}")

# -------------------------
# 11. Argument count/order sanity check with **kwargs and duplicate keys
# -------------------------
def show(**kwargs):
    print(kwargs)

d1 = {"a": 1}
d2 = {"a": 2}          # duplicate key 'a'
merged = {**d1, **d2}  # later dict's value WINS on key collision
print(merged)           # {'a': 2}
# show(**d1, **d2)      # works fine for merging, but show(a=1, **{"a": 2})
                         # would raise: TypeError: got multiple values for keyword argument 'a'

print(f"{'*' * 80}")

# -------------------------
# 12. Empty *args / **kwargs still work fine (no error if nothing extra is passed)
# -------------------------
log_call()   # Positional args: ()   Keyword args: {}


# ==============================================================================
# INTERVIEW QUESTIONS ON *ARGS, **KWARGS & UNPACKING
# (For a candidate with ~4 years of experience. Answers intentionally omitted for practice.)
# ==============================================================================

# 1. What is the difference between *args and **kwargs? What data structures do they
#    collect their values into?
#
# 2. What is the correct order of parameters in a function definition when mixing
#    positional, default, *args, keyword-only, and **kwargs? What happens if you
#    get the order wrong?
#
# 3. Why is using a mutable object (like a list or dict) as a default argument value
#    considered dangerous? Walk through exactly when the default value gets created.
#
# 4. What is the fix for the mutable default argument problem, and why does that
#    fix work (i.e., why is `None` safe as a default)?
#
# 5. What do positional-only parameters (using '/') mean, and why would an API
#    designer want to use them?
#
# 6. What does a bare '*' (with no name) do in a function signature? How is it
#    different from *args?
#
# 7. How would you forward all arguments received by a wrapper function to another
#    function unchanged? Why is this pattern common in decorators?
#
# 8. What does functools.wraps do, and why is it important when writing decorators
#    that use *args, **kwargs?
#
# 9. If you unpack two dictionaries with overlapping keys into a single dict literal
#    (e.g., {**d1, **d2}), which value wins for a duplicate key?
#
# 10. What error do you get if you pass a keyword argument that collides with a
#     positional argument already provided (e.g., f(1, a=2) where 'a' is the first
#     parameter)?
#
# 11. Can you unpack a generator or other iterable (not just a list) using *? What
#     about unpacking a non-dict mapping using **?
#
# 12. What is extended iterable unpacking (e.g., `first, *rest = some_list`)? How
#     is this related to, or different from, *args in function definitions?
#
# 13. Is it mandatory to name your variadic parameters "args" and "kwargs"? What
#     actually makes them behave this way syntactically?
#
# 14. How would you write a function that accepts any number of positional
#     arguments but requires at least one? (Hint: think about signature design,
#     e.g. def f(first, *rest).)
#
# 15. What happens if you call a function with more positional arguments than it
#     defines and it has no *args to catch them?
#
# 16. In class inheritance, why do we often see `super().__init__(*args, **kwargs)`
#     in a subclass's __init__? What problem does this solve?
#
# 17. Can *args and **kwargs be empty when a function is called with no extra
#     arguments? What values do they hold in that case?
#
# 18. How would you dynamically call a function with arguments stored in a list
#     and a dict that were built at runtime (not known when writing the code)?
#
# 19. What's the difference between *args in a function DEFINITION versus * used
#     when CALLING a function? (i.e., "collecting" vs "unpacking")
#
# 20. Why might overusing **kwargs in a public API's function signatures be
#     considered bad practice from a readability/maintainability standpoint?