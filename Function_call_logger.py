from datetime import datetime
from functools import wraps

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' called at {datetime.now()}")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet():
    print("Hello, world!")

greet()