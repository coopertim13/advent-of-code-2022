score = 0

with open('2.txt') as plays:
    for play in plays:
        moves = play.strip().split(" ")
        if moves[1] == 'X': #lose
            if moves[0] == 'A': #opponent chooses rock, need scissors
                score = score + 3 + 0
            if moves[0] == 'B': #opponent chooses paper, need rock
                score = score + 1 + 0
            if moves[0] == 'C': #opponent chooses scissors, need paper
                score = score + 2 + 0
        if moves[1] == 'Y': #draw
            if moves[0] == 'A': #opponent chooses rock, need rock
                score = score + 1 + 3
            if moves[0] == 'B': #opponent chooses paper, need paper
                score = score + 2 + 3
            if moves[0] == 'C': #opponent chooses scissors, need scissors
                score = score + 3 + 3
        if moves[1] == 'Z': #win
            if moves[0] == 'A': #opponent chooses rock, need paper
                score = score + 2 + 6
            if moves[0] == 'B': #opponent chooses paper, need scissors
                score = score + 3 + 6
            if moves[0] == 'C': #opponent chooses scissors, need rock
                score = score + 1 + 6

print(score)