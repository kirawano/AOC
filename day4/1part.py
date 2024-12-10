aoc = []
with open("day4.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        arr = []
        for l in line:
            arr.append(l)
        
        aoc.append(arr)

def find_mas(x, i, j):
    valmap = {
        0:"X",
        1:"M",
        2:"A",
        3:"S"
    }
    total = 0
    #up
    check = 0
    for k in range(4):
        if x[i-k][j] == valmap[k]:
            check+=1
        if check==4:
            total+=1 
    #down
    check = 0
    for k in range(4):
        if x[i+k][j] == valmap[k]:
            check+=1
        if check == 4:
            total+=1
    #right
    check = 0
    for k in range(4):
        if x[i][j+k] == valmap[k]:
            check+=1
        if check == 4:
            total+=1
    #left
    check = 0
    for k in range(4):
        if x[i][j-k] == valmap[k]:
            check+=1
        if check == 4:
            total+=1
    #diags
    check1 = 0
    check2 = 0
    check3 = 0
    check4 = 0
    #JANK SUPREME
    for k in range(4):
        if x[i+k][j+k] == valmap[k]:
            check1+=1
        if x[i+k][j-k] == valmap[k]:
            check2+=1
        if x[i-k][j+k] == valmap[k]:
            check3+=1
        if x[i-k][j-k] == valmap[k]:
            check4+=1
        if check1 == 4:
            total+=1
        if check2 == 4:
            total+=1
        if check3 == 4:
            total+=1
        if check4 == 4:
            total+=1
    return total

def find_xmas(aoc):
    total = 0
    for i in range(4,len(aoc)-3):
        for j in range(4,len(aoc[5])-3):
            if aoc[i][j] == "X":
                total+=find_mas(aoc, i, j)

    return total

test = """
000000000000000000
000000000000000000
000000000000000000
000000000000000000
0000MMMSXXMASM0000
0000MSAMXMSMSA0000
0000AMXSXMAAMM0000
0000MSAMASMSMX0000
0000XMASAMXAMM0000
0000XXAMMXXAMA0000
0000SMSMSASXSS0000
0000SAXAMASAAA0000
0000MAMMMXMMMM0000
0000MXMXAXMASX0000
000000000000000000
000000000000000000
000000000000000000
000000000000000000
"""
arr = test.split("\n")
arr.pop(len(arr)-1)
gwid = []
for i in arr:
    temp = []
    for j in i:
        temp.append(j)
    gwid.append(temp)
print(find_xmas(aoc))
