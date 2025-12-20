# Y X
factoryMap = []

with open("resources/f4", "r") as f:
    for l in f:
        r = list(l.strip())
        factoryMap.append(r)

rolls = 0

for Y in range(len(factoryMap)):
    for X in range(len(factoryMap[Y])):

        if factoryMap[Y][X] == '@':

            count = -1

            # xxx
            #  o
            #

            for i in range(-1, 2):
                if Y-1 >= 0 and X+i >=0 and X+i < len(factoryMap[Y]):
                    if factoryMap[Y-1][X+i] == '@':
                        count += 1

            #
            #  o
            # xxx

            for i in range(-1, 2):
                if Y+1 < len(factoryMap) and X+i >=0 and X+i < len(factoryMap[Y]):
                    if factoryMap[Y+1][X+i] == '@':
                        count += 1

            #
            # xox
            #

            for i in range(-1, 2):
                if X+i >= 0 and X+i < len(factoryMap[Y]):
                    if factoryMap[Y][X+i] == '@':
                        count += 1

            if count < 4:
                rolls += 1

print(rolls)