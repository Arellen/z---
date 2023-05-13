print("How old are you?", end= '')
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weight?", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

name = input("请输入您的名字：")
print("您好，" + name + "!")
# "您好，" + name + "!" ==  f"您好，{name}!"
name = input("请输入您的名字：")
print(f"您好，{name}!")