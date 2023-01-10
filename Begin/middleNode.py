# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):

        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Move the fast pointer twice as fast as the slow pointer
        # When the fast pointer reaches the end of the list, the slow pointer will be at the middle
        while fast and fast.next:
            value = slow
            slow = slow.next
            fast = fast.next.next

        # If the fast pointer has reached the end of the list, return the middle node
        # Otherwise, the list has an even number of nodes, so return the second middle node
        if not fast:
            return value.next
        else:
            return slow