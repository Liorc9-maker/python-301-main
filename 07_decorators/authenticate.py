def authenticate(func):
    def wrapper(*args, **kwargs):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username == "user" and password == "pass":
            return func(*args, **kwargs)
        else:
            raise Exception("Authentication failed")
    return wrapper

@authenticate
def update_profile(user_id, new_username, new_password):
    # Your code to update the user profile
    print(f"Updating profile for user with id {user_id}")

update_profile(1, "new_user", "new_pass")
