
'''
考察：链表遍历，链表合并；节点保存和遍历
1.根节点注意保存，算法复杂度高O(n)
2.最后一位可能会进位
'''



'''
解法一：先直接相加，相加完后再处理一遍进位过程
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



'''
解法二：相加过程中将多余的值直接进位保存
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow = 0;
        if (l1 != None and l2 != None):
            head = ListNode(l1.val + l2.val);
            head.next = None;
            overflow = head.val // 10;
            head.val = head.val % 10;
            headStart = head;
            templastNode = head;
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
            nextNode = ListNode(l1.val + l2.val + overflow);
            nextNode.next = None;
            head.next = nextNode;
            head = nextNode;
            overflow = head.val // 10;
            head.val = head.val % 10
            l1 = l1.next;
            l2 = l2.next;
            templastNode = head;
            print('sss1', templastNode.val)
        if (l1 == None):
            if (l2 != None):
                head.next = l2;
            if (overflow > 0):
                while (l2 != None):
                    l2.val = l2.val + overflow;
                    overflow = l2.val // 10;
                    l2.val = l2.val % 10;
                    templastNode = l2;
                    l2 = l2.next;
        if (l2 == None):
            if (l1 != None):
                head.next = l1;
            if (overflow > 0):
                while (l1 != None):
                    l1.val = l1.val + overflow;
                    overflow = l1.val // 10;
                    l1.val = l1.val % 10;
                    print(head.val)
                    templastNode = l1;
                    l1 = l1.next;

        if (overflow > 0):
            lastNode = ListNode(overflow);
            templastNode.next = lastNode;

        return headStart;

'''
解法三：；链表直接相加，多余的位数应0代替考虑
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next




