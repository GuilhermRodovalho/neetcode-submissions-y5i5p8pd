# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        sec = slow.next
        slow.next = None
        while sec:
            temp = sec.next
            sec.next=prev
            prev = sec
            sec = temp

        sec = prev
        first = head
        
        while sec:
            temp1, temp2 = first.next, sec.next
            
            first.next = sec
            sec.next=temp1
            first, sec = temp1, temp2

    
