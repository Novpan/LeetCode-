'''
考察：贪心算法
'''

#解法一：暴力破解法
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height);
        if (length < 2):
            return 0;
        result = 0;
        secondList = [0]*length;
        maxList = secondList.copy();
        for i in range(1,length):
            for z in range(i):
                maxList[i] = 0;
                secondList[i] = 0;
                for j in range(z,length,i):
                    if(i + z > length-1):
                        continue;
                    if secondList[i] <= height[j]:
                        secondList[i] = height[j];
                    if maxList[i] <= secondList[i]:
                        temp = maxList[i];
                        maxList[i] = secondList[i];
                        secondList[i] = temp;
                    result = max(result, i * secondList[i]);
        return result;

#解法二：
 # * 贪心算法：从两边开始向中间缩小;每一步比较左右边界高度,高度小的那个向里走一步
 #     *
 #     * 这个贪心算法,为什么最优解不会被错过？         反证法 假设会被错过。
 #     *         假设最优解是横坐标为x1,x2(x2在右边)的这两个点组成的
 #     *               只考虑扫描到x2时,x1被错过的情况(x2被错过同理)：
 #     *         被错过指的是 当右指针向左扫描经过x2之后,左指针还在x1的左边P处时,x1被错过。
 #     *
 #     *                     情况一   x2>p:  x2会被保留,然后左指针向右移动到x1,x1不会被错过
 #     *                     情况二   x2<p:  小情况一：height[p]>height[x1]    则最优解为 p,x2而不是 x1,x2。  假设不成立
 #     *                                   小情况二：p<=x1  最优解还是p,x2。 假设不成立
 #     *                             //因为x2比p和x1都小,所以容器高度取决于x2,而p比x1偏左,所以p,x2比x1,x2面积大
 #     *
 #     *
 #     */

# 用h(i)
# 表示第i条线段的高度，S(ij)
# 表示第i条线段和第j条线段圈起来的面积。
#
# 可知
# h(0) < h(7)，从而S(07) = h(0) * 7。
#
# 有S(06) = min(h(0), h(6)) * 6。
# 当h(0) <= h(6)，有S(06) = h(0) * 6；
# 当h(0) > h(6)，有S(06) = h(6) * 6，S(06) < h(0) * 6。
#
# 由此可知，S(06)
# 必然小于S(07)。
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0;
        leftpoint,rightPoint=0,len(height) -1;
        while leftpoint < rightPoint :
            leftNum = height[leftpoint];
            righrNum = height[rightPoint];
            result = max(result, (rightPoint-leftpoint) * min(leftNum, righrNum))
            if leftNum <= righrNum :
                leftpoint +=1;
            else:
                rightPoint-=1;
        return result;