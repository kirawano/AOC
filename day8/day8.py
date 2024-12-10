from math import sqrt

def gcd(a, b):
    while b:
        a,b = b, a%b
    return a

aoc = []
with open("input.txt", "r") as f:
    lines = f.read().split("\n")
    lines.pop(len(lines)-1)
    for l in lines:
        aoc.append([i for i in l])

def distance(a,b):
    x1,y1 = a
    x2,y2 = b
    return sqrt((x1-x2)**2 + (y1-y2)**2)

def generate_opairs(x):
    opairs = []
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j:
                opairs.append((x[i],x[j]))

    return opairs

def ap(a,b):
    c,d = a
    e,f = b
    return (c+e,d+f)

def colinear(a, b, grid, positions):
    ret = 0

    x1,y1 = a
    x2,y2 = b

    dx = x2-x1
    dy = y2-y1
    
    slope = (dx,dy)

    up = ap(b,slope)
    ux, uy = up

    down = ap(a, (-dx,-dy))
    ox, oy = down

    if up not in positions and ux >= 0 and uy >= 0 and ux < len(grid) and uy < len(grid[0]):
        ret+=1
        positions.append(up)
    if down not in positions and ox >= 0 and oy >= 0 and ox < len(grid) and oy < len(grid[0]):
        ret+=1
        positions.append(down)
    
    return ret



def part1(aoc):
    positions = []
    total = 0
    keys = {}
    for i in range(len(aoc)):
        for j in range(len(aoc[0])):
            try:
                if aoc[i][j] != "." and aoc[i][j] != "#": 
                    if keys[aoc[i][j]] != None:
                        keys[aoc[i][j]].append((i,j))
            except KeyError:
                keys[aoc[i][j]] = [(i,j)]

    for key,value in keys.items():
        opairs = generate_opairs(value)
        for opair in opairs:
            o1, o2 = opair
            total+=colinear(o1,o2,aoc,positions)

    return total

def iterate(a,b,grid,positions):
    total = 0
    x1, y1 = a
    x2, y2 = b
    dx = x2-x1
    dy = y2-y1

    delta = gcd(dy,dx)
    deltay = int(dy / abs(delta))
    deltax = int(dx / abs(delta))

    print("slope: "+str(deltax)+", "+str(deltay))
    
    x = x1
    y = y1
    while x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
        if (x,y) not in positions:
            total+=1
            positions.append((x,y))
            grid[x][y] = "#"
            print((x,y))
        x+=deltax
        y+=deltay

    X = x1
    Y = y1
    while X >= 0 and X < len(grid) and Y >= 0 and Y < len(grid[0]):
        if (X,Y) not in positions:
            total+=1
            positions.append((X,Y))
            grid[X][Y] = "#"
            print((X,Y))

        X-=deltax
        Y-=deltay
    return total

def part2(aoc):
    positions = []
    total = 0
    keys = {}
    for i in range(len(aoc)):
        for j in range(len(aoc[0])):
            try:
                if aoc[i][j] != "." and aoc[i][j] != "#": 
                    if keys[aoc[i][j]] != None:
                        keys[aoc[i][j]].append((i,j))
            except KeyError:
                keys[aoc[i][j]] = [(i,j)]

    for key,value in keys.items():
        opairs = generate_opairs(value)
        for opair in opairs:
            o1, o2 = opair
            total+=iterate(o1,o2,aoc,positions)

    return total

test = """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

ok = test.split("\n")
ok.pop(len(ok)-1)
ok.pop(0)
gwid = []
for i in ok:
    hi = []
    for j in i:
        hi.append(j)
    gwid.append(hi)

def print_grid(grid):
    for i in grid:
        for j in i:
            print(j, end=' ')
        print("")

print(part2(aoc))
print_grid(gwid)

