import pandas as pd

#prepare stacks, place in list
stacks = pd.read_fwf("stacks.txt", header=None)
stacklist1 = stacks.T.to_numpy().tolist()
stacks_final = []
i = 0
for stack in stacklist1:
    stacks_final.append([])
    for item in stack:
        if not pd.isna(item) and not item.isnumeric():
            stacks_final[i].append(item[1:2])
    i+=1

#modify stacks according to instructions
instruct = open('instructions.txt', 'r')
instructions = instruct.readlines()
for task in instructions:
    t = task.strip()
    howmany = int(t[t.find("move ")+len("move "):t.rfind(" from")])
    source = int(t[t.find("from ")+len("from "):t.rfind(" to")])
    dest = int(t[t.find("to ")+len("to "):t.rfind("")])
    while howmany > 0:
        stacks_final[dest-1].insert(0, stacks_final[source-1][howmany-1]) #change here
        stacks_final[source-1].pop(howmany-1) #change here
        howmany -= 1

for stack in stacks_final:
    print(stack[0][0], end="")