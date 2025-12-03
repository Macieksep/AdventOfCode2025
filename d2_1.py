def is_correct(num) -> bool:

    if len(num) % 2 == 0:
        if num[:len(num) // 2] == num[len(num) // 2:]:
            return False

    return True

rgs = (
        open("resources/f2_1", "r")
       .read()
       .split(',')
       )

result = 0

for rg in rgs:

    rgBorder = rg.split('-')

    for numId in range(int(rgBorder[0]), int(rgBorder[1])+1):
        if not is_correct(str(numId)):
            result += numId

print(result)