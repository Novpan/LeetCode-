
'''
考察：两组list中的排序后的中位数：考察抽象分组，以及二分法查找能力：通过抽象上下遍历指针
1.寻找一个数比其大和比其小的数相同，或者两个数比其大和比其小的数相差一个
2.考察抽象分组，以及二分法查找能力：通过抽象上下遍历指针，可以找到两个数组指针之间的关系j=(m+n+1)/2(偶数加1再除以2没关系)
3.边界的检查在a[i-1]<b[j],b[j-1]<a[i]中，遇到不满组条件的就跳过检查
'''
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 确认长短数组，以及长度
        shortList = nums1 if (len(nums1) <= len(nums2)) else nums2;
        longList = nums1 if (len(nums1) > len(nums2)) else nums2;
        shortLen = len(shortList);
        longLen = len(longList);
        # 对长的数组做有效判断
        if longLen == 0:
            return -1;
        leftShort = 0;
        rightShort = shortLen;
        if ((shortLen + longLen) % 2 == 0):
            isEvel = True;
        else:
            isEvel = False;
        # 对短数组空值做判断
        if(shortLen == 0):
            if isEvel:
                if(longLen == 1):
                    return longList[1];
                else:
                    return (longList[longLen//2 - 1] + longList[longLen//2]) / 2;
            else:
                 return longList[longLen//2];
        while (leftShort <= rightShort):
            mid = (leftShort + rightShort) // 2;
            currentLong = (shortLen + longLen + 1) // 2 - mid;
            # 当达到边界或者a[i-1]<b[j],b[j-1]<a[i] 有效时进行处理
            if ((mid == 0 or currentLong == longLen or shortList[mid - 1] <= longList[currentLong]) and (
                    mid == shortLen or currentLong == 0 or longList[currentLong - 1] <= shortList[mid])):
                # 对偶数奇书进行判断
                if (isEvel):
                    # 对边界和非边界进行判断
                    if (mid == 0):
                        if(currentLong==0):
                            print('>>> 1');
                            return min(shortList[mid],longList[currentLong]);
                        elif(currentLong==longLen):
                            print('>>> 2',shortList[mid - 1],shortList[mid]);
                            return (longList[currentLong - 1] + shortList[mid]) / 2;
                        else:
                            return (longList[currentLong - 1] + min(shortList[mid],longList[currentLong])) / 2;
                    elif (mid == shortLen):
                        if(currentLong==0):
                            print('>>> 3');
                            return (shortList[mid - 1] + longList[currentLong]) / 2;
                        elif(currentLong==longLen):
                            print('>>> 4');
                            return (max(shortList[mid - 1], longList[currentLong - 1]));
                        return (max(shortList[mid - 1], longList[currentLong - 1]) + longList[currentLong]) / 2
                    else:
                        print('>>> 5');
                        return (max(shortList[mid - 1], longList[currentLong - 1]) + min(shortList[mid],longList[currentLong])) / 2;
                else:
                    if (mid == 0):
                        if(currentLong==0):
                            return -1;
                        else:
                            return longList[currentLong - 1];
                    elif(currentLong==0):
                        return shortList[mid - 1];
                    else:
                        return max(shortList[mid - 1], longList[currentLong - 1]);
            elif (longList[currentLong - 1] > shortList[mid]):
                # 不满足条件时进行判断
                leftShort = mid + 1;
            elif (shortList[mid - 1] > longList[currentLong]):
                rightShort = mid - 1;
        return -1;






