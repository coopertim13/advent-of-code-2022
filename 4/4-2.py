total = 0

with open('4.txt') as pairs:
    for pair in pairs:
        p = pair.strip()
        p1 = []
        for i in range(int(p.split(",")[0].split("-")[0]), int(p.split(",")[0].split("-")[1]) + 1, 1):
            p1.append(i)
        p2 = []
        for i in range(int(p.split(",")[1].split("-")[0]), int(p.split(",")[1].split("-")[1]) + 1, 1):
            p2.append(i)
        for number in p1:
            if number in p2:
                total+=1
                break

print(total)