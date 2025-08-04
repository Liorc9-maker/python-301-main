from time import sleep

class RateLimitError(Exception):
    """Rate limit exceeded."""

def rate_limit(max_requests):
    def decorator(func):
        request_count = 0

        def wrapper(*args, **kwargs):
            nonlocal request_count
            if request_count >= max_requests:
                raise RateLimitError(func.__name__)
            else:
                request_count += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


@rate_limit(4)
def get_user_data():
    # Your API code to get user data from a page
    print(f"Got user data")


@rate_limit(3)
def scrape_comment_page(url):
    # Your web scraping code to scrape comments from a page
    print(f"Scraped comments from {url}")

for _ in range(6):
    try:
        get_user_data()
        scrape_comment_page("www.example.com")
    except RateLimitError as re:
        print(f"(x) {re.__doc__} (function: {re})")

