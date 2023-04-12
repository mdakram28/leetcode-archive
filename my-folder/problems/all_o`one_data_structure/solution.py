class Node:
    def __init__(self, val, prev=None, next = None):
        self.val = val
        self.next = next
        self.prev = prev
    
    def remove(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.next = self.prev = None

inf = float('inf')

class AllOne:

    def __init__(self):
        # Node((freq, {key: True}))
        self.freq_head = Node({})
        self.freq_tail = Node({})
        self.freq_head.next = self.freq_tail
        self.freq_tail.prev = self.freq_head
        self.freq_nodes = {
            0: self.freq_head,
            inf: self.freq_tail,
        }

        self.keys_freq = collections.defaultdict(int)
    
    def print_ll(self):
        node = self.freq_head
        while node:
            print(str(node.val) + " -> ", end='')
            node = node.next
        print("END")

    def inc(self, key: str) -> None:
        # Get and update freq
        freq = self.keys_freq[key]
        self.keys_freq[key] = freq+1
        freq_node = self.freq_nodes[freq]
        next_freq_node = self.freq_nodes.get(freq+1)

        # Add next frequency node if required
        if not next_freq_node:
            self.freq_nodes[freq+1] = next_freq_node = Node({}, freq_node, freq_node.next)
            freq_node.next = next_freq_node
            next_freq_node.next.prev = next_freq_node
            if self.freq_tail == freq_node:
                self.freq_tail = next_freq_node
        
        # Add key to next frequency node
        next_freq_node.val[key] = True

        if freq > 0:
            # Remove key from previous freq node
            del freq_node.val[key]
            # Remove previous frequency node if required
            if len(freq_node.val) == 0:
                freq_node.remove()
                del self.freq_nodes[freq]
                if self.freq_head == freq_node:
                    self.freq_head = next_freq_node

    def dec(self, key: str) -> None:
        # Get and update freq
        freq = self.keys_freq[key]
        self.keys_freq[key] = freq-1
        freq_node = self.freq_nodes[freq]
        prev_freq_node = self.freq_nodes.get(freq-1)

        # Add prev freq node is required
        if not prev_freq_node:
            prev_freq_node = self.freq_nodes[freq-1] = Node({}, freq_node.prev, freq_node)
            freq_node.prev = prev_freq_node
            prev_freq_node.prev.next = prev_freq_node
            if self.freq_head == freq_node:
                eslf.freq_head = prev_freq_head
        
        if freq > 1:
            # Add key to prev freq node
            prev_freq_node.val[key] = True
        
        # Remove key from freq node
        del freq_node.val[key]
        if len(freq_node.val) == 0:
            freq_node.remove()
            del self.freq_nodes[freq]
            if self.freq_tail == freq_node:
                self.freq_tail = prev_freq_node

    def getMaxKey(self) -> str:
        vals = self.freq_tail.prev.val
        return next(iter(vals.keys())) if vals else ""

    def getMinKey(self) -> str:
        vals = self.freq_head.next.val
        return next(iter(vals.keys())) if vals else ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()