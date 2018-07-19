
"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""


print('Euler problem 17')

import inflect
p = inflect.engine()

print('example number-to-words: 666: ', p.number_to_words(666))
print('example number-to-words: 102 without space/hyphen: ', p.number_to_words(102).replace('-','').replace(' ',''))

counter=0
for num in range(1,1001):
    num_string = p.number_to_words(num).replace('-','').replace(' ','')
    counter+= len(num_string)

print('problem solution:')
print(counter)


