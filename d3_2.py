#Code under construction :)

file = open("resources/f3_1", "r")

sum = 0

for line in file:

    line = line.strip()

    num = 0

    for dig in range(0, 12):

        currentMaxPos = 0 + dig
        currentMax = 0

        for i in range(currentMaxPos, len(line)-(12-dig)):
            if int(line[i]) > currentMax:
                currentMax = int(line[i])
                currentMaxPos = i

        num += currentMax * pow(10, 12-dig)

    print(num)

print(sum)