def process(text_input):
    facing = 90
    current_x = 0
    current_y = 0
    mod = {0:1,90:1,180:-1,270:-1}
    for item in text_input:
        if 'R' in item:
            facing += 90
        else:
            facing -= 90
        if facing < 0:
            facing += 360
        elif facing >= 360:
            facing -= 360
        modifier = mod[facing]
        val = item.lstrip('RL')
        if facing == 90 or facing == 270:
            current_y += modifier*int(val)
        else:
            current_x += modifier*int(val)

    return current_x+current_y

            
def main():
    f = open("input.txt","r+")
    m = f.read()
    n = m.split(', ')
    answer = process(n)
    print "The Bunny HQ is {} blocks away.".format(answer)
    return 0

if __name__ == "__main__":
    main()
