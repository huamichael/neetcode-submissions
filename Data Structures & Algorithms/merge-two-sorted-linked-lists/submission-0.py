# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        head = node
        while list1 and list2:
            if list1.val > list2.val: #if list2 smaller
                node.next = list2 #node points to list node
                list2 = list2.next #list goes to next
            else: #if list1 smaller
                node.next = list1
                list1 = list1.next
            node = node.next #move to next
        if not list1:
            node.next = list2
        if not list2:
            node.next = list1
        return head.next