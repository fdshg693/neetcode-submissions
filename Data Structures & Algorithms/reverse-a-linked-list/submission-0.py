# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cursor = None        
        while head:
            if not cursor:
                node = ListNode(head.val)
                cursor = node
            else:
                node = ListNode(head.val)
                node.next = cursor
            cursor = node
            head = head.next
        return cursor
            
        