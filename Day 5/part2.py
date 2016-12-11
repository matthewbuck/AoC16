import hashlib

def main():
    x = 'reyedfim'
    password = ['*' for num in range(8)]
    y = 0
    while '*' in password:
        digest = hashlib.md5(x+str(y)).hexdigest()
        if digest[:5] == '00000':
            if ord(digest[5]) >= 48 and ord(digest[5]) < 56 :
                position = int(digest[5])
                if password[position] == '*':
                    password[position] = digest[6]
                    print ''.join(password)
        y += 1


if __name__ == '__main__':
    main()