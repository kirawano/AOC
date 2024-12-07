rules = []
pages = []
with open("day5.txt", "r") as f:
    lines = f.readlines()
    rule = True
    for line in lines:
        if line == "\n":
            rule = False
            continue
        elif rule and line != "\n":
            rules.append(line)
        elif line != "\n":
            pages.append(line)

def get_rules(rules):
    ret = []
    for rule in rules:
        rs = rule.split("|")
        if rule != "\n":
            ret.append((int(rs[0]),int(rs[1])))
    return ret
def get_updates(pages):
    ret = []
    for page in pages:
        hi = []
        pg = page.split(",")
        for p in pg:
            hi.append(int(p[:2]))
        ret.append(hi)
    return ret

def generate_opairs(x):
    ret = []
    for i in range(len(x)):
        for j in range(0, len(x)):
            if i > j:
                ret.append((int(x[i]), int(x[j])))
    return ret

def valid_update(rules, update):
    for X,Y in rules:
        if X in update and Y in update:
            if update.index(X)>update.index(Y):
                return (False, update.index(X), update.index(Y))
    return (True, 0, 0)

def part1(rs,pages):
    rules = get_rules(rs)
    updates = get_updates(pages)

    vals = []
    for update in updates:
        valid, doesnt, matter = valid_update(rules,update)
        if valid:
            vals.append(update)
    print(vals)

    total = sum(val[int(len(val)/2)] for val in vals)

    return total

def part2(rules, updates):
    vals = []
    for update in updates:
        val, doesnt, matter = valid_update(rules,update)
        if val:
            continue

        while True:
            valid, i1, i2 = valid_update(rules, update)
            if valid:
                vals.append(update)
                break
            temp = update[i2]
            update[i2] = update[i1]
            update[i1] = temp
            print(update)

    print(vals)

    total = sum(val[int(len(val)/2)] for val in vals)
    return total



    
    
    


rs=[(47,53),(97,13),(87,61),(97,47),(75,29),(61,13),(74,53),(29,13),(97,29),(53,29),(61,53),(97,53),(61,29),(47,13),(75,47),(97,75),(47,61),(75,61),(47,29),(7,13),(53,13)]
us=[[75,47,61,53,29],[97,61,53,29,13],[75,29,13],[75,97,47,61,53],[61,13,29],[97,13,75,29,47]]
print(part2(get_rules(rules), get_updates(pages)))
#print(part2(rs,us))
