#Input two binary numbers using space

# get the two binary inputs separated by spaces
bnum1, bnum2 = input("Enter two binary numbers: ").split()

# get the maximum length among the two binaries
max_len = max(len(bnum1), len(bnum2))

# fill out the zeros of those shorter binary numbers
bnum1 = bnum1.zfill(max_len)
bnum2 = bnum2.zfill(max_len)

result = ''

carry = 0

for i in range(max_len -1, -1, -1):
    r = carry
    r += 1 if bnum1[i] == '1' else 0
    r += 1 if bnum2[i] == '1' else 0

    # if r is 1 this means adding 1 and 0, if r is 2 you are adding 1 and 1
    result = ('1' if r % 2 == 1 else '0') + result

    # if r is 2 that means you are adding 1 and 1
    carry = 0 if r < 2 else 1

# append if there is carry
if carry != 0:
    result = '1' + result

print(result.zfill(max_len))
