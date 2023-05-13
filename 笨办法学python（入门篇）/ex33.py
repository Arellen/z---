# 将小于6的数字添加到一个空的数组中，并返回添加后的数组。
i = 0
numbers = []

while i < 6:
    print(f"The initial number is {i}")
    numbers.append(i)
    i += 1
    print(f"the number is now {i}")
    print(f"The numbers is {numbers}")

    for num in numbers:
        print(num)

# 制作一个函数，给一个数字，制作一个从0到这个数字的数组
# from sys import argv
#
# script, num = argv
# 如果改成input（）形式，隐藏27行；显示16-18行；python输入框中输入 script, num两个参数

def create_array(yyds):
    arr = []
    for number in range(0, int(yyds)):
        arr.append(number)
    return arr

num = input("> ")
print(create_array(num))

