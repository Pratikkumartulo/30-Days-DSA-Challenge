
'''Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.'''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr = head
        temp = []
        prev = None
        while(ptr):      
            if ptr.val not in temp:
                temp.append(ptr.val)
                prev = ptr
                ptr = ptr.next
            else:
                prev.next = ptr.next
                ptr = ptr.next
        return head
                