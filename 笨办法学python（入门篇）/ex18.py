# this one is likeyour scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")
# def means define
# *args presents more than one
def print_three(*args):
    arg1, arg2, arg3 = args
    print(f"arg1: {arg1}, arg2: {arg2}, arg3:{arg3}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothing.")


print(print_two("zed", "shaw"))
print(print_two_again("zed", "shaw"))
print(print_one("First"))
print(print_none())
print(print_three(1, 1.0, 2.2))