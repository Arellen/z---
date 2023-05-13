the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'bananas']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list.
for number in the_count:
    print("This is the count:", number)

# same as above
for fruit in fruits:
    print("A fruit of type:", fruit)

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding", i, "to the list.")
    # append is a function that lists understand.
    elements.append(i)
# range()函数会从第一个数到最后一个数，但不包含最后一个数，所以range(0, 6),显示的数字是0，1，2，3，4，5
# .append()也会向列表中添加一个元素，但这只是一个命名的函数，不会对列表进行扩展或排序。

# now we can print them out too

for i in elements:
    print("Element was:", i)
