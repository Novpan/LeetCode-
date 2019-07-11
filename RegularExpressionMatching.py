
'''
考察：回文字符串比较

'''

#解法一：递归
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # 在python中 None,  False, 空字符串"", 0, 空列表[], 空字典{}, 空元组()都相当于False
        if len(p) == 0 :
            return len(s) == 0;
        # 代表第一个数是否命中.或者s的第一位
        firstmatch = False;
        if len(s) >= 1 :
            firstmatch = p[0] in {'.',s[0]};
        if len(p) >= 2 and p[1] == '*':
            # 第一个数匹配上，比较后面的数与模式匹配，否则直接跳过
            return (firstmatch and self.isMatch(s[1:],p)) or (self.isMatch(s, p[2:])) ;
        # 第二个数不是*
        else:
            # 第一个数匹配上，比较后面的数与模式匹配，否则直接跳过
            if firstmatch :
                return self.isMatch(s[1:],p[1:]);
            else:
                return firstmatch;

#解法二：递归二
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # bad case
        if len(p) == 0:
            if len(s) == 0:
                return True;
            else:
                return False;
        if len(s) == 0:
            if len(p) == 0:
                return True;
            if len(p) > 1 and p[1] == '*':
                return self.isMatch(s, p[2:]);
            else:
                return False;
        # Recursive
        if len(p) > 1 and p[1] == '*':
            if p[0] in {s[0], '.'}:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:]);
            else:
                return self.isMatch(s, p[2:]);
        else:
            if p[0] in {s[0], '.'}:
                return self.isMatch(s[1:], p[1:]);
            else:
                return False;

#解法三：动态规划(时间复杂度为O(TP)，空间复杂度O(TP))
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {};
        def dpdpdp(text:str,patter:str):
            if (len(text),len(patter)) in memo :
                return memo[len(text),len(patter)];
            # bad case
            if len(patter) == 0 and len(text) == 0 :
                memo[len(text), len(patter)] = True;
                return memo[len(text), len(patter)];
            if len(patter) == 0:
                if len(text) > 0 :
                    memo[len(text), len(patter)] = False;
                    return memo[len(text), len(patter)];
            if len(text) == 0 :
                if len(patter) > 1 and patter[1] == '*' :
                    memo[len(text), len(patter)] = dpdpdp(text,patter[2:])
                else:
                    memo[len(text), len(patter)] = False;
                return memo[len(text), len(patter)];
            # # Recursive
            if len(patter) > 1 and patter[1] == '*' :
                if patter[0] in {'.',text[0]} :
                    memo[len(text), len(patter)] = dpdpdp(text,patter[2:]) or dpdpdp(text[1:],patter);
                    return memo[len(text), len(patter)];
                else:
                    memo[len(text), len(patter)] = dpdpdp(text, patter[2:]);
                    return memo[len(text), len(patter)];
            else:
                if patter[0] in {'.', text[0]}:
                    memo[len(text), len(patter)] = dpdpdp(text[1:], patter[1:]);
                    return memo[len(text), len(patter)];
                else:
                    memo[len(text), len(patter)] = False;
                    return memo[len(text), len(patter)];
        return dpdpdp(s,p);








