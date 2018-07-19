print('problem 18')

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

"""


smalltriangle=[(3), (7,4), (2,4,6), (8,5,9,3)]
bigtriangle=[
75,
(95,64),
(17,47,82),
(18,35,87,10),
(20,4,82,47,65),
(19,1,23,75,3,34),
(88,2,77,73,7,63,67),
(99,65,4,28,6,16,70,92),
(41,41,26,56,83,40,80,70,33),
(41,48,72,33,47,32,37,16,94,29),
(53,71,44,65,25,43,91,52,97,51,14),
(70,11,33,28,77,73,17,78,39,68,17,57),
(91,71,52,38,17,14,91,43,58,50,27,29,48),
(63,66,4,68,89,53,67,30,73,16,69,87,40,31),
(4,62,98,27,23,9,70,98,73,93,38,53,60,4,23),
]


#triangle = smalltriangle
triangle = bigtriangle

# check triangle format is correct
nr_rows = len(triangle)
for rowidx in range(nr_rows):
    row = triangle[rowidx]
    if type(row) == int:
        rowsize=1
    else:
        rowsize = len(row)
    expected_size = rowidx+1
    if rowsize != expected_size:
        print('Error. Row ', row, ' has size ', rowsize, ' instead of ', expected_size)

#
print('triangle with ', nr_rows, ' rows.')

def make_route(triangle, routecode):
    nr_bits = len(triangle) - 1
    leftrights = route_code2list(routecode,nr_bits)
    routedescr = ['dummy']
    routedescr.extend(leftrights)
    route = [ triangle[0] ]
    previous_column = 0
    for rowidx in range(1,len(triangle)):
        if routedescr[rowidx] == '1':
            # right:
            columnidx = previous_column + 1
        elif routedescr[rowidx] == '0':
            columnidx = previous_column
        else:
            raise Error()
        route.append(triangle[rowidx][columnidx])
        previous_column = columnidx
    return route

def print_route(triangle, routecode):
    print(make_route(triangle, routecode))

def route_code2list(code, nrbits):
    # code = number between 0 and 2^^bits-1
    # return something like [0,1,0,1]
    binstring = bin(code)[2:].zfill(nrbits)
    return list(binstring)

nr_bits = len(triangle) - 1

# test some route: (0=left/1=right)
routecode = 5
print('route coding: ', routecode)
print('route list: ', route_code2list(routecode, nr_bits))
print_route(triangle,routecode)

# test some random route:
import random
routecode=random.randint(0,2**nr_bits-1)
print('route coding: ', routecode)
print('route list: ', route_code2list(routecode, nr_bits))
print_route(triangle,routecode)

# now the actual problem:
maxsum=0
maxroute=None
maxcode=None
for routecode in range(2**nr_bits):
    route = make_route(triangle,routecode)
    if sum(route) > maxsum:
        maxsum = sum(route)
        maxroute = route
        maxcode = routecode

print('Results:')
print('Code: ', maxcode)
print('Route: ', maxroute)
print('Sum: ', maxsum)



