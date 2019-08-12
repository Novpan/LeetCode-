'''
考察：就是遍历
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        class Solution:
            def intToRoman(self, num: int) -> str:
                if (num < 0 or num > 3999):
                    return 0;
                four, nine, fourTy, nineTy, fourhundred, ninehundred = 'IV', 'IX', 'XL', 'XC', 'CD', 'CM'
                one, five, ten, fifty, onehundred, fivehundred, thoundred = 'I', 'V', 'X', 'L', 'C', 'D', "M"
                result, numList = '', []
                numStr = str(num)
                for i in range(len(numStr) - 1, -1, -1):
                    numList.insert(0, int(numStr[i]) * (10 ** (len(numStr) - 1 - i)))
                for i in range(len(numList)):
                    if numList[i] >= 1000:
                        result = result + thoundred * (numList[i] // 1000)
                    elif numList[i] == 900:
                        result = result + ninehundred
                    elif numList[i] >= 500:
                        result = result + fivehundred + ((numList[i] - 500) // 100) * onehundred
                    elif numList[i] == 400:
                        result = result + fourhundred
                    elif numList[i] >= 100:
                        result = result + (numList[i] // 100) * onehundred

                    elif numList[i] == 90:
                        result = result + nineTy
                    elif numList[i] >= 50:
                        result = result + fifty + ((numList[i] - 50) // 10) * ten
                    elif numList[i] == 40:
                        result = result + fourTy
                    elif numList[i] >= 10:
                        result = result + (numList[i] // 10) * ten

                    elif numList[i] == 9:
                        result = result + nine
                    elif numList[i] >= 5:
                        result = result + five + (numList[i] - 5) * one
                    elif numList[i] == 4:
                        result = result + four
                    elif numList[i] >= 1:
                        result = result + (numList[i]) * one
                return result

