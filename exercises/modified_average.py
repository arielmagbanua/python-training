def average(num, *arg):
    """Calculates the average of at least 1 number

    Parameters:
    num (int|float): The required number argument.
    arg: Arbitary argument list of numbers.
    """

    # sum of arguments
    sum_arg = sum(arg)
    # get the sum of all numbers
    all_sum = num + sum_arg

    # return the average by dividing the sum
    # with the length of arguments + 1 (for num)
    return all_sum / (1 + len(arg))

# test cases
print(average(2, 4, 5, 6, 10, 12)) # 6.5
print(average(10)) # 10.0
print(average()) # TypeError: average() missing 1 required positional argument: 'num'