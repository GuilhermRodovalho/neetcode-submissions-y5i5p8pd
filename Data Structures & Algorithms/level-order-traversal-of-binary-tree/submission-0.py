# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque()
        q.append([root])

        res = []
        while q:
            this_level = q.popleft()
            res.append([n.val for n in this_level])

            current = []
            for n in this_level:
                if n:
                    if n.left:
                        current.append(n.left)
                    if n.right:
                        current.append(n.right)
            
            if current:
                q.append(current)

            
        return res


        