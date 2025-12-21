with open('resources/f6', 'r') as file:

    content = list()

    l_max = 4

    for i in file:
        content.append(i.replace('\n', ''))

    chars = list()

    for c in content[len(content)-1]:
        if not ' ' in c:
            chars.append(c)

    line_max = 0

    for i in content:
        if len(i) > line_max:
            line_max = len(i)

    for i in range(len(content)):
        if len(content[i]) < line_max:
            content[i] += ' '*(line_max - len(content[i]))

    nums = list()

    for X in range(line_max):

        tmp_nums = list()

        num = ''

        for Y in range(l_max):
            num += content[Y][X]

        nums.append(num)

    nums.append(' ')

    counter = 0

    result = 0

    tmp_res = 0

    for n in nums:

        if n.isspace():

            result += tmp_res

            counter += 1

            if counter == len(chars):
                break
            elif chars[counter] == '+':
                tmp_res = 0
            else:
                tmp_res = 1

        elif chars[counter] == '+':
            tmp_res += int(n)
        elif chars[counter] == '*':
            tmp_res *= int(n)

    print(result)