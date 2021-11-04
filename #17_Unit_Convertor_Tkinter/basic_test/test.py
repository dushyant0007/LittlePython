result = 0


def add(*nums):
    print(nums[2])
    result = 0
    print(type(nums))
    for a in nums:
        result += a
    return result


print(add(1, 2, 3, 4, 5))

print("============_____________================__________===============")


def calculate(n, **kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    print(f"value of key add input is : ")
    print(kwargs["add"])
    n += kwargs["add"]
    print(f"ans of add = {n}")
    n *= kwargs["multiply"]
    print(f"ans of multiply = {n}")


calculate(2, add=4, multiply=5)


class Car:
    def __init__(self, **kw):
        # self.make = kw["make"] # this will give error of we don's pass any argument in call
        self.make = kw.get("make") # But this will return empty is not passed // so there is no error
        self.model = kw.get("modeal")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
