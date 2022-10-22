def validate(numbers):
    """
    This function validates lottery numbers.

    Args:
        list (numbers): It is a list that contains the lotter numbers.
    
    Returns:
        boolean: True if lottery numbers is valid otherwise false.
    """

    # check if the numbers is greater than or less than 6
    if len(numbers) > 6 or len(numbers) < 6:
        print('Should be 6 numbers')
        return False

    # check if there are duplicates
    numbers_set = set(numbers)
    if len(numbers_set) != len(numbers):
        print('No Duplicates')
        return False
    
    return True

# get user input
input = input().split()

# get the name of the user from the input
user = input[0]

# get the lotter numbers
lottery_numbers = input[1::]

# check for price money
if validate(lottery_numbers):
    # winning numbers
    winning_numbers = {10, 11, 8, 1, 5, 20}

    count = 0

    for num in lottery_numbers:
        if int(num) in winning_numbers:
            count += 1
    
    # calculate price money
    price_money = count * 100

    if price_money == 0:
        print(f'{user} won nothing!')
    else:
        print(f'{user} won {price_money} pesos!')
