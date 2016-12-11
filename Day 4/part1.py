from collections import Counter
from operator import itemgetter
import re

def process(x):
    clean = re.sub(r'-',r'',x)
    regex = r'([a-z]+(?=[1-9]))(\d+)\[(\w{5})'
    return re.findall(regex,clean)

def compare(x):
    #x is the cleaned input
    total = 0
    for group in x:
        for subgroup in group:
            # subgroup[0] is the string, 1 is the number, 2 is the hash
            counted =  Counter(subgroup[0]).most_common()
            counted = sorted(counted,key=itemgetter(0))
            counted = sorted(counted,key=itemgetter(1),reverse=True)
            #counted isnt alphabetized
            # need to pull out the top 5 for comparison to hash
            # could access indicies 0-4, concatenate them
            #access by counted[0-4][0]
            #tf = top five
            #ch = computed hash
            ch = ''
            for tf in range(5):
                ch += counted[tf][0]
            #now compare ch to subgroup[2]
            if ch == subgroup[2]:
                #then the hashes are equivalent and it can be added to the total
                total += int(subgroup[1])
    return total

def main():
    x = []
    with open('test.txt','r') as f:
     for line in f:
         x.append(process(line))
    print compare(x)

"""print content
for item in x :
    for message in item:
        print Counter(message).most_common()
"""

if __name__ == '__main__':
    main()
