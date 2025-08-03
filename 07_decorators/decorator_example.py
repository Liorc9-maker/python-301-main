def lowercase(func):
    """A decorator that avoids digital screaming."""
    def wrapper(text):
        initial_result = func(text)
        new_result = initial_result.lower()
        return new_result
    return wrapper

@lowercase
def say_something(text):
    return text

print(say_something("HEY WHAT'S UP?"))  # OUTPUT: hey what's up?


@lowercase
def respond(text):
    return text

print(respond("I AM FINE, THANK YOU!"))  # OUTPUT: i am fine, thank you!





def decorator_func(initial_func):
    def wrapper_func():
        print("the wrapper function picked some...")
        return initial_func()
    return wrapper_func


@decorator_func
def prettify():
    print("flowers for you")

prettify()
