total = 0

with open('4.txt') as pairs:
    for pair in pairs:
        p = pair.strip()
        l1, l2 = int(p.split(",")[0].split("-")[0]), int(p.split(",")[0].split("-")[1])
        r1, r2 = int(p.split(",")[1].split("-")[0]), int(p.split(",")[1].split("-")[1])
        if (l1 <= r1 and l2 >= r2) or (r1 <= l1 and r2 >= l2):
            total = total + 1

print(total)