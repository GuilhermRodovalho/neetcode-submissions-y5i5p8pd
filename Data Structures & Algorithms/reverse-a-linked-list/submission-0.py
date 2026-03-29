# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = None
        next_node = head
        if not next_node:
            return None
        
        while next_node:
            temp = next_node.next
            next_node.next = current
            current = next_node
            next_node = temp
        
        return current
        
        