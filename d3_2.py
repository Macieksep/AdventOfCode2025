with open('resources/f3', 'r') as file:

    total = 0

    for l in file:

        l = l.strip()

        result = ''

        prev_i = -1

        while len(result) != 12:

            currMax = -1

            for i in range(prev_i+1, len(l)-(11-len(result))):

                now = l[i]

                if int(l[i]) > currMax:
                    currMax = int(l[i])
                    prev_i = i

            result += str(currMax)

        total += int(result)

    print(total)