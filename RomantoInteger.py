'''
考察：对字符串从末尾忘头进行遍历，需要判断当前的前一个是否是I,X,C进行非0判断
'''

# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

class Solution:
    def romanToInt(self, numList: str) -> int:
        one, five, ten, fifty, onehundred, fivehundred, thoundred, four, nine, fourTy, nineTy, fourhundred, ninehundred \
            = 'I', 'V', 'X', 'L', 'C', 'D', "M", 'IV', 'IX', 'XL', 'XC', 'CD', 'CM'
        result = 0
        nextSkip = False
        for i in range(len(numList) - 1, -1, -1):
            if nextSkip:
                nextSkip = False
                continue
            if numList[i] == five:
                if i - 1 >= 0:
                    if numList[i - 1] == one:
                        result = result + 4
                        nextSkip = True
                        continue
                result = result + 5
                nextSkip = False
            elif numList[i] == ten:
                if i - 1 >= 0:
                    if numList[i - 1] == one:
                        result = result + 9
                        nextSkip = True
                        continue
                result = result + 10
                nextSkip = False
            elif numList[i] == fifty:
                if i - 1 >= 0:
                    if numList[i - 1] == ten:
                        result = result + 40
                        nextSkip = True
                        continue
                result = result + 50
                nextSkip = False
            elif numList[i] == onehundred:
                if i - 1 >= 0:
                    if numList[i - 1] == ten:
                        result = result + 90
                        nextSkip = True
                        continue
                result = result + 100
                nextSkip = False
            elif numList[i] == fivehundred:
                if i - 1 >= 0:
                    if numList[i - 1] == onehundred:
                        result = result + 400
                        nextSkip = True
                        continue
                result = result + 500
                nextSkip = False
            elif numList[i] == thoundred:
                if i - 1 >= 0:
                    if numList[i - 1] == onehundred:
                        result = result + 900
                        nextSkip = True
                        continue
                result = result + 1000
                nextSkip = False
            elif numList[i] == one:
                result = result + 1
                nextSkip = False
        return result

