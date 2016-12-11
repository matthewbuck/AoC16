def process(text_input):
    facing = 90
    current_x = 0
    current_y = 0
    mod = {0:1,90:1,180:-1,270:-1}
    past = []
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
            destination_y = current_y + modifier*int(val)
            while current_y != destination_y:
                location = (current_x,current_y)
                if location in past:
                    return current_x+current_y
                else:
                    past.append(location)
                    current_y += modifier
        else:
            destination_x = current_x + modifier*int(val)
            while current_x != destination_x:
                location = (current_x,current_y)
                if location in past:
                    return current_x+current_y
                else:
                    past.append(location)
                    current_x += modifier
            
            
def main():
    f = open("input.txt","r+")
    m = f.read()
    n = m.split(', ')
    answer = process(n)
    print "The Bunny HQ is {} blocks away.".format(answer)
    return 0

if __name__ == "__main__":
    main()
