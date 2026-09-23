# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        count = 0
        curr1= head
        while curr1:
            count += 1
            curr1 = curr1.next
        
        count = count - n
        count2 = 0
        dummy.next = head
        curr2 = dummy
        while curr2:
            if count2 == count:
                curr2.next = curr2.next.next
                
            curr2 = curr2.next
            count2 += 1  
            
        return dummy.next
        