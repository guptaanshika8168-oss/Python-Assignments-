from functools import wraps

def validate_positive_integers(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        values = list(args) + list(kwargs.values())
        if all(isinstance(x, int) and x > 0 for x in values):
            return func(*args, **kwargs)
        else:
            print("Error: All arguments must be positive integers.")
    return wrapper

def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"{func.__name__} has been called {wrapper.calls} time(s).")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
@validate_positive_integers
def add_numbers(a, b):
    print("Sum:", a + b)

add_numbers(3, 5)
add_numbers(2, 8)
add_numbers(4, -1)