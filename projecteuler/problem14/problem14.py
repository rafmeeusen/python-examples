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

def collatz_seq_len(num):
    len=1
    while num != 1:
        num = collatz_next(num)
        len += 1
    return len

print('example: Collatz sequence for number 51:')
print(collatz_seq(51))

print('example: Collatz sequence length for number 51:')
print(collatz_seq_len(51))

maxnum=1000000
longest_len=0
longest_num=0
for i in range(1,maxnum):
    seqlen=collatz_seq_len(i)
    if seqlen > longest_len:
        #print(seqlen)
        longest_len=seqlen
        longest_num=i

print('checked Collatz sequence lengths between 1 and ',maxnum)
print('longest sequence found for ',longest_num)
print('sequence length: ',longest_len)
print(collatz_seq(longest_num))
