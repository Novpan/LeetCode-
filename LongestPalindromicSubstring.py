
'''
参考资料：https://www.felix021.com/blog/read.php?2040
考察： 字符串遍历、拉马车算法、字符串以中心节点进行两边扩展
'''
from typing import List


class Solution:
    class Solution:
        def longestPalindrome(self, preS):
            # 添加分割字符
            s = '#' + '#'.join(preS) + '#';
            length = len(s);
            # right max vaule
            maxRight = 0;
            # right max vaule Palindrome pos
            pos = 0;
            RL = [0] * length
            for i in range(length):
                if (i < maxRight):
                    # 根据当前maxRight 与 i之间的值得出RL[i]的值
                    if (maxRight - i > RL[pos * 2 - i]):
                        RL[i] = RL[pos * 2 - i];
                    else:
                        RL[i] = maxRight - i;
                else:
                    # 根据当前maxRight不超出i时，说明此时i比maxRight要大，直接设置为1
                    RL[i] = 1;
                # try extented 当前的 i
                while (i + RL[i] < length and s[i - RL[i]] == s[i + RL[i]]):
                    RL[i] += 1;
                # 更新MaxRight,pos
                if i + RL[i] - 1 > maxRight:
                    maxRight = i + RL[i] - 1;
                    pos = i;
            # 更新最长回文串的长度
            maxLen = max(RL)
            idx = RL.index(maxLen)
            sub = s[idx - maxLen + 1: idx + maxLen]
            return sub.replace('#', '');






