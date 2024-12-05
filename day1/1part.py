l1 = []
l2 = []

with open("day1.txt", "r") as f:
    lines = f.readlines() 
    for l in lines:
        l1.append(int(l.split('  ')[0]))
        l2.append(int(l.split('  ')[1]))

l1.sort()
l2.sort()

sum = 0
for i in range(0, len(l1)):
    sum+=abs(l1[i]-l2[i])

print(sum)

