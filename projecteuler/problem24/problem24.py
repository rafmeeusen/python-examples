"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import math
import itertools



def main():
    print('problem 24')
    nrpermu=math.factorial(10)
    print('nr of permutations:',nrpermu)
    nrpermu_0X=math.factorial(9)
    print('permutations 1 until', nrpermu_0X, 'start with 0')
    print('permutations', nrpermu_0X+1, 'until', 2*nrpermu_0X, 'start with 1')
    print('permutations', 2*nrpermu_0X+1, 'until', 3*nrpermu_0X, 'start with 2')

    nrpermu_20X=math.factorial(8)
    print('permutations', 2*nrpermu_0X+1, 'until', 2*nrpermu_0X+nrpermu_20X, 'start with 20')
    print('permutations', 2*nrpermu_0X+nrpermu_20X+1, 'until', 2*nrpermu_0X+2*nrpermu_20X, 'start with 21')
    print('permutations', 2*nrpermu_0X+2*nrpermu_20X+1, 'until', 2*nrpermu_0X+3*nrpermu_20X, 'start with 23')
    print('permutations', 2*nrpermu_0X+3*nrpermu_20X+1, 'until', 2*nrpermu_0X+4*nrpermu_20X, 'start with 24')
    print('permutations', 2*nrpermu_0X+4*nrpermu_20X+1, 'until', 2*nrpermu_0X+5*nrpermu_20X, 'start with 25')
    print('permutations', 2*nrpermu_0X+5*nrpermu_20X+1, 'until', 2*nrpermu_0X+6*nrpermu_20X, 'start with 26')
    print('permutations', 2*nrpermu_0X+6*nrpermu_20X+1, 'until', 2*nrpermu_0X+7*nrpermu_20X, 'start with 27')
    print('permutations', 2*nrpermu_0X+7*nrpermu_20X+1, 'until', 2*nrpermu_0X+8*nrpermu_20X, 'start with 28')
    print('permutations', 2*nrpermu_0X+8*nrpermu_20X+1, 'until', 2*nrpermu_0X+9*nrpermu_20X, 'start with 29')

    print('so it seems that our solution starts with 27')

    #sortedlist=(list(itertools.permutations([0, 1, 3, 4, 5, 6, 8, 9]))).sort()
    tmp=list(itertools.permutations([0, 1, 3, 4, 5, 6, 8, 9]))
    sortedlist=tmp
    sortedlist.sort()
    overall_idx_of_idx0 = 2*nrpermu_0X+6*nrpermu_20X+1
    idx_of_1m = 1000000 - overall_idx_of_idx0
    print( 'item', overall_idx_of_idx0, ':',sortedlist[0] )
    for i in range(idx_of_1m-10,idx_of_1m+10):
        print( 'item', overall_idx_of_idx0+i, ':', sortedlist[i])

if __name__ == '__main__':
    main()

