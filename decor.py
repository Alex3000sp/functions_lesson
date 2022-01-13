#Decorator

def inspect(decorator):
    def wrapper(*args, **kwargs):
        print(f'Args: {args}\n',
              f'Kwargs: {kwargs}\n',
              f'Result: {" ".join(args) if not reversed else " ".join(args[::-1]) }\n')
    return wrapper