result_nums = set()

with open('resources/f2', 'r') as file:
    element = file.readline().strip().split(',')

    ranges = list()

    for e in element:
        ranges.append(e.split('-'))

    for r in ranges:
        for num in range(int(r[0]), int(r[1])+1):

            num = str(num)

            for i in range(2, len(num)+1):
                if len(num) % i == 0:
                    if num == num[:len(num)//i]*i:
                        result_nums.add(num)

result = 0

for i in result_nums:
    result += int(i)

print(result)