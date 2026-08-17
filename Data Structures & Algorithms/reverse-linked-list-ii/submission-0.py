# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy  = ListNode(0)
        dummy.next = head
        prev = dummy

        for _ in range(left-1):
            prev = prev.next

        sub_head = prev.next
        sub_tail = sub_head

        for _ in range(right-left):
            sub_tail = sub_tail.next
        
        next_node = sub_tail.next
        sub_tail.next = None
        reverse_list = sub_head
        old = None
        while reverse_list:
            tmp = reverse_list.next
            reverse_list.next = old
            old = reverse_list
            reverse_list = tmp
        
        prev.next = old
        sub_head.next = next_node

        return dummy.next


            