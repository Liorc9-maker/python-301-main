def add_message_from(name):
    def decorator_func(initial_func):
        def wrapper_func(*args):
            print(f"{name} picked some")
            return initial_func(*args)
        return wrapper_func
    return decorator_func


@add_message_from("Zeek")
def prettify(msg):
    print(msg)

prettify("flowers for you")  # Zeek picked some flowers for you


@add_message_from("Alice")
def prettify(msg):
    print(msg)

prettify("roses for you")    