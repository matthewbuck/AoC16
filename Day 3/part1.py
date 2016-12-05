import re

def main():
    count = 0
    input = open('input.txt','r+').read().splitlines()
    for line in input:
        clean = re.findall('(\\d+)',line)
        clean = sorted([int(x) for x in clean])
        if clean[0] + clean [1] > clean[2]:
            count +=1
    print 'There are {} possible triangles.'.format(count)



if __name__ == '__main__':
    main()