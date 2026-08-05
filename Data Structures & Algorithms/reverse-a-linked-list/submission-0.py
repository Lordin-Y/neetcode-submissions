# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        temp = None
        while curr:
            temp = curr.next              # step 1
            curr.next = prev          # step 2
            prev = curr                # step 3
            curr = temp                  # step 4
        return prev


