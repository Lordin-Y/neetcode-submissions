# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #create dummy. dummy = ListNode(0,head)
        #create 2 pointers. First & Second
        #create for loop that makes 1 pointer increment n times
        #Now create the while loop that stops before the nth node from the end of the list
        #Remove the nth node
        dummy = ListNode(0,head)
        first = dummy
        second = dummy
        for i in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

        
        
        
            