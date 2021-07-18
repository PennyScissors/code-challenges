"""
Problem: 203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        curr = head
        dummy = prev = ListNode(0)
        dummy.next = head

        while curr:
            if curr.val == val:
                prev.next = curr.next
                curr.next = None
                curr = prev.next
            else:
                prev = curr
                curr = curr.next

        return prev.next

