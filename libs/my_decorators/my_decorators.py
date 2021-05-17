import datetime


def speed_test(func):
    def wrapper(self, d):
        start_time = datetime.datetime.now()
        result = func(self, d)
        print(f"{func.__name__}. Execution time = {datetime.datetime.now() - start_time}")
        return result
    return wrapper
