#the only thing I need to run this is NASA PC :(
freshID = set()

count = 0

with open("resources/f5_1", "r") as file:
    for currLine in file:

        currLine = currLine.strip()

        if '-' in currLine:

            rangeID = currLine.split('-')



            freshID.update(range(int(rangeID[0]), int(rangeID[1])+1))

            print("ok")

        else:
            break

print(len(freshID))