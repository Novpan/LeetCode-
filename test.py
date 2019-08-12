from typing import List

fllist = ["ssow", "fl", "hg"]


def intToRoman(strss: List[str]) -> str:
    j = 0
    breakVal = False
    while True:
        if breakVal:
            break
        i = 0
        try:
            temp = strss[i][j]
            while i < len(strss):
                if temp != strss[i][j]:
                    breakVal = True
                    break
                else:
                    i = i + 1
            if breakVal:
                break
            j = j + 1
        except:
            breakVal = True
    if j < 1:
        return ''
    else:
        return fllist[0][:j]


print(intToRoman(fllist))
