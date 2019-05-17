
'''
考察：list遍历，list合并；节点保存和遍历
1.根节点注意保存，算法复杂度高O(n)
2.最后一位可能会进位
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 != None and l2 != None):
            head = ListNode(l1.val + l2.val);
            head.next = None;
            headStart = head;
        else:
            if (l1 == None):
                headStart = l2;
                return headStart;
            else:
                headStart = l1;
                return headStart;
        l1 = l1.next;
        l2 = l2.next;
        while (l1 != None and l2 != None):
            nextNode = ListNode(l1.val + l2.val);
            nextNode.next = None;
            head.next = nextNode;
            head = nextNode;
            l1 = l1.next;
            l2 = l2.next;
        if (l1 == None):
            if (l2 != None):
                head.next = l2;
        if (l2 == None):
            if (l1 != None):
                head.next = l1;

        headResult = headStart;

        overflow = 0;
        while (headStart != None):
            print('begin');
            overflow = 0;
            if (headStart.val >= 10):
                headStart.val = headStart.val - 10;
                overflow = 1;
            tempHeadStart = headStart;
            headStart = headStart.next;
            if (headStart != None):
                headStart.val = headStart.val + overflow;
            else:
                if (overflow == 1):
                    tempHeadStart.next = ListNode(overflow);

        return headResult;

