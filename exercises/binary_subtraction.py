# get the two binary inputs separated by spaces
bnum1, bnum2 = input("Enter two binary numbers: ").split()

# get the maximum length among the two binaries
max_len = max(len(bnum1), len(bnum2))

# fill out the zeros of those shorter binary numbers
bnum1 = bnum1.zfill(max_len)
bnum2 = bnum2.zfill(max_len)

result = ''

borrow = False

for i in range(max_len -1, -1, -1):
    r = ''

    if borrow:
        if bnum1[i] == '0':
            bnum1 = bnum1[:i] + '2' + bnum1[i+1:]
        else:
            borrow = False
            bnum1 = bnum1[:i] + '0' + bnum1[i+1:]

    if bnum1[i] == '0' and bnum2[i] == '1':
        r += '1'
        borrow = True
    elif bnum1[i] == '2' or (bnum1[i] == '1' and bnum2[i] == '0'):
        r += '1'
    else:
        r += '0'
    
    result += r

# fill out empty spaces with 0
result = result.zfill(max_len)
# reverse the result
result = result[::-1]
print(result)
    
