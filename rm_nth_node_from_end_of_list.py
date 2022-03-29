"""
Remove Nth Node From End of List (LeetCode)

found at: https://leetcode.com/explore/interview/card/top-interview-questions-easy/93/linked-list/603/

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        # list with zero or one element
        if head.next == None or head == None:
            return None

        # find n-th element in list
        i = 0
        curr = head
        # tmp will stop right before the element that must be removed
        tmp = head
        # browse list till you find the tail
        while curr.next != None:
            if i+1 <= n:
                i += 1
            else:
                tmp = tmp.next
            curr = curr.next
        # if i < n, the head must be removed...
        if i < n:
            return head.next
        # ...otherwise, remove element after tmp (i.e., n-th element from tail)
        tmp.next = tmp.next.next
        return head
