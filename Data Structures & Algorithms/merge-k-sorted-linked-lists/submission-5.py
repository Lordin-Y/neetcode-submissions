# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def mergeListNode(self, list1, list2):
        dummy = ListNode() 
        curr = dummy
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr2 = curr2.next
            curr = curr.next
        if curr1:
            curr.next = curr1
        else:
            curr.next = curr2
        return dummy.next
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #while loop that keeps running until there's one LL
        #For loop that merges 2 LL's together 
        #if i+1 < len(lists): then list2 = lists[i+1] else: None
        #mergeList.append(self.mergeListNode(list1,list2))
        #lists = mergeList
        #outer, return lists[0]

        if not lists:
            return None
        while len(lists) > 1:
            mergeList = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                if (i+1) < len(lists):
                    list2 = lists[i+1] 
                else:
                    list2 = None
                mergeList.append(self.mergeListNode(list1, list2))
            lists = mergeList
        return lists[0]

