# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # different sizes
        # being disprop
        minimum = min([a[0].val for a in lists])
        curr = ListNode(minimum, None)

        full = [1 for a in lists]
        for a   == 1 in full:

        return full

        def shorten(self, list: List[Optional[ListNode]]) -> Optional[ListNode]:
            list