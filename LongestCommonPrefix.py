#Write a function to find the longest common prefix string amongst an array of strings. 
#
# If there is no common prefix, return an empty string "". 
#
# Example 1: 
#
# 
#Input: ["flower","flow","flight"]
#Output: "fl"
# 
#
# Example 2: 
#
# 
#Input: ["dog","racecar","car"]
#Output: ""
#Explanation: There is no common prefix among the input strings.
# 
#
# Note: 
#
# All given inputs are in lowercase letters a-z. 
#
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        j = 0
        breakVal = False
        while True:
            if breakVal:
                break
            i = 0
            try:
                temp = strs[i][j]
                while i < len(strs):
                    if temp != strs[i][j]:
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
            return strs[0][:j]