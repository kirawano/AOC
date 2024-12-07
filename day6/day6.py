from time import sleep
aoc = []
with open("input.txt", "r") as f:
    lines = f.read()
    for line in lines.split("\n"):
        hi = []
        for l in line:
            hi.append(l)
        aoc.append(hi)

direction = {
        0:(-1,0),
        1:(0,1),
        2:(1,0),
        3:(0,-1)
        }

def get_guy(aoc):
    x = 0
    y = 0
    for i in range(len(aoc)):
        for j in range(len(aoc[0])):
            if aoc[i][j] == "^":
                x = i
                y = j
    return (x,y)

def part1(aoc):
    positions = []
    dindex = 0
    while True:
        x,y = get_guy(aoc)
        if (x,y) not in positions:
            positions.append((x,y))

        dir = direction[dindex % 4]
        dx,dy = dir

        #print_grid(aoc)
        #sleep(1)

        if x+dx < 0 or y+dy < 0:
            return positions
#        print(str(dx) + ", " + str(dy))


        try:
#            print(aoc[x+dx][y+dy])
            if aoc[x+dx][y+dy] != "#" and (x+dx >= 0 and y+dy >= 0):
                x+=dx
                y+=dy
            else:
                dindex+=1
                dir = direction[dindex % 4]
        except IndexError:
            return positions 

        aoc[x][y]="^"
        aoc[x-dx][y-dy]="X"
    
def part2(aoc_param):
    total = 0
    a = []
    for i in aoc_param:
        hi = []
        for j in i:
            hi.append(j)
        a.append(hi)
    path = part1(a)
    print(len(path))
    profile = 0
    for timepara in path:
        print(profile)
        positions = []
        aoc = []
        for i in aoc_param:
            hi = []
            for j in i:
                hi.append(j)
            aoc.append(hi)
        xobs,yobs = timepara
        aoc[xobs][yobs]="#"
        dindex = 0
        x,y = get_guy(aoc)
        while True:
            #print(positions)
            #print_grid(aoc)
            #sleep(1)
            dir = direction[dindex % 4]
            dx,dy = dir
            if (x,y,dir) not in positions:
                positions.append((x,y,dir))
            else:
                #print("oml")
                total+=1
                break
            if x+dx < 0 or y+dy < 0:
                #print("I'm broke")
                break

            try:
                if aoc[x+dx][y+dy] != "#" and (x+dx >= 0 and y+dy >= 0):
                    x+=dx
                    y+=dy
                else:
                    dindex+=1
                    dir = direction[dindex % 4]
            except IndexError:
                #print("I'm broke")
                break

            aoc[x][y]="^"
            aoc[x-dx][y-dy]="."
        
        aoc[xobs][yobs] = "."
        profile+=1
    return total



test = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

def print_grid(grid):
    for i in grid:
        for j in i:
            print(j,end='\t')
        print("\n")

    print("\n==========================================================================================\n")

gwid = []
for i in test.split("\n"):
    hi = []
    for j in i:
        hi.append(j)
    gwid.append(hi) 
gwid.pop(len(gwid)-1)
gwid.pop(0)
aoc.pop(len(aoc)-1)


print(part2(aoc))

