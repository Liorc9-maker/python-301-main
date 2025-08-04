# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def censor(*offensive_words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in offensive_words:
                if len(word) > 1:
                    censored = word[0] + '*' * (len(word) - 1)
                else:
                    censored = word
                result = result.replace(word, censored)
            return result
        return wrapper
    return decorator

@censor("shoot", "crab")
def complain():
    return "I bumped my toe! shoot! And I saw a crab!"

print(complain())  # Output: I bumped my toe! s****! And I saw a c***
