# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2 :
            return None
        
        multiplier = 1
        num1 = num2 = 0
        while l1 or l2:
            if l1:
                val1 = l1.val if l1 else 0
                num1 += val1 * multiplier
                l1 = l1.next
            if l2:
                val2 = l2.val if l2 else 0
                num2 += val2 * multiplier
                l2 = l2.next
            multiplier *= 10

        
        num3 = num1 + num2
        dummy = l3 = ListNode(0)
        
        if num3 == 0:
            return l3
        
        while num3 != 0:
            num = num3 % 10
            node = ListNode(num)
            l3.next = node
            l3 = l3.next
            num3 = num3 // 10
        
        return dummy.next
