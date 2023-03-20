import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
    
    def __repr__(self):
        return f"[Node({self.val}) prev={self.prev.val if self.prev is not None else 'X'} next={self.next.val if self.next is not None else 'X'}]"

class LRUCache:

    def __init__(self, capacity: int):
        self.nodes = defaultdict(lambda: Node(-1))
        self.head = None
        self.tail = None
        self.len = 0
        self.cap = capacity

    def get(self, key: int) -> int:
        # print(f"Get {key=}")
        node = self.nodes[key]
        val = node.val
        if val == -1:
            return -1
        self.delete(node)
        # self.print()
        node.val = val
        self.insert(node)
        # self.print()
        return val
    
    def delete(self, node: Node):
        if node.val == -1:
            return
        # print(f"Deleting node : {node=}")
        if self.len == 1:
            node.prev = None
            node.next = None
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            node.next = None
            self.head.prev = None
        elif node == self.tail:
            self.tail = node.prev
            node.prev = None
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = None

        # if self.tail is None and self.head is not None:
        #     raise Exception(f"Inconsistent delete : {node=}, {self.head=}, {self.tail=}")
        self.len -= 1
        node.val = -1
    
    def insert(self, node: Node):
        self.len += 1
        if self.head is None:
            self.head = node
            self.tail = node
            node.prev = None
            node.next = None
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
            node.next = None

        # if self.tail is None and self.head is not None:
        #     raise Exception(f"Inconsistent insert : {node=}")

    def put(self, key: int, value: int) -> None:
        # print(f"Put {key=}, {value=}")
        # print("Before add")
        # self.print()
        node = self.nodes[key]
        self.delete(node)
        node.val = value
        self.insert(node)

        # print("After add")
        # self.print()
        if self.len > self.cap:
            self.delete(self.head)
        # print("After delete")
        # self.print()

    def print(self):
        node = self.head
        while node is not None:
            sys.stdout.write(f"{node.val} -> ")
            node = node.next
        print(f"End, {self.len=}")


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)