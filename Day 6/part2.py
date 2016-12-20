from collections import Counter

def count(x):
    code = ''
    for ll in x.itervalues():
        code += Counter(ll).most_common()[-1][0]
    return code
def main():
    bi = {n:[] for n in range(8)}
    with open('input.txt','r') as f:
        for line in f:
            for letters in range(8):
                bi[letters].append(line[letters])
    print count(bi)

    return None

if __name__ == '__main__':
    main()