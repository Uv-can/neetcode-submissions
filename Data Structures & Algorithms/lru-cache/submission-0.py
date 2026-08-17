# List Node for double linked list
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity #max length of cache
        self.cache = {} #map key to node

        self.left, self.right = Node(0,0), Node(0,0) #left and right node to put new nodes between
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self,node): # remove the LRU (node next to left)
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node): # insert MRU to second last (prev to right)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int: #get the value of key
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1


    def put(self, key: int, value: int) -> None: #add node to cache
        if key in self.cache:# remove cache if already available
            self.remove(self.cache[key]) 
        self.cache[key] = Node(key, value) 
        self.insert(self.cache[key]) #insert new node 

        if len(self.cache) > self.cap: #if cache full delete LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

