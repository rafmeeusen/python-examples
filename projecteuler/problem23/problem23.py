"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
from rafsint import RafsInt

def main():
    print('problem 23')
    maxval = 28123
    #let's just list all abundant numbers between 0, max 28123
    abundant_list=[]
    for i in range(0,maxval+1):
        if RafsInt(i).is_abundant():
            abundant_list.append(i)
    sum_two_abundants_list=[]
    for x in abundant_list:
        for y in abundant_list:
            sum_two_abundants_list.append( x+y )
    not_sum_two_abundants_list=[]
    for i in range(0,maxval+1):
        if not i in sum_two_abundants_list:
            # this i cannot be written as sum of two abundant numbers
            not_sum_two_abundants_list.append(i)
    print(sum(not_sum_two_abundants_list))


if __name__ == '__main__':
    main()

