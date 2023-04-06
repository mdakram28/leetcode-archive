class Node:
    def __init__(self, val, nxt=None):
        self.val = val
        self.next = nxt


class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        node = self.head
        for i in range(index):
            node = node.next
        return node.val

    def addAtHead(self, val: int) -> None:
        self.head = Node(val, self.head)
        if self.length == 0:
            self.tail = self.head
        self.length += 1


    def addAtTail(self, val: int) -> None:
        if self.length == 0:
            self.tail = self.head = Node(val)
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
        self.length += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.length:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.length:
            self.addAtTail(val)
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            prev.next = Node(val, prev.next)
            self.length += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return
        if self.length == 1:
            self.head = self.tail = None
            self.length -= 1
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
        else:
            prev = self.head
            for i in range(index-1):
                prev = prev.next
            prev.next = prev.next.next
            if index == self.length-1:
                self.tail = prev
            self.length -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)