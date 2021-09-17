# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mid_of_linklist(self, node):
        slow = node
        fast = node.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_linklist(self, node):
        prev = None
        cur = node
        while cur != None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev

    def reorderList(self, node: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        first = node
        mid = self.mid_of_linklist(node)
        second = mid.next
        mid.next = None
        second = self.reverse_linklist(second)
        head_node = first
        while first != None and second != None:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        return head_node
