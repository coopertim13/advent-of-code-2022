total = 0

f = open('3.txt', 'r')
lines = f.readlines()
for i in range(0, len(lines), 3):
    sacks = [lines[i].strip(), lines[i+1].strip(), lines[i+2].strip()]
    sorted_sacks = list(sorted(sacks, key = len, reverse = True))
    for j in range(len(sorted_sacks[0])):
        if sorted_sacks[0][j] in sorted_sacks[1] and sorted_sacks[0][j] in sorted_sacks[2]:
            if ord(sorted_sacks[0][j]) >= 97 and ord(sorted_sacks[0][j]) <= 122: #a-z
                total = total + ord(sorted_sacks[0][j]) - 96
            elif ord(sorted_sacks[0][j]) >= 65 and ord(sorted_sacks[0][j]) <= 90: #A-Z
                total = total + ord(sorted_sacks[0][j]) - 38
            break

print(total)