# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************

def decorate(symbol):
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = func(*args, **kwargs)
            line_length = len(results) + 4 
            decoration = symbol * line_length
            return f"{decoration}\n{symbol} {results} {symbol}\n{decoration}"
        return wrapper
    return decorator

@decorate("*")
def say_hello():
    return "Hello"

print(say_hello())