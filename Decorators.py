# Execution Decorator
def execution_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)   # run the original function
        print("After execution")
        return result
    return wrapper

@execution_decorator
def greet(name):
    print(f"Hello, {name}!")

greet("Mayank")

# Retry Decorator
import time
def retry_on_failure(max_retries, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Error: {e} Retrying...")
                    time.sleep(delay)
            raise Exception("Maximum retries exceeded.")
        return wrapper
    return decorator

@retry_on_failure(max_retries=3, delay=2)
def unstable_func():
    raise ValueError("Random failure")
unstable_func()

# Access Control Decorator
def requires_admin(func):
    def wrapper(user, *args, **kwargs):
        if user.get("role") != "admin":
            print("Access denied.")
            return None
        return func(user, *args, **kwargs)
    return wrapper

@requires_admin
def admin_panel(user):
    print("Welcome, admin!")
admin_user = {"username": "alice", "role": "admin"}
regular_user = {"username": "bob", "role": "user"}
admin_panel(admin_user)  # Should allow access
admin_panel(regular_user)  # Should deny access

# Caching/Memoization Decorator
def cache_result(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print("Retrieving result from cache.")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@cache_result
def multiply(x, y):
    print("Calculating...")
    return x * y
print(multiply(3, 4))  # first call → computes
print(multiply(3, 4))  # second call → retrieves from cache

# Logging Decorator
def add_logging(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@add_logging
def add(x, y):
    return x + y
add(5, 7)

# Rate Limiting Decorator
import time
def rate_limits(max_calls, period):
    def decorator(func):
        calls = 0
        last_reset = time.time()
        def wrapper(*args, **kwargs):
            nonlocal calls, last_reset
            if time.time() - last_reset > period:
                calls = 0
                last_reset = time.time()
            if calls >= max_calls:
                raise Exception("Rate limit exceeded.")
            calls += 1
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limits(max_calls=6, period=10)
def api_call():
    print("API call executed.")
for i in range(8):
    try:
        api_call()
    except Exception as e:
        print(e)