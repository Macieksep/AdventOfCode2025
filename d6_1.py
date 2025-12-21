import re

nums = list()

with open("resources/f6", "r") as file:

    for l in file:
        nums.append(re.findall("[0-9*+]+", l))

results = []

for i in range(0, len(nums.__getitem__(0))):

    results.append(int(nums.__getitem__(0)[i]))

    for j in range(1, len(nums)-1):
        if nums.__getitem__(len(nums)-1)[i] == '+':
            results[i] += int(nums.__getitem__(j)[i])
        else:
            results[i] *= int(nums.__getitem__(j)[i])

print(sum(results))