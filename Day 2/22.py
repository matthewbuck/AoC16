grid1 = [['0','0','1','0','0'],
        ['0','2','3','4','0'],
        ['5','6','7','8','9'],
        ['0','A','B','C','0'],
        ['0','0','D','0','0']]

instructions1 = {
    'U':(-1,0),
    'D': (1,0),
    'R': (0,1),
    'L': (0,-1)
}


def move(input,grid,instructions):
    code = ''
    position = (2,0)
    for line in input:
        for direction in line:
            new = instructions[direction]
            next = (position[0] + new[0], position[1] + new[1])
            if next[0] > 4 or next[0] < 0 or next[1] > 4 or next[1] < 0 or grid[next[0]][next[1]] == '0':
                pass
            else:
                position = next
        code += grid[position[0]][position[1]]
    return code



def main():
    f = open('input.txt','r+')
    m = f.read().splitlines()
    test = ['ULL','RRDDD','LURDL','UUUUD']
    print move(m,grid1,instructions1)

if __name__ == '__main__':
    main()