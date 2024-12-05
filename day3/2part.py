L = []
import re
with open("day3.txt", "r") as f:
    lines = f.readlines() 
    for l in lines:
        L.append(l)


def mul(s):

    nums = re.findall(r'\d{1,3}', s)
    x = int(nums[0])
    y = int(nums[1])
    print(x)
    print(y)
    return x*y

total = 0
toggle = 1
for line in L:
    lis = re.findall(r'mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)', line)
    for exp in lis:
        if exp == "don't()":
            toggle=-1
        if re.match(r'mul\(\d{1,3},\d{1,3}\)', exp) != None and toggle != -1:
            total+=mul(exp)
        if exp == "do()":
            toggle=1


print(total)
