
import math
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
"""




def main():
    print('problem 20')
    number = math.factorial(100)
    print(number)
    stringnum=str(number)
    sumdigits=0
    for digit in stringnum:
        sumdigits += int(digit)
    print('Sum digits: ', sumdigits)


main()


