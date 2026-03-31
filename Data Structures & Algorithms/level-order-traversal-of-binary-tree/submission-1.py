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
        q.append(root)

        res = []
        while q:
            q_len = len(q)
            current = []
            for i in range(q_len):
                n = q.popleft()
                if n:
                    current.append(n.val)
                    q.append(n.left)
                    q.append(n.right)
                
            if current:
                res.append(current)
            
        return res


        