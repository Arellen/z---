from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C)")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file……")
target = open(filename,'w')
# 'w'是write, 'r' is read, 'a' is append.
# if you just write the code like 'open(filename)' without any of them,
# it will be opened with 'r' as the default

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(f"{line1} \n {line3} \r {line2} \t I know you.")


print("And finally, we close it.")
target.close()

print(open(filename).read())
