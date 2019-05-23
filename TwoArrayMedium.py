
'''
考察：两组list中的排序后的中位数
1.寻找一个数
'''


#解法一：每次记录最大的连续字符串，下次移动时需要头部和尾部两个指针一起动,for循环较为耗时O(n^2)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0;
        if (len(s) == 1):
            return 1;
        longestNum = comPareNow = 1;
        compareStart = 0;
        everylongestNum = 0;
        while (comPareNow < len(s) and compareStart <= comPareNow):
            everylongestNum = 1;
            for i in range(compareStart, comPareNow):
                if (s[i] != s[comPareNow]):
                    everylongestNum = everylongestNum + 1;
                    longestNum = max(everylongestNum, longestNum);
                else:
                    compareStart = i + 1;
                    break;
            comPareNow = comPareNow + 1;
        return longestNum;

