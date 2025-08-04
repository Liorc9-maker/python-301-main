# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.
def quote_wrap(func):
    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        return f'"{results}"'
    return wrapper

@quote_wrap
def greet():
    return "Hello world!"

print(greet())
