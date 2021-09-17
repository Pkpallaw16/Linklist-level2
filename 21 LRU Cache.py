class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class Double_linklist:
    def __init__(self,head=None,tail=None,size=0):
        self.head=head
        self.tail=tail
        self.size=size
    def addLast(self,node):
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail = node
            self.size+=1
    def removeFirst(self):
        if self.size==1:
            self.head = self.tail = None
        else:
            self.head=self.head.next
            self.head.prev=None
        self.size-=1
    def removenode(self,node):
        if self.size==1:
            self.head=self.tail=None
        elif self.head==node:
            self.head=node.next
            self.head.prev=None
        elif self.tail==node:
            self.tail=self.tail.prev
            self.tail.next=None
        else:
            pre_node=node.prev
            next_node=node.next
            pre_node.next=next_node
            next_node.prev=pre_node
        self.size -= 1
class LRUCache:
    def __init__(self, capacity: int):
        self.qu_map = {}
        self.cap=capacity
        self.dll=Double_linklist()
    def get(self, key: int) -> int:
        if key in self.qu_map.keys():
            node = self.qu_map[key]
            self.dll.removenode(node)
            self.dll.addLast(node)
            return node.value
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.qu_map.keys():
            node=self.qu_map[key]
            node.value=value
            self.dll.removenode(node)
            self.dll.addLast(node)
        elif self.dll.size<self.cap:
            node=Node(key,value)
            self.qu_map[key]=node
            self.dll.addLast(node)
        else:
            removal_key=self.dll.head.key
            del self.qu_map[removal_key]
            self.dll.removeFirst()
            node=Node(key,value)
            self.dll.addLast(node)
            self.qu_map[key]=node 

lRUCache = LRUCache(2);
lRUCache.put(1, 1) #cache is {1=1}
lRUCache.put(2, 2) # cache is {1=1, 2=2}
lRUCache.get(1)    # return 1
lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)   # returns -1 (not found)
lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)   # return -1 (not found)
lRUCache.get(3)    # return 3
lRUCache.get(4)

