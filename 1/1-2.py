biggest = []
tempbiggest = 0

with open('1.txt') as list:
    for calorie in list:
        if len(calorie) > 1:
            tempbiggest = tempbiggest + int(calorie.strip())
        else:
            biggest.append(tempbiggest)
            tempbiggest = 0

biggest.sort(reverse=True)
print(biggest[0] + biggest[1] + biggest[2])