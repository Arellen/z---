people = 30
cars = 10
trucks = 15


if cars >people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That'll be a lot of trucks.")
elif trucks <  cars:
    print("Maybe you should take the trucks.")
else:
    print("Sure.")

if people > trucks:
    print("Let's not take the trucks.")
else:
    print("You're right, let's take the trucks.")