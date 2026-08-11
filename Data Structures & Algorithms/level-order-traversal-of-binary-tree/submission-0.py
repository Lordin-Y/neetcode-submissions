# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return []         
        queue = deque([root])     
        while queue:
            level_size = len(queue)
            current_level = []
            
            for i in range(level_size):
                node = queue.popleft()#pop one node from the FRONT of the queue
                current_level.append(node.val)#record its value into current_level
                if node.left:#if it has a left child, push it to the BACK of the queue
                    queue.append(node.left)
                if node.right:#if it has a right child, push it to the BACK of the queue
                    queue.append(node.right)
            #add current_level to result
            result.append(current_level)
        return result