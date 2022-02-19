# Function decorator

def fun_decorator(function):
    def wrapper_function():
        print("example")
        function()

    return wrapper_function


@fun_decorator
def hello_fun():
    print("Hello")


hello_fun()
