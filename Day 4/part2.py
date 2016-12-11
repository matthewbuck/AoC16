from collections import Counter
from operator import itemgetter
import re

def process(x):
    clean = re.sub(r'-',r' ',x)
    regex = r'(\D+)(\d+)\[(\w+)'
    return re.findall(regex,clean)

def compare(x):
    for group in x:
        for subgroup in group:
            counted =  Counter(subgroup[0].replace(' ','')).most_common()
            counted = sorted(counted,key=itemgetter(0))
            counted = sorted(counted,key=itemgetter(1),reverse=True)
            ch = ''
            for tf in range(5):
                ch += counted[tf][0]
            if ch == subgroup[2]:
                z = cipher(subgroup[0],subgroup[1])
                if 'north' in z:
                    print z
                    print subgroup[0],subgroup[1]
    return None

def cipher(x,y):
    z = ''
    shift = int(y) % 26
    for letter in x:
        if letter == ' ':
            z += ' '
        else:
            z += chr((ord(letter)-97+shift)%26+97)
    return z


def main():
    x = []
    with open('input.txt','r') as f:
     for line in f:
         x.append(process(line))
    print compare(x)


if __name__ == '__main__':
    main()
