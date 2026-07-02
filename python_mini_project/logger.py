def logger(func):  # create one wrapper function
    def wrapper(*args, **kwargs):
        print(f"INFO : calling {func.__name__}")  # This will print the
        return func(*args, **kwargs)
    return wrapper
