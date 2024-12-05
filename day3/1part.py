import re
L = []
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


# mul(1,3)
total = 0
for line in L:
    lis = re.findall(r'mul\(\d{1,3},\d{1,3}\)', line)
    for exp in lis:
        total+=mul(exp)

print(total)




