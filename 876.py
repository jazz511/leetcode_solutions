class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
    slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


lst=[1,2,3,4,5,6]
#last node
Node = ListNode(lst[-1],None)
# skip last node and reverse order
for i in lst[:-1][::-1]:
    Node = ListNode(i,Node)

print(Solution().middleNode(Node).val)
