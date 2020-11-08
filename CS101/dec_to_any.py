import math

number_letters = 'ABCDEF'

#--------------------------------------------------------------#
#
# Function dec_to_any
#
# Input:
#		n: number to convert
#		radix: radix to use
#
# Output:
#		new_num: converted number
#
#--------------------------------------------------------------#
def dec_to_any_list(n, radix):
    converted_number = []
    quotient = n

    if n < radix:
        converted_number.append(n)

    while quotient >= radix:
        quotien_result = math.floor(quotient / radix)
        remainder = quotient % radix

        quotient = quotien_result

        converted_number.append(remainder)

        if quotient < radix:
            converted_number.append(quotient)

    # reverse the order
    converted_number = converted_number[::-1]

    # replace the numbers with letters depending on radix
    new_result = []

    for num in converted_number:
        val = num

        if 10 <= num < radix:
            # compute for the right index and get the equivalent letter
            index = num - 10
            val = number_letters[index]

        new_result.append(val)

    return new_result

def dec_to_any_string(n, radix):
    # get the list form of conversion
    converted = dec_to_any_list(n, radix)
 
    # using list comprehension cast / convert each item to string 
    # converted = [str(item) for item in converted]

    new_converted = []
    for item in converted:
        new_converted.append(str(item))

    # join the list into one string and return it
    converted_number = ''.join(new_converted)
    return converted_number

#--------------------------------------------------------------#
#
# Function main
#
# This is the driver function
# Do commandline input/output and formatting here
#
#		Example:
#		Enter a number: 61
#		Enter a radix: 16
#		61 in base 10 is 3D in base 16
#
#
# Just digits, no gap or another character
# 123 (O)    ‘1’ ‘2’ ‘3’ (x)
# “Wrong input!!!” if inputs are not in range
# You must use the formatting operator % (TAs will check!!!)

#--------------------------------------------------------------#

def main():
    n = int(input('Enter a number: '))
    if (n < 0):
        print('Wrong Input!!!')
        return

    radix = int(input('Enter a radix: '))
    if (radix > 16 or radix < 2):
        print('Wrong Input!!!')
        return

    converted_number = dec_to_any_string(n, radix)

    print('%d in base 10 is %s in base %d' % (n, converted_number, radix))

main()
