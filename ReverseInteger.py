
'''
考察：先记录字符串正负，反转字符串后，转换成整数，再乘以正负，得到数字
'''

class Solution:
    def reverse(self, x: int) -> int:
        IsNegative = False;
        if (x < 0):
            IsNegative = True;
            x = x * (-1);
        l = list(str(x))
        l.reverse()
        resultStr = "".join(l)
        result = int(resultStr);
        if (IsNegative):
            result = result * (-1);
        if (result <= -2 ** 31 or result >= 2 ** 31 - 1):
            return 0;
        return result;






