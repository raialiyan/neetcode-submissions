# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # Base case - only work with lists of 3 or more nodes : 

        if not head or not head.next or not head.next.next : return

        # step 1 - Find middle of list : 
        slow = head 
        fast = head 

        while fast and fast.next : 
            slow = slow.next
            fast = fast.next.next # slow whill give us middle 

        # step 2 - Reverse second half : 
        curr = slow.next # current is start of second half 
        slow.next = None
        prev = None
        while curr :
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 

        back = prev
        front = head 

        # step 3 - interleave : 

        while back : 
            front_temp = front.next 
            back_temp = back.next 
            front.next = back 
            back.next = front_temp 
            front = front_temp 
            back = back_temp