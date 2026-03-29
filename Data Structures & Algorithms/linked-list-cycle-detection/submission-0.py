# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow, fast = head, head.next
    
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast and fast.next:
                fast = fast.next
            else:
                return False
        
        return True