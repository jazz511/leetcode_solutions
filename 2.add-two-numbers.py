#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1,n2=[],[]
        node=l1
        while node:
            n1.append(str(node.val))
            node=node.next

        node=l2
        while node:
            n2.append(str(node.val))
            node=node.next
        
        num1=int("".join(n1[::-1]))
        num2=int("".join(n2[::-1]))
        sum=num1+num2
        #sum=str(sum)
        # node=next_node=None
        # for i in sum:
        #     node=ListNode(i, next_node)
        #     next_node=node

        sum=str(sum)[::-1]
        head=node=prev_node=ListNode()
        for i in sum:
            node.val=i
            prev_node.next=node
            prev_node=node
            node=ListNode()
        if head.next == head: head.next = None
        return head
# @lc code=end

