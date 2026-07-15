def say_hello(name):
    return(f"Hello, {name}!")


def total(* numbers):
    return sum(numbers)
print(total(1, 2, 3, 4, 5))

def user_profile(**kwargs):
    print(kwargs)

user_profile(name="John", age=30, city="New York")
user_profile(name="Alice", age=25, city="Los Angeles", occupation="Engineer")
user_profile(name="Bob", age=40, city="Chicago", occupation="Manager", hobby="Photography")

# name = input ("Enter your name:")
# print(say_hello(name))