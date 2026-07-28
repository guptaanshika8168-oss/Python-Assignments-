def login_required(func):
    def wrapper(*args, **kwargs):
        if is_logged_in:
            return func(*args, **kwargs)
        else:
            print("Access denied. Please log in first.")
    return wrapper


is_logged_in = False

@login_required
def protected_function():
    print("Welcome to the protected function!")


# Try accessing without login
protected_function()

# Simulate login
is_logged_in = True

# Try accessing after login
protected_function()