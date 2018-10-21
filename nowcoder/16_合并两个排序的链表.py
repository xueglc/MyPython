# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
         
        res = head = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                head.next = pHead1
                pHead1 = pHead1.next
                 
            elif pHead1.val >= pHead2.val:
                head.next = pHead2
                pHead2 = pHead2.next
            head = head.next
        head.next = pHead1 or pHead2
         
        return res.next