
'''
考察：最长字符串遍历
1.每次记录最大的连续字符串，下次移动时需要头部和尾部两个指针一起动
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

#解法二：每次记录最大的连续字符串，下次移动时需要头部和尾部两个指针一起动,使用in方式可以减少特别多耗时O(2n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if (len(s) == 0):
            return 0;
        if (len(s) == 1):
            return 1;
        longestNum = comPareNow = 1;
        compareStart = 0;
        while (comPareNow < len(s) and compareStart <= comPareNow):
            compareStr = s[compareStart:comPareNow];
            if (s[comPareNow] in compareStr):
                compareStart = compareStr.index(s[comPareNow]) + 1 + compareStart;
            comPareNow = comPareNow + 1;
            longestNum = max(longestNum, comPareNow - compareStart);
        return longestNum

#解法三：每次记录最大的连续字符串，下次移动时需要头部和尾部两个指针一起动,使用字典方式记录最近的一个相同的字符，这样可以减少起始位置的增加
    class Solution:
        def lengthOfLongestSubstring(self, s: str) -> int:
            dic, res, start, = {}, 0, 0
            for i, ch in enumerate(s):
                if ch in dic:
                    # update the res
                    res = max(res, i - start)
                    # here should be careful, like "abba"
                    start = max(start, dic[ch] + 1)
                dic[ch] = i
            # return should consider the last
            # non-repeated substring
            return max(res, len(s) - start)

