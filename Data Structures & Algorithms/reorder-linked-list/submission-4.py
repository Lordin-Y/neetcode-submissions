# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle of the list using slow and fast 
        #actually split the 2 in half. Slow.next = None, slow_start = slow.next
        #create a reversed linked list for the 2nd half. second_start =
        #now merge the two lists together. first = head, second = prev.
        
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        prev = None
        
        while mid:
            temp = mid.next
            mid.next = prev
            prev = mid
            mid = temp
        sec_start = prev
        start = head
        while sec_start:
            temp1 = start.next
            temp2 = sec_start.next
            start.next = sec_start
            sec_start.next = temp1
            start = temp1
            sec_start = temp2

        return
        
        

