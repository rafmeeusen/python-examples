#!/usr/bin/python3
# projecteuler.net
# problem 12
# highly divisible triangular number

from collections import namedtuple
import pyprimes

limit_nr_divisors=20

TriangNum = namedtuple('TriangNum',['idx','num'])

def triangular(n):
    return int(n*(n+1)/2)

def nextTriangular(previous=TriangNum(1,1)):
    newidx = previous.idx + 1
    newnum = previous.num + newidx
    return TriangNum(newidx,newnum)

def primefactors(n):
    primelist = {}
    divider=2
    primelist[divider]=0
    while n > 1:
#        print('div ',divider, 'n',n)
        if n%divider == 0:
            n=n//divider
            primelist[divider]+=1
        else:
#            divider=pyprimes.next_prime(divider)
            divider+=1
            primelist[divider]=0
#TODO: why was this so slow:
#    for i in range(2, n//2+1):
#        while not n%i:
#            print(i)
#            if i in primelist:
#                primelist[i]+=1;
#            else:
#                primelist[i]=1;
#            n=n/i
    return primelist

tn = nextTriangular()
"""
for i in range(1,max):
    print(tn)
    primefactors(tn.num)
    tn = nextTriangular(tn)
"""


def nrOfDivisors(num):
    primedividers=primefactors(num)
    nrdividers=1
    for prime in primedividers.keys():
        exponent=primedividers[prime]
        nrdividers *= (exponent+1)
    return nrdividers




tn = nextTriangular()
while nrOfDivisors(tn.num) <= limit_nr_divisors:
    tn = nextTriangular(tn)
#    print("triangular number:", tn)
#    print("primedivs:", primefactors(tn.num))
#    print("nr divs:", nrOfDivisors(tn.num))

print("triangular number:", tn)
print("primedivs:", primefactors(tn.num))
print("nr divs:", nrOfDivisors(tn.num))

print('mmm not getting anywhere')

# any triangular number: n*(n+1)/2

# d(x), number of divisors, is (e1+1)*(e2+1)*... with e1,e2... the exponents of cannonical factorization
# d(x) is multiplicative function; d(x*y) = d(x)*d(y); BUT: this holds only if x and y don't share prime factors!
# ??? useful?? : d(tn) = d(n)*d(n+1)*(1+new_exp_2)/(1+old_exp_2)
#
# n*(n+1) is also > n^2;

thesqrt=2**250
print('2^250:', thesqrt)
#print("nr divs:", nrOfDivisors(thesqrt))
# nr divs for thesqrt: simple, e=250, so its e+1 = 251.
print('2^250+1', thesqrt+1)

#print("nr divs:", nrOfDivisors(thesqrt+1))
print ( primefactors( (2**3)*(4**5)*(7**5)*(9**5)*(113**9)*(1001*3)) )
#print ( primefactors( 11223344556677889900 ))

print('mmmm. prime factorization is indeed slow even for 2^250 order of magnitude... won\'t solve it this way')
# 499 is prime
# is 2^499-1 a Mersenne prime? no, not prime...

# 2*Tn = n*(n+1)
# d(2*Tn) =  d(n) * d(n+1) (IFF n and n+1 coprime!!)
# we want d(Tn) > 500.
# 22^2=484; 22*23=506
# smallest n for which d(n) = 22: 2^21
# 2^22: d(..)=23 (22+1)
# 2^22+1 or 2^22-1: odd numbers, so NO 2 in the factorization.


print("nr divs 2^22:", nrOfDivisors(2**22))
print("nr divs 2^22-1:", nrOfDivisors(2**22-1))

print("T500:",triangular(500))
print("nr divs T500:", nrOfDivisors(triangular(500)))



# just found out: a peak in d(n) function is called a "highly composite number"
# so we are looking for highly composite number with d(n) > 500, and then the next triangular number Tm.
# is there a way?
# well, it can be looked up in a list of "HCN's":
print('48th HCN = 14414400, has d(n)=504, and equals  2^6 * 3^2 * 5^2 * 7^1 * 11*1 * 13^1')
#

# mmm; my first reasoning about needing a number larger than 2^500 was wrong!!! 
# Tn > 14414400: 5369*5370/2 ?
print("T5368:", triangular(5368))
print("T5369:", triangular(5369))
print("T5370:", triangular(5370))

print('So: T5369 is smallest Tn that could have d(n) > 500...')

#n=1
n=5369
tn=triangular(n)
dtn=nrOfDivisors(tn)
print('nr divs T', n, '=',tn, ' is:', dtn)

while dtn < 500:
    n+=1
    tn=triangular(n)
    dtn=nrOfDivisors(tn)
    print('nr divs T', n, '=',tn, ' is:', dtn)


#print("nr divs T5369:", nrOfDivisors(triangular(5369)))
#print("nr divs T5370:", nrOfDivisors(triangular(5370)))
