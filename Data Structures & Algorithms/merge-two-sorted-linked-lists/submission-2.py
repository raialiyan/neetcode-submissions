# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy_node = ListNode()
        current = dummy_node 

        while list1 and list2 : 

            if list1.val < list2.val : 
                current.next = list1 # made connection dummynode  ------>  list1
                current = list1 # make the node of list1 the head now 
                list1 = list1.next # the value at list1 varibale for the next loop will be the value at next node in that list 
            else : 
                current.next = list2 # made connection dummynode  ------>  list2
                current = list2    # make the node of list2 the head now 
                list2 = list2.next # the value at list2 variable for the next loop will be the value at next node in that list 

            
        current.next = list1 if list1 else list2 # if there is either one list or no list at all

        return dummy_node.next # cause we were starting at dummynode and after that will be the entire sorted merged list 



        