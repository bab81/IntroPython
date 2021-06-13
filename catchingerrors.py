
try:
    number = int(input("Enter a number: "))
    print(number)
except ValueError as err: # there can be multiple except blocks for a try block, depending on the type of error.
    print("Invalid input")
    print (err)
