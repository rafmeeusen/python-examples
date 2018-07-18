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

maxnum=100000
longest_len=0
longest_num=0
for i in range(1,maxnum):
    seqlen=len(collatz_seq(i))
    if seqlen > longest_len:
        #print(seqlen)
        longest_len=seqlen
        longest_num=i

print('checked Collatz sequence lengths between 1 and ',maxnum)
print('longest sequence found for ',longest_num)
print('sequence length: ',longest_len)
print(collatz_seq(longest_num))
