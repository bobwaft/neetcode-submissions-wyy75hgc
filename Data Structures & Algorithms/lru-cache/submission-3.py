class DLL:
    def __init__(self,key=0,val = 0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.length = 0
        self.capacity = capacity
        self.head = None
        self.tail = None

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            if not node.next:
                return node.val
            else:
                self.moveToTail(node)
                return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if not self.head:
            self.head = DLL(key,value)
            self.tail = self.head
            self.hashmap[key] = self.head
            self.length += 1
        elif key in self.hashmap:
            node = self.hashmap[key]
            if node.next:
                self.moveToTail(node)
            node.val = value
        elif self.length < self.capacity:
            node = DLL(key,value)
            self.hashmap[key] = node
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.length += 1
        else:
            if not self.head.next:
                self.hashmap.pop(self.head.key)
                self.head = DLL(key,value)
                self.hashmap[key] = self.head
            else:
                self.head.next.prev = None
                self.hashmap.pop(self.head.key)
                self.head = self.head.next
                node = DLL(key,value)
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
                self.hashmap[key] = node

    def removeNode(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def moveToTail(self, node):
        if node == self.tail:
            return
        if node == self.head:
            self.head = node.next
            self.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        node.prev = self.tail
        node.next = None
        self.tail.next = node
        self.tail = node

