import re

def main():
    count = 0
    input = open('input.txt','r+').read().splitlines()
    new = []
    for line in input:
        clean = re.findall('(\\d+)',line)
        clean = [int(x) for x in clean]
        new.append(clean)
    for idx,row in zip(range(0,len(new),3),new[::3]):
        for turn in range(3):
            new_t = [new[idx][turn],
                    new[idx+1][turn],
                    new[idx+2][turn]]
            new_t = sorted(new_t)
            if new_t[0] + new_t[1] > new_t[2]:
                count +=1
    print 'There are {} triangles, counting vertical pairs of 3.'.format(count)

if __name__ == '__main__':
    main()