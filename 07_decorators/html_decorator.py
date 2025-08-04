# Write a decorator function that wraps text passed to it in a specified HTML tag. 
# The user should be able to decide which tag to use.

def html_decorator(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            content = func(*args, **kwargs)
            return f"<{tag}>{content}</{tag}>"
        return wrapper
    return decorator

@html_decorator("h1")
def greet(name):
    return f"Hello, {name}!"

print(greet("Dana"))