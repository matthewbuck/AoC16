import re
def process(x):
    #perhaps after the join there are new abbas created that shouldn't be counted
    r = re.compile(r'\[(\w+)]')
    ip = re.sub(r,' ',x).split(' ')
    hyper = re.findall(r,x)
    return ip,hyper

def check(x):
    for items in x[1]:
        if pal(items):
            return 0
    for items in x[0]:
        if pal(items):
            return 1
    else:
        return 0

def pal(x):
    for idx in range(len(x)-3):
        poss = x[idx:idx+4]
        if poss == poss[::-1] and poss[0] != poss[1]:
            return True

def main():
    counter = 0
    with open('input.txt','r') as f:
        for line in f:
            counter += check(process(line.strip()))
    print counter

if __name__ == '__main__':
    main()