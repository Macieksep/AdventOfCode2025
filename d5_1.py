freshID = []

count = 0

with open("resources/f5_1", "r") as file:
    for currLine in file:

        currLine = currLine.strip()

        if '-' in currLine:

            rangeID = currLine.split('-')

            freshID.append([int(rangeID[0]), int(rangeID[1])])

        elif currLine.isdigit():

            for start, end in freshID:
                if start <= int(currLine) <= end:
                    count += 1
                    break

print(count)