LI = []
with open("day2.txt", "r") as f:
    lines = f.readlines()
    for L in lines:
        b = []
        for a in L.split(' '):
            b.append(int(a))
        LI.append(b)
print(LI)

def strictly_increasing(x):
    for i in range(1, len(x)):
        if x[i] <= x[i-1]:
            return False
    return True

    return True
def strictly_decreasing(x):
    for i in range(1, len(x)):
        if x[i] >= x[i-1]:
            return False 
    return True
def is_safe(x):
    for i in range(1, len(x)):
        if abs(x[i] - x[i-1]) > 3 or abs(x[i] - x[i-1]) < 1:
            return False

    if strictly_increasing(x) or strictly_decreasing(x):
        return True
    return False

total = 0
for sample in LI:
    if is_safe(sample):
        total+=1

print(total)
