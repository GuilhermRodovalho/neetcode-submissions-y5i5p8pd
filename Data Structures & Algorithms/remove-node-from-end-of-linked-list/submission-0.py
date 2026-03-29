# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        r = head
        l = ListNode(next=head)
        head = l

        i = 0
        while r and i<n:
            r = r.next
            i+=1

        while r:
            r = r.next
            l = l.next

        print(l.val, l.next)

        tmp = l.next
        if tmp:
            tmp=tmp.next

        l.next=tmp
        return head.next
