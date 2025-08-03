def outer_func():
    msg = "Weeeeeekend!"
    def inner_func():
        print(msg)
    return inner_func


outer_func()
say_wee = outer_func()
say_wee()

def outer_func2(msg):
    def inner_func():
        print(msg)
    return inner_func

say_hi = outer_func2("Hi")
say_hi()