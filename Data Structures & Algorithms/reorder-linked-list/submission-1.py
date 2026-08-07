# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of the list using slow and fast 
        #actually split the 2 in half. Slow.next = None, slow_start = slow.next
        #create a reversed linked list for the 2nd half
        #now merge the two lists together
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_start = slow.next
        slow.next = None
        prev = None
        while second_start:
            temp = second_start.next
            second_start.next = prev
            prev = second_start
            second_start = temp

        first = head
        second = prev
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        return 
        

