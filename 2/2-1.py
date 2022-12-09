score = 0

with open('2.txt') as plays:
    for play in plays:
        moves = play.strip().split(" ")
        if moves[1] == 'X':
            score = score + 1
            if moves[0] == 'A':
                score = score + 3
            if moves[0] == 'B':
                score = score + 0
            if moves[0] == 'C':
                score = score + 6
        if moves[1] == 'Y':
            score = score + 2
            if moves[0] == 'A':
                score = score + 6
            if moves[0] == 'B':
                score = score + 3
            if moves[0] == 'C':
                score = score + 0
        if moves[1] == 'Z':
            score = score + 3
            if moves[0] == 'A':
                score = score + 0
            if moves[0] == 'B':
                score = score + 6
            if moves[0] == 'C':
                score = score + 3

print(score)