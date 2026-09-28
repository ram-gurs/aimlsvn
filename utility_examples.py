print("Hello, World!")
from functools import cache, singledispatchmethod

# Memoizes function results so that repeated calls with the same arguments return cached outputs instead of recomputing. @cache is a simpler, unbounded shortcut for @lru_cache(maxsize=None).

# functools-- WRAPPER FUNC AND decorators to make functions easier and faster to use AND USES ANNOTATIONS.

from functools import partial
import functools

# Creates a new function with some of the original function's arguments pre-filled or "frozen."

def multiply(a,b):
    return a * b

double = partial(multiply, 2)
double(5)
# returns 10


from functools import wraps

# A decorator helper used when writing custom decorators. It copies metadata (such as __name__, __doc__, and type annotations) from the original function to the wrapper function.
def a_decorator(asyncfunc):
    @wraps(asyncfunc)
    def my_wrapper(*args, **kwargs):
        return asyncfunc(*args, **kwargs)
    return my_wrapper


from functools import reduce
# Applies a two-argument function cumulatively to the items of a sequence to reduce it to a single value.

total = reduce(lambda x, y: x + y, [0, 0, 3, 4])  # Output: 7


    # singledispatchmethod IS A  type‑based method IT AUTO CONVERTS TO TYPE USES ANNOTATIONS

    # functools.singledispatch turns a standard function into a generic function, enabling method overloading based on the type of the first argument.

from functools import singledispatch

@singledispatch
def process(data):
    """Fallback implementation for unsupported types."""
    raise TypeError(f"Unsupported type: {type(data).__name__}")

@process.register
def _(data: int):
    print(f"Processing integer: {data * 2}")

@process.register
def _(data: str):
    print(f"Processing string: {data.upper()}")

@process.register
def _(data: list):
    print(f"Processing list of length {len(data)}: {data}")


# Usage
process(10)          # Output: Processing integer: 20
process("hello")     # Output: Processing string: HELLO
process([1, 2, 3])   # Output: Processing list of length 3: [1, 2, 3]

# Triggers the fallback:
# process(3.14)      # Raises TypeError: Unsupported type: float

# When an exception is raised while the generator is paused at a yield, Python injects that exception into the generator at the suspension point, causing the generator to either handle it or stop with that exception.[ remember send val --. trow excptn---> close the task]


# What is the primary purpose of the inspect.signature object and its bind / apply_defaults methods?PLS Layman summary

# Crisp breakdown
# inspect.signature → captures the function’s parameter structure (names, defaults, kinds).

# bind → takes real arguments and maps them to those parameters exactly as Python’s call machinery would.

# apply_defaults → fills in any parameters that weren’t provided with their default values.