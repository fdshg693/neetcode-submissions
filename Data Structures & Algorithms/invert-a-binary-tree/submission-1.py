# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        left = None
        right = None
        if not root:
            return None
        if root.left:
            left = root.left    
        if root.right:
            right = root.right

        answer = TreeNode(root.val)
        
        answer.right = self.invertTree(left)
        answer.left = self.invertTree(right)
        return answer
        