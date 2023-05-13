from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)
# f变量是一个文件因此可以进行 f.seek(0), f.readline()
# seek()函数的处理对象是字节而非行，所以seek（0）只是转到文件的0字节
# f.readline()读取文件的一行
def print_a_line(line_count, f):
    print(line_count, f.readline(), end="")
# print在打印时会增加一个\n，加入参数end=“”，这样print就不会为每一行多打印/n出来了
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line +1
print_a_line(current_line, current_file)
