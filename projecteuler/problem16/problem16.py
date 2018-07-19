
"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""


print('Euler problem 16')

bignum = 2**1000
print(bignum)

stringnum=str(bignum)
sumdigits=0
for digit in stringnum:
    sumdigits += int(digit)

print('Sum digits: ', sumdigits)

