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
    result = []
    quotient = n

    if n < radix:
        result.append(n)

    while quotient >= radix:
        quotien_result = math.floor(quotient / radix)
        remainder = quotient % radix

        quotient = quotien_result

        result.append(remainder)

        if quotient < radix:
            result.append(quotient)
    
    # reverse the order
    result = result[::-1]

    # replace the numbers with letters depending on radix
    new_result = []
    for num in result:
        val = num

        if 10 <= num < radix:
            # compute for the right index and get the equivalent letter
            val = number_letters[num - 10]
        
        new_result.append(val)

    return new_result

def dec_to_any_string(n, radix):
    # get the list form of conversion
    converted = dec_to_any_list(n, radix)
    
    # using list comprehension cast / convert each item to string 
    converted = [str(item) for item in converted]

    # join the list into one string and return it
    converted_number = ''.join(converted)
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

    if (radix > 16):
        print('Wrong Input!!!')
        return

    converted_number = dec_to_any_string(n, radix)

    print('%d in base 10 is %s in base %d' % (n, converted_number, radix))

main()
