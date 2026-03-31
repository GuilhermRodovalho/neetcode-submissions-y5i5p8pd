# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == q == None:
            return True
        if (p and not q) or (q and not p):
            return False

        stack = [(p, q)]
        while stack:
            tp, tq = stack.pop()

            if tp and tq and tp.val != tq.val:
                return False
            if (tp and not tq) or (not tp and tq):
                return False
            if not tp and not tq:
                continue
            stack.append((tp.left, tq.left))
            stack.append((tp.right, tq.right))
        
        return True
        