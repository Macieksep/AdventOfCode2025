file = open("resources/f1", "r")

curr = 50

passwd = 0

for i in file:

    currN = int(i[1:])

    if currN >= 100:
        currN -= 100 * (currN // 100)

    if i[0] == 'L':
        curr -= currN

        if curr < 0:
            curr += 100*(currN//100+1)
    else:
        curr += currN

        if curr > 99:
            curr -= 100*(currN//100+1)

    if curr == 0:
        passwd += 1

print(passwd)