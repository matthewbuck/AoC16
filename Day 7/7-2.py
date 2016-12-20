import re
def process(x):
    r = re.compile(r'\[(\w+)]')
    ip = re.sub(r,' ',x).split(' ')
    hyper = re.findall(r,x)
    return ip,hyper

def ssl(x):
    for item in x[0]:
        for idx in range(len(item)-2):
            aba = item[idx:idx+3]
            if aba[0] == aba[2] and aba[0] != aba[1]:
                for hyper in x[1]:
                    if aba[1]+aba[0]+aba[1] in hyper:
                        return 1
    return 0

def main():
    counter = 0
    with open('input.txt','r') as f:
        for line in f:
            counter += ssl(process(line.strip()))
    print counter

if __name__ == '__main__':
    main()