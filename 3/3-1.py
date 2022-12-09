total = 0

with open('3.txt') as sacks:
    for sack in sacks:
        temp = 0
        s1, s2 = sack.strip()[:len(sack.strip())//2], sack.strip()[len(sack.strip())//2:] #split string in half
        bad = []
        for i in range(len(s1)):
            if str(s1[i]) in s2:
                if s1[i] not in bad:
                    bad.append(s1[i])
        for c in bad:
            if ord(c) >= 97 and ord(c) <= 122: #a-z
                temp = temp + ord(c) - 96
            elif ord(c) >= 65 and ord(c) <= 90: #A-Z
                temp = temp + ord(c) - 38
        total = total + temp

print(total)
