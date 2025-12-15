file = open("resources/f1", "r")

curr = 50

clicks = 0

for i in file:

    skipClick = False

    print(i)

    currN = int(i[1:])

    if currN >= 100:
        clicks += (currN // 100)
        currN -= 100 * (currN // 100)

    if i[0] == 'L':

        curr -= currN

        if curr < 0:
            if curr + currN != 0:
                clicks += (currN//100+1)
                skipClick = True
            curr += 100*(currN//100+1)

    else:
        curr += currN

        if curr > 99:
            clicks += (currN//100+1)
            curr -= 100*(currN//100+1)
            skipClick = True

    if curr == 0 and skipClick == False:
        clicks += 1

print("\n",clicks)