aoc = []
with open("day4.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        arr = []
        for l in line:
            arr.append(l)
        
        aoc.append(arr)

def check_mas(aoc,i,j):
    total = 0
    if aoc[i+1][j+1] == "M" and aoc[i-1][j-1] == "S" and aoc[i-1][j+1] == "M" and aoc[i+1][j-1] == "S":
        total+=1
    if aoc[i+1][j+1] == "S" and aoc[i-1][j-1] == "M" and aoc[i-1][j+1] == "M" and aoc[i+1][j-1] == "S":
        total+=1
    if aoc[i+1][j+1] == "M" and aoc[i-1][j-1] == "S" and aoc[i-1][j+1] == "S" and aoc[i+1][j-1] == "M":
        total+=1
    if aoc[i+1][j+1] == "S" and aoc[i-1][j-1] == "M" and aoc[i-1][j+1] == "S" and aoc[i+1][j-1] == "M":
        total+=1
    
    return total

def find_x_mas(aoc):
    total = 0
    for i in range(1,len(aoc)-1):
        for j in range(1,len(aoc[7])-1):
            if aoc[i][j] == 'A':
                total+=check_mas(aoc,i,j)
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

print(find_x_mas(aoc))