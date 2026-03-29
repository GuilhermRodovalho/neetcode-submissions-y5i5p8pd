# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode(val=0)
        
        temp_list = new_list
        while list1 or list2:
            if not list1:
                while list2:
                    temp_list.next=list2
                    list2 = list2.next
                    temp_list = temp_list.next
                break
            if not list2:
                while list1:
                    temp_list.next=list1
                    list1=list1.next
                    temp_list = temp_list.next
                break

            if list1.val > list2.val:
                temp_list.next=list2
                list2 = list2.next
                temp_list = temp_list.next
            else:
                temp_list.next=list1
                list1=list1.next
                temp_list = temp_list.next

        return new_list.next 