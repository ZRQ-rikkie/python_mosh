successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful!")
        break  # break get out of for loop

successful = input("?:")
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful!")
        break  # break get out of for loop
else:
    print("Attempted three times and failed!")

for x in range(5):
    for y in range(3):
        print(f"({x},{y})")

for x in range(5):
    print(x)
print(type(5))
print(type(range(5)))

# range type is iterable
# and so does string!!
# eg:
for x in "Python":
    print(x)

# List:
for x in [1, 3, 5, 9]:
    print(x)


# how to use while loop:
number = 100
while number > 0:
    print(number)
    number //= 2

# how to build a shell:
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
