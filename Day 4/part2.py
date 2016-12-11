from collections import Counter
from operator import itemgetter
import re
from string import ascii_lowercase as lower

def process(x):
    clean = re.sub(r'-',r' ',x)
    regex = r'([a-z]+(?=[1-9]))(\d+)\[(\w{5})'
    return re.findall(regex,clean)

def compare(x):
    #x is the cleaned input
    for group in x:
        for subgroup in group:
            counted =  Counter(subgroup[0]).most_common()
            counted = sorted(counted,key=itemgetter(0))
            counted = sorted(counted,key=itemgetter(1),reverse=True)
            ch = ''
            for tf in range(5):
                ch += counted[tf][0]
            if ch == subgroup[2]:
                #then it is valid, so decode
                #z is the decoded string
                z = cipher(subgroup[0])
                print z
    return None

def cipher(x,y):
    # x is a valid string to be decoded
    # y is the sector id and also the rotation to be performed
    #use module on the shifted letter
    # z is the return string
    z = ''
    for letter in x:
        z += chr(ord(letter))


def main():
    x = []
    with open('test.txt','r') as f:
     for line in f:
         x.append(process(line))
    print compare(x)
    test_string = 'qzmt zixmtkozy ivhz'
    print cipher(test_string)


if __name__ == '__main__':
    main()
