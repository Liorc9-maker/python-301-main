def say_hi():
    print("Hi there!")

def say_bye():
    print("Bye bye!")

def say_hello():
    print("Hello!")

def say_goodbye():
    print("Goodbye!")

funcy_list = [
    say_hi,
    say_bye,
    say_hello,
    say_goodbye
]

for func in funcy_list:
    func()  # Call each function in the list     
