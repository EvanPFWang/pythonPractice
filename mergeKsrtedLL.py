import math
# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # different sizes
        # being disprop
        if  len(lists)  <=  2:
            if len(lists)   ==  2:
                return  lists.sorted(lists[0]   +   lists[1])
            else:
                return lists[0]
        else:
            lists   =   lists.sorted(lists, keys    =   lambda x: x[0]) #O(n log n)
            minimum = min([a[0].val for a in lists])
            layers  =   math.log(len(lists))+1    #2^k < len(lists)
            for pass1 in range(len(lists)//2):#odd indexes
                index = pass1*2 # sort pairs then delete the slot after with del() or remove()
                lists[index]    =   mergeKLists(lists[index],lists[index+1])
                lists[index+1]  =   None
            for pass2 in range(len(lists),-1,-1):#delete even slots or odd indexes
                index   =   pass2*2+1
                #find
            #mergesort

            curr = ListNode(minimum, None)

            full = [1 for a in lists]
            for a   == 1 in full:

            return full

        #def shorten(self, list: List[Optional[ListNode]]) -> Optional[ListNode]:
            list