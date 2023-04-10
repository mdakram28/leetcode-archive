class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def __repr__(self):
        return str(self.val)

class NodeList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def empty(self):
        return not self.head
    
    def insert_head(self, node):
        if self.empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        node.prev = None
    
    def insert_tail(self, node):
        if self.empty():
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        node.next = None
    
    def insert_after(self, node, n2):
        if node == self.tail:
            self.insert_tail(n2)
        else:
            n2.next = node.next
            n2.prev = node
            node.next.prev = n2
            node.next = n2
    
    def remove_head(self):
        rem = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        rem.next = None
        rem.prev = None
    
    def remove_tail(self):
        rem = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        rem.next = None
        rem.prev = None

    def remove(self, node):
        if node == self.head:
            self.remove_head()
        elif node == self.tail:
            self.remove_tail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next = None
            node.prev = None

    def __repr__(self):
        ret = "["
        node = self.head
        while node:
            ret += str(node) + ' -> '
            node = node.next
        ret += 'END]'
        return ret

    def print(self):
        node = self.head
        print('\n---HEAD---')
        while node:
            print(node)
            node = node.next
        print('---TAIL---\n')

class LFUCache:

    def __init__(self, capacity: int):
        self.f = NodeList()
        self.nodes = {}
        self.freq_nodes = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        # print(f"get({key=})")
        if key in self.nodes:
            self.increment_freq(key)
            # self.f.print()
            return self.nodes[key].val[1]
        else:
            # self.f.print()
            return -1

    def put(self, key: int, value: int) -> None:
        # print(f"put({key=}, {value=})")
        if key in self.nodes:
            self.increment_freq(key)
            self.nodes[key].val = (key, value)
            # self.f.print()

            return

        if len(self.nodes) == self.cap:
            # print(f"Capacity reached {len(self.nodes)}")
            self.remove_lfu()

        if self.f.empty() or self.f.head.val[0] != 1:
            self.f.insert_head(Node((1, NodeList())))
        freq_node = self.f.head
        self.nodes[key] = Node((key, value))
        self.freq_nodes[key] = freq_node
        freq_node.val[1].insert_tail(self.nodes[key])
        # print("After inserting", self.nodes)
        # self.f.print()
    
    def increment_freq(self, key):
        freq_node = self.freq_nodes[key]
        node = self.nodes[key]
        freq_node.val[1].remove(node)
        new_count = freq_node.val[0]+1
        
        if freq_node.next is None or freq_node.next.val[0] != new_count:
            self.f.insert_after(freq_node, Node((new_count, NodeList())))
        
        next_freq_node = freq_node.next
        if freq_node.val[1].empty():
            self.f.remove(freq_node)
        
        next_freq_node.val[1].insert_tail(node)

        self.freq_nodes[key] = next_freq_node

    def remove_lfu(self):
        freq_node = self.f.head
        node = freq_node.val[1].head
        del self.nodes[node.val[0]]
        del self.freq_nodes[node.val[0]]
        freq_node.val[1].remove_head()
        if freq_node.val[1].empty():
            self.f.remove_head()

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)