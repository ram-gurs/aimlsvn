from functools import singledispatchmethod

class Formatter:
    @singledispatchmethod
    def format(self, value):
        return str(value)

    @format.register
    def _(self, value: int):
        return f"INT:{value:,}"

    @format.register
    def _(self, value: dict):
        return f"KEYS:{', '.join(value.keys())}"


fmt = Formatter()
print(fmt.format(1000000))            # Output: INT:1,000,000
print(fmt.format({"a": 1, "b": 2}))   # Output: KEYS:a, b
print(fmt.format(3.14))               # Output: 3.14 (uses fallback)
from multipledispatch import dispatch


# ==========================================
# 1. Standalone Function Overloading
# ==========================================

@dispatch(int, int)
def add(x, y):
    print("Called add(int, int)")
    return x + y

@dispatch(str, str)
def add(x, y):
    print("Called add(str, str)")
    return f"{x} {y}"

@dispatch(list, list)
def add(x, y):
    print("Called add(list, list)")
    return x + y

@dispatch(object, object)
def add(x, y):
    """Fallback handler for any two objects."""
    print("Called add(object, object) [Fallback]")
    return f"{x} & {y}"


# ==========================================
# 2. Class Method Overloading
# ==========================================

class Calculator:
    @dispatch(int, int)
    def compute(self, a, b):
        return f"Multiplying ints: {a * b}"

    @dispatch(float, float)
    def compute(self, a, b):
        return f"Dividing floats: {a / b:.2f}"

    @dispatch(str, int)
    def compute(self, text, count):
        return f"Repeating string: {text * count}"


# ==========================================
# Execution & Verification
# ==========================================

if __name__ == "__main__":
    print("--- Function Overloading ---")
    print(add(10, 20))           # Matches (int, int)
    print(add("Hello", "World"))  # Matches (str, str)
    print(add([1, 2], [3, 4]))   # Matches (list, list)
    print(add(3.14, True))       # Matches (object, object)

    print("\n--- Class Method Overloading ---")
    calc = Calculator()
    print(calc.compute(4, 5))         # Matches (int, int)
    print(calc.compute(10.0, 4.0))    # Matches (float, float)
    print(calc.compute("Py", 3))      # Matches (str, int)