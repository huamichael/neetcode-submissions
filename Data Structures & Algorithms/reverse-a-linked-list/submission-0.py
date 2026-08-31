# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head #2 ptrs
        while curr != None:
            nxt = curr.next #temp
            curr.next = prev #ptr to None
            prev = curr #ptr to curr
            curr = nxt #ptr to next
        return prev
