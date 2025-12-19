file = open("resources/f3", "r")

sum = 0

for line in file:

    maxV = 0

    for i in range(0, len(line)-2):
        for j in range(i+1, len(line)-1):

            curr = int(line[i])*10 + int(line[j])

            if curr > maxV:
                maxV = curr

    sum += maxV

print(sum)