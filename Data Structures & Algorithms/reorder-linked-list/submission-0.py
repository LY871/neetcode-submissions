# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finding middle of list 
        slow=head
        fast=head
        ret=ListNode()
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        # reverse after middle
        prev=None
        curr=slow.next
        slow.next=None
        while curr:
            nextnode=curr.next
            curr.next=prev
            prev=curr
            curr=nextnode
        first=head
        second=prev
        while second:
            tmp1=first.next
            tmp2=second.next

            first.next=second
            second.next=tmp1
            first=tmp1
            second=tmp2
        
        


        



