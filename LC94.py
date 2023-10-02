# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        stack = []
        res = []
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack: # if here, curr is None!
                temp = stack.pop()
                res.append(temp.val)
                curr = temp.right
            else:
                return res
                
