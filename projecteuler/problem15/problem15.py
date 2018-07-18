
"""
Combinatorics

20 times d 'down' and 20 times 'r' right in any possible combination.
e.g. dddrrrdddrrrdddrrrdrdddrrrdddrrrdddrrrdr
warning: not just power of 2; not unlimited combinations, if 20 d are used, all remaining are r.

solution 1:
nr of permutations of 40 items: 40!, but divide by permutations of equals: (40!)/(20!)/(20!)

"""


print('Euler problem 15')
import math
print( int(math.factorial(40)/ math.factorial(20)/math.factorial(20)) )
