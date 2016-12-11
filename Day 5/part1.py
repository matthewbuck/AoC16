import hashlib

def main():
    x = 'reyedfim'
    password = ''
    y = 0
    while len(password) < 8:
        if hashlib.md5(x+str(y)).hexdigest()[:5] == '00000':
            password += hashlib.md5(x+str(y)).hexdigest()[5]
            print hashlib.md5(x+str(y)).hexdigest()
        y += 1
    print password


if __name__ == '__main__':
    main()