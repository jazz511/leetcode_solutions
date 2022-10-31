# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l=[]
        while head:
            l.append(head.val)
            head = head.next
        return l == l[::-1]


lst=[1,2,3,2,1,5]
#last node
Node = ListNode(lst[-1],None)
# skip last node and reverse order
for i in lst[:-1][::-1]:
    Node = ListNode(i,Node)

A=Solution()
print(A.isPalindrome(Node))
