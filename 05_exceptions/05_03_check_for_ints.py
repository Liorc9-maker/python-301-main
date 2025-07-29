# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.
while True:
    try:
        user_input = input("Please enter an integer: ")
        int_user_input = int(user_input)
        print(f"You have entered a valid integer: {int_user_input}")
        break
    except ValueError:
        print("Thats not a valid integer. Please try again.")
     