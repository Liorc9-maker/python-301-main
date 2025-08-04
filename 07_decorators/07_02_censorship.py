# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"


def censor(func):
    offensive_words = ["shoot"]

    def wrapper(*args, **kwargs):
        results = func(*args, **kwargs)
        for word in offensive_words:
            result = results.replace(word[1:], '*' * len(word))

        return result
    
    return wrapper

@censor
def complain():
    return "I bumbed my toe! shoot!"

print(complain())