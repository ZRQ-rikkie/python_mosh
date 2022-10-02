always use lowercase to name your fuction
always keep your function name meaningful


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("welcome aboard")


greet("Rae", "Z")
greet("Hammer", "Z")


def greet(name):
    print(f"Hi {name}")
# There are two types of function:
# 1-Perform a task
# 2-Return a value

# Rewriting the greet function into type 2:


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("rae")
file = open("content.txt", "w")
file.write(message)


def greet(name):
    print(f"Hi {name}")


greet("Rae")                    # Hi Rae
print(greet("Rae"))             # None
print(type(greet("Rae")))         # <class 'NoneType'>
which means the(1-Perform a task) type doesnt return value, so the value is none(absence of value).


def increment(number, by):
    return number + by


print(increment(2, by=1))  # more readable


# SyntaxError: non-default argument follows default argument
def increment(number, by=1, another):
    return number + by


print(increment(2, by=1))  # more readable


def multiply(*numbers):
    print(numbers)


multiply(2, 3)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):  # using**in the argument of the function, when recall the data,


python will automatically package the data into the dictionary

print(user)


save_user(id=1, name="john", age=22)
# print out: {'id': 1, 'name': 'john', 'age': 22} This is a data structure type called dictionary!!


def save_user(**user):
    # using the bracket notation, can get the value of various keys in this dictionary.
    print(user["name"])


save_user(id=1, name="john", age=22)


def greet(name):  # name is the parameter  #local variables
    message = "a"  # a very important concept in python: scope
    # which refers to the region of the code where a variable is defined.


def send_email(name):
    message = "b"


printgreet("rae")  # output: name error. name is not defined.


there is also a concept named global variable. // garbage collected
message = "a"


def greet(name):
    message = "b"
    return message


print(greet("mosh"))


# a bad practice , but just try it!!!
message = "a"


def greet(name):
    global message
    message = "b"
    return message


# The out put is b! there might be multipul function rely on the global variable
print(greet("mosh"))
# If u accidentally change the global variable in one function
# There might cause tons of side effect on the other funchin which use this variable.


# Now we can learn how to find and fix bugs in programs!!
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
# use the bug icon or the short cut ctrl+shif+D to start debugging.


print("Start")       # add breakpoint on one of these statements.
print(multiply(1, 2, 3))  # put the cursor on one of this line
# and then press F9, so that we can insert a breakpoint on lineX :)
# Then press F5 to run the application up to this breakpoint
# Press F10, to execute one statement at a time
# Press F11 to step into the function
# Shift + F5 to stop the debugger.
# Shift+F11 to step out of the function.


Do some tricks!!!!Yeah!
1.put your cursor to the end shortcut: the endkey(Fn+right arrow)
2. Similarly put your cursor to the beginning of the line: the homekey(Fn+left arrow)
3. ctrl + home: to put your cursor to the beginning of the file
4. ctrl + end: to put your cursor to the end of the file
5.pressing alt and use up and down arrows to move the line you selected.
6.shift + alt + up or down arrow to duplicate the line you selected
7. ctrl+/ to make the code to comment.same short cut to remove the comment.
8. just type the forst few characters and enter to make auto-completion.


# The question often comes in programming interviews: fizz buzz algorithms
def fizz_buzz(input):
    if input % 3 == 0 and input % 5 != 0:
        result = "fizz"
    elif input % 5 == 0 and input % 3 != 0:
        result = "buzz"
    elif input % 5 == 0 and input % 3 == 0:
        result = "fizzbuzz"
    else:
        result = input
    return result


# This is one way to implement the rules, but not the best way.
print(fizz_buzz(5))

# Here is the best way!!


def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "fizzbuzz"  # return means execute the program.
    if input % 3 == 0:
        return "fizz"
    if input % 5 == 0:
        return "buzz"
    return input


print(fizz_buzz(7))
