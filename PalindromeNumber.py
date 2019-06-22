
'''
考察：回文字符串比较

'''

#解法一：反转后比较（相等就代表回文），需要处理边界条件
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            s = str(x);
            sre = s[::-1];
            if (s == sre):
                return True;
        return False;

#解法一：以中间为初始化值，往两边比较，不相等则为False
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x >= 0):
            s = str(x);
            isOdd = True;
            if (len(s) % 2) == 0:
                isOdd = False;
            mid = len(s) // 2;
            if isOdd:
                i = 1;
                while mid - i >= 0 and mid + i < len(s):
                    if s[mid - i] != s[mid + i]:
                        return False;
                    i += 1;
                return True;
            else:
                i = 0;
                while mid - i - 1 >= 0 and mid + i < len(s):
                    if s[mid - i - 1] != s[mid + i]:
                        return False;
                    i += 1;
                return True;
        return False;








