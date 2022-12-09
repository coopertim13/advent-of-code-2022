biggest = 0
tempbiggest = 0

with open('1.txt') as list:
    for calorie in list:
        if len(calorie) > 1:
            tempbiggest = tempbiggest + int(calorie.strip())
        else:
            if tempbiggest > biggest:
                biggest = tempbiggest
            tempbiggest = 0

print(biggest)