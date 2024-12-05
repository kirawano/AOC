l1 = []
l2 = []
with open("day1.txt", "r") as f:
    lines = f.readlines() 
    for l in lines:
        l1.append(int(l.split('  ')[0]))
        l2.append(int(l.split('  ')[1]))

total = 0
for l in l1:
    t = 0
    for L in l2:
        if l == L:
            t+=1
    total+=(l*t)

print(total)

