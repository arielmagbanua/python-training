# Firstname Lastname <-- Replace this part with your actual first name and last name

# Assigns the value of your favorite integer to the variable
numfave=23

# Creates a counting variable called ucount that counts the number of guesses made by the user
ucount = 0

# ask the user to guess correctly the numfave value until user guesses the correct number
while True:
    # increment number of tries
    ucount += 1

    # ask for integer input
    input_number = input('Guess my integer\n')

    # convert the inputted value into an integer (assume the user will only input integers)
    input_number = int(input_number)

    if input_number == numfave:
        print('You guessed correctly my favorite number!')
        print("Number of attempts: " + str(ucount))

        # break the loop since user guessed the number correctly
        break
    elif input_number > numfave:
        print('Input number is too high!')
    else:
        print('Input number is too low!')
