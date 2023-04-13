"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, nodes: List['Employee'], find_id: int) -> int:
        node_by_id = {}
        for node in nodes:
            node_by_id[node.id] = node
        
        find_node = next(filter(lambda node: node.id == find_id,nodes))

        def dfs(node):
            return node.importance + sum(dfs(node_by_id[child]) for child in node.subordinates)
            
        return dfs(find_node)