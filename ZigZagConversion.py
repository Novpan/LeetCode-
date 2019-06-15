
'''
考察：当前数组按照之型摆放：需要解决

'''
from typing import List


#解法一：思路，按竖直摆放该数组，然后将改数组依次按横向打印出来，算法复杂度为,打印出来的算法复杂度为O(n^2)
# 1.数组大小
# 2.数据摆放
# 3.依次打印数据
class Solution:
    def convert(self, s: str, num: int) -> str:
        le = len(s);
        if(le==0 or len ==1 or num==1):
            return s;
        # 首先确认数组
        tempcol = le // (2 * num - 2) * (num -1);
        leftcol = le % (2 * num - 2);
        if leftcol <= num and leftcol > 0:
            leftcol = 1;
        elif leftcol > num:
            leftcol = 1 + leftcol - num;
        col = tempcol + leftcol;
        myList = [([''] * col) for i in range(num)]
        # 其次按照数组依次摆数据
        for i in range(le):
            i = i+1;
            # 第几组数据
            curNumNo = i // (2* num - 2);
            # 具体数据数值
            curNum = i % (2* num - 2);
            if(curNum == 0):
                curNumNo -= 1;
            coll = curNumNo * (num -1);
            if(curNum <= num and curNum >0):
                roww = curNum;
                coll = coll + 1;
            elif(curNum > num):
                roww = 2* num - curNum;
                coll = coll + curNum - num + 1;
            elif curNum ==0:
                roww = 2;
                coll = coll + num - 1;
            myList[roww-1][coll-1] = s[i-1];
        result = '';
        # 最后循环打印数组即可
        for h in range(len(myList)):
            for k in range(len(myList[0])):
                result = result + myList[h][k];
        return result


#解法二：以每一行row为结果导向，找出每一行下标之间的规律，通过得到每一行第一个数值的下标，推断出改行所有的下标，时间复杂度为O(n)
class Solution:
    def convert(self, s: str, num: int) -> str:
        length = len(s);
        if num <=0:
            return ;
        if length <= num or num == 1:
            return s;
        result = '';
        for row in range(num):
            # 这里每一行的是差值[2*(num-1-row),2*row],其中当num =1 ，row = 0，row = num-1时需要特殊处理
            dValue = [2*(num - row - 1),row * 2];
            if dValue[0] == 0:
                dValue[0] = dValue[1];
            elif dValue[1] == 0:
                dValue[1] = dValue[0];
            curindex = row;
            result +=s[curindex];
            while(curindex<length):
                curindex = curindex + dValue[0];
                if(curindex<length):
                    result +=s[curindex];
                    curindex = curindex + dValue[1];
                    if(curindex<length):
                        result +=s[curindex];
                    else:
                        break;
                else:
                    break;
        return result;


#解法二（2.1）：还是解法2，通过调整一些常数的计算，提升速度到leetCode快速水平
class Solution:
    def convert(self, s: str, num: int) -> str:
        length = len(s);
        if num <=0:
            return ;
        if length <= num or num == 1:
            return s;
        result = '';
        indexDiff = 2*(num - 1);
        indexNum = num -1;
        for row in range(num):
            if row == 0 or row == indexNum:
                curindex = row;
                while(curindex<length):
                    result +=s[curindex];
                    curindex += indexDiff;
            else:
                rowNumTwo = 2*row;
                dValue = [indexDiff - rowNumTwo,rowNumTwo];
                curindex = row;
                result +=s[curindex];
                while(curindex<length):
                    curindex = curindex + dValue[0];
                    if(curindex<length):
                        result +=s[curindex];
                        curindex = curindex + dValue[1];
                        if(curindex<length):
                            result +=s[curindex];
                        else:
                            break;
                    else:
                        break;
        return result;


#解法三：遍历过程中保存将每一个数添加到对应的行数中，最终一起输出就行
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        # This is a vague sentence for python beginers
        L = [''] * numRows
        # it can be replaced by the following:
        # L = []
        # for i in range(0, numRows):
        #     L.append('')
        # so if numRows = 3, L = ['', '', '']
        index, step = 0, 1

        for x in s:
            L[index] += x
            #@1 start #
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            #@1 end  #
            # I like to explain the part above
            # take the str "PAYPALISHIRING" for example:
            # We start with variable index with the value 0, step with the value 1
            # Each row added with the next char
            # If we reach the bottommost row, we need to turn to the next above row, so we change the step value to -1
            # we keep the step value until we reach topmost row. DON'T CHANGE IT!
            # Again, if we reach the topmost row, we need to reset the step value to 1
            # What we need to remember is:
            # the zigzag pattern is just a pictorial image for us to have a better understanding
            # What the trick of algorithm is actually add the next char of the given string to different rows.
            # Don't really think how to move the cursor in the matrix.
            # It's really misleading way you think of this. Even it works, it's not efficient.
            index += step

        return ''.join(L)




