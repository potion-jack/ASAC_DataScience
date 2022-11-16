def introduce(name):
    print(f"My name is {name}!")

def decorator(func):
    def wrapper(*args,**kwargs):
        print("Hello")
        return func(*args,**kwargs)
    return wrapper

decorated_introduce = decorator(introduce)
decorated_introduce("Chaewon")

@decorator
def introduce(name):
    print(f'my name is {name}')

introduce('Chaewon')

