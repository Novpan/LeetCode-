#!/usr/local/bin/python3.6

'''
考察：数组遍历，遍历过程中记录中间过程值，减少反复遍历次数
1.可以采用轮询的方式，但是算法复杂度高O(n^2)
2.可以借助python字典或者java hashMap实现较快的二次检查过程
这里的二次检查指将前面检查过需要对比的数值保存在字典或者map中
测试中发现hashMap比字典的效率要高
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) < 2):
            print("invaild");
        searchHistoy = {};
        for i in range(len(nums)):
            if (nums[i] in searchHistoy.keys()):
                return [searchHistoy[nums[i]], i]
            else:
                searchHistoy[target - nums[i]] = i;
        print("not macth");
        return False;