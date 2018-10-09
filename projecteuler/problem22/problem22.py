"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""


def calc_alpha_val(name):
    val=0
    for letter in name:
        letval = 1+ord(letter)-ord('A')
        val += letval
    return val

def calc_score(name,pos):
    alpha_value = calc_alpha_val(name)
    return (pos*alpha_value)

def main():
    print('problem 22')
    csvfile='p022_names.txt'
    allnames_str = open(csvfile,'r').read().replace('"','')
    allnames_lst = allnames_str.split(',')
    allnames_lst.sort()
    print('Nr of names in list:', len(allnames_lst))
    test_position = 938
    test_name = 'COLIN'
    test_idx = test_position - 1
    assert( allnames_lst[test_idx] == test_name )
    #print(allnames_lst)
    total_score = 0
    for idx in range(0, len(allnames_lst)):
        name=allnames_lst[idx]
        position=idx+1
        score = calc_score(name,position)
        #print(name,position,score)
        total_score += score
    print(total_score)

if __name__ == '__main__':
    main()

