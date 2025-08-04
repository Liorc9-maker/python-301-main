# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.
from datetime import datetime
from zoneinfo import ZoneInfo

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        result = func(*args, **kwargs)
        end_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        execusion_time = end_time - start_time
        print(f"{func.__name__} executed in {execusion_time.total_seconds():.6f} seconds")
        return result
    return wrapper

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

@time_it
@censor("shoot", "crab")
def complain():
    return "I bumped my toe! shoot! And I saw a crab!"

print(complain())