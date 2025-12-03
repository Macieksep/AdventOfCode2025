# not done yet, some errors occurred ;)

def is_correct(num) -> bool:

    s = list()

    for i in range(0, len(num)-1):
        for j in range(1, len(num), 2):
            s.append(num[i:i+j+1])

    s = sorted(set(s), key=len)

    for i in s:
        if len(i) % 2 == 0:
            if i[:len(i)//2] == i[len(i)//2:]:
                return False

    return True

# rgs = (
#         open("resources/f2_1", "r")
#        .read()
#        .split(',')
#        )

rgs = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(',')

result = 0

for rg in rgs:

    rgBorder = rg.split('-')

    for numId in range(int(rgBorder[0]), int(rgBorder[1])+1):
        if not is_correct(str(numId)):
            print(numId)
            result += numId

print(result)