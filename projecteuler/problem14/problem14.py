def collatz_next(num):
    if num%2:
        return 3*num+1
    else:
        return int(num/2)


def collatz_seq(num):
    seq=[num]
    while seq[-1] != 1:
        seq.append(collatz_next(seq[-1]))
    return seq


print('example: Collatz sequence for number 51:')
print(collatz_seq(51))

 
