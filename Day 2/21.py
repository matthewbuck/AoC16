def decode(input):
    id = {'U':-3,'D':3,'L':-1,'R':1}
    seed = 5
    codeword = ''
    for line in input:
        for instruction in line:
            if check(seed,instruction):
                temp = seed + id[instruction]
                if temp > 0 and temp < 10:
                    seed = temp
        codeword += str(seed)
    return codeword

def check(val,instruction):
    x = (3,6,9)
    y = (1,4,7)
    if val in x and instruction == 'R':
        return False
    elif val in y and instruction == 'L':
        return False
    else:
        return True

def main():
    f = open('input.txt','r+')
    m = f.read().splitlines()
    test = ['ULL','RRDDD','LURDL','UUUUD']
    print 'The codeword is {}.'.format(decode(m))

if __name__ == '__main__':
    main()