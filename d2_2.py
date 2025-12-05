# not done yet, some errors occurred ;)

def is_correct(num) -> bool:

    num = str(123123123)

    for l in range(1, len(num)):
        if int(num) % l == 0:

            matchSeq = num[:l]

            for i in range(0, len(num)//l):
                if matchSeq != num[i*l:(i+1)*l]:
                    break

    return False

rgs = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124".split(',')

result = 0

for rg in rgs:

    rgBorder = rg.split('-')

    for numId in range(int(rgBorder[0]), int(rgBorder[1])+1):
        if not is_correct(str(numId)):
            print(numId)
            result += numId

print(result)