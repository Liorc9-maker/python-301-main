from datetime import datetime
from zoneinfo import ZoneInfo  # Python 3.9+

def log_it(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        tz = ZoneInfo("Asia/Kolkata")  # Change to your desired timezone
        with open("activity.log", "a") as f:
            f.write(f"{func.__name__} was called at {datetime.now(tz)}\n")    
        return result
    return wrapper



@log_it
def send_email(to, subject, message):
    pass # Your code to send an email

send_email("user@example.com", "Hello", "How are you?")
