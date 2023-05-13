from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv
# argv 参数变量 argument variable, 3行将argv 解包 unpack
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)