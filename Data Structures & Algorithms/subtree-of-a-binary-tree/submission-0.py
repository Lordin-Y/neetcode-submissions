# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    def isSameTree(self,p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        test_left = self.isSameTree(p.left, q.left)
        test_right = self.isSameTree(p.right, q.right)
        if p.val == q.val and test_left and test_right:
            return True
        else:
            return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSameTree(subRoot, root):
            return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)