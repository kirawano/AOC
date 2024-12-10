import itertools
aoc = []
with open("input.txt","r") as f:
    lines = f.read().split("\n")
    lines.pop(len(lines) - 1)
    for l in lines:
        wow = l.split(": ")
        hi = []
        for i in wow[1].split(" "):
            if i != '':
                hi.append(int(i))
        aoc.append((int(wow[0]),hi)) 

def mulfull(x):
    total = 1
    for i in x:
        total*=i
    return total

def mul(x,y):
    return x*y
def add(x,y):
    return x+y
def concatenate(x,y):
    return int(str(x)+str(y))
ops = {
    0: mul,
    1: add,
    2: concatenate
        }

def parsenums(x, op):
    total = x[0]
    for i in range(1,len(x)):
        total = ops[op[i-1]](total, x[i])

    return total

def part1(aoc):
    total = 0
    for eq in aoc:
        val, nums = eq
        for p in itertools.product([0,1], repeat=len(nums)-1):
            print(str(parsenums(nums,p)) + ": "+str(val))
            print(p)
            if parsenums(nums, p) == val:
                total+=val
                break
    return total

def part2(aoc):
    total = 0
    for eq in aoc:
        val, nums = eq
        for p in itertools.product([0,1,2], repeat=len(nums)-1):
            if parsenums(nums,p) == val:
                total+=val
                break
    return total

test = """
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
gwid = []
lis = test.split("\n")
lis.pop(0)
lis.pop(len(lis) - 1)
for i in lis:
    ok = i.split(": ")
    seriously = ok[1].split(" ")
    two = [int(j) for j in seriously]
    one = int(ok[0])

    gwid.append((one,two))

#for p in itertools.product([0,1], repeat=2):
#   print(p)
#   print(parsenums([1,2,3],p))

with open("output","w") as f:
    f.write(str(part2(gwid))+"\n")

