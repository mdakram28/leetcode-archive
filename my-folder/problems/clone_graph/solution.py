"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_cache = {}
        q = [node]

        for orig_node in q:
            if orig_node is None or orig_node.val in node_cache:
                pass
            else:
                print(f"Creating node {orig_node.val}")
                new_node = Node(orig_node.val, [])
                node_cache[orig_node.val] = new_node
                for orig_neighbor in orig_node.neighbors:
                    if orig_neighbor.val in node_cache:
                        new_neighbor = node_cache[orig_neighbor.val]
                        new_neighbor.neighbors.append(new_node)
                        if new_neighbor != new_node:
                            new_node.neighbors.append(new_neighbor)
                    else:
                        q.append(orig_neighbor)
        return node_cache[node.val] if node is not None else None
