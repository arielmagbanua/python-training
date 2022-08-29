# get the inputs from the console
operation, first_number, second_number = input().split()

# convert string to intergers
first_number = int(first_number)
second_number = int(second_number)

if operation == "A":
    print(first_number + second_number)
elif operation == "S":
    print(first_number - second_number)
elif operation == "%":
    print(first_number % second_number)
elif operation == ">":
    print(1 if first_number > second_number else 0)
elif operation == "<":
    print(1 if first_number < second_number else 0)
else:
    print("Invalid operation!")
