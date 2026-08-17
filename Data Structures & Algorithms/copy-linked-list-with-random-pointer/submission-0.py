"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {None:None}

        cur = head
        while cur:
            node = Node(cur.val)
            copy[cur] = node
            cur = cur.next
        
        curr = head
        while curr:
            node = copy[curr]
            node.next = copy[curr.next]
            node.random = copy[curr.random]
            curr = curr.next
        
        return copy[head]

