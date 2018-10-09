
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

def proper_divisors(n):
    list_divs=[1]
    max_div = 1+int(n/2)
    for candidate in range(2,max_div):
        if n % candidate == 0:
            list_divs.append(candidate)
    return list_divs


def d_of_n(n):
    d=sum(proper_divisors(n))
    return d


def main():
    print('problem 21')
    ''' data structure to find amicable numbers: need to map n to d (d_of_n), and easily map back;
        simple array indexing is OK.
        index0 unused; index 1 to max_num will be used
    '''
    max_num = 10000
    print('searching amicable nums up to',max_num)
    our_range = range(1,max_num)
    d_list=[None]*(max_num+1)
    for i in our_range:
        d_list[i] = d_of_n(i)
    amicables=[]
    ''' now scan list for amicables '''
    for i in our_range:
        d_of_i = d_list[i]
        if i != d_of_i and d_of_i in our_range:
            d_of_dofi = d_list[ d_of_i ]
            if i == d_of_dofi:
                print('found:', i, d_of_i)
                amicables.append( i )
                amicables.append( d_of_i )
                ''' prevent higher number to trigger again number to be found '''
                d_list[ d_of_i ] = None
    print('amicables:', amicables)
    print('sum:', sum(amicables))

if __name__ == '__main__':
    main()

