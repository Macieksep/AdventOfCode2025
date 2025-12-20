freshID = list()

resultID = list()

with open("resources/f5", "r") as file:
    for currLine in file:

        currLine = currLine.strip()

        if '-' in currLine:

            rangeID = currLine.split('-')

            freshID.append([int(rangeID[0]), int(rangeID[1]), 0])

        else:
            break

    freshID.sort()

    for i in range(len(freshID)):

        teraz = freshID[i]

        if freshID[i][2] == 1:
            continue

        currStart = freshID[i][0]

        for j in range(i+1, len(freshID)):
            if freshID[i][1] >= freshID[j][0]:
                freshID[j][2] = 1

                if freshID[i][1] < freshID[j][1]:
                    freshID[i][1] = freshID[j][1]

                if freshID[len(freshID)-1][2] == 1:
                    resultID.append(list([freshID[i][0], freshID[i][1]]))

            else:
                resultID.append(list([freshID[i][0], freshID[i][1]]))
                break

count = 0

for i in resultID:
    count += int(i[1]) - int(i[0])+1

print(count)