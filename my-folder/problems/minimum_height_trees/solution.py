from queue import Queue

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        children = defaultdict(set)

        if len(edges) == 0:
            return [0]

        for n1, n2 in edges:
            children[n1].add(n2)
            children[n2].add(n1)
        
        to_remove = []
        while len(children) > 2:
            to_remove.clear()
            for node, node_children in children.items():
                if len(node_children) == 1:
                    to_remove.append(node)
            for node in to_remove:
                for child in children[node]:
                    children[child].remove(node)
                del children[node]

        return list(children.keys())