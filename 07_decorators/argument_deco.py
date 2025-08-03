def decorator_func(initial_func):
    def wrapper_func(msg):
        print("wrapper function picked some...")
        return initial_func(msg)
    return wrapper_func

@decorator_func
def prettify(msg):
    print(msg)

prettify("flowers for you")
