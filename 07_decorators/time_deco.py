import time
from functools import wraps

def decorator_func(initial_func):
    @wraps(initial_func)
    def wrapper_func():
        print("wrapper function picked some...")
        return initial_func()
    return wrapper_func

def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {end - start:.4f} seconds to execute.")
        return result
    return wrapper


@decorator_func
@time_it
def prettify():
    print("flowers for you")

@decorator_func
@time_it
def feed():
    print("apples and potatoes")

prettify()
feed()