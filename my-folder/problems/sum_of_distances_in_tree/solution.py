class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        children = [[] for i in range(n)]
        for n1, n2 in edges:
            children[n2].append(n1)
            children[n1].append(n2)
        
        sum_dist = [0]*n
        num_nodes = [1]*n
        def calc_child_sum(at, p):
            child_sum = 0
            child_count = 1
            for to in children[at]:
                if to == p:
                    continue
                calc_child_sum(to, at)
                child_sum += sum_dist[to] + num_nodes[to]
                child_count += num_nodes[to]
            sum_dist[at] = child_sum
            num_nodes[at] = child_count
        
        def add_parent_sum(at, p):
            sum_dist[at] += sum_dist[p] - sum_dist[at] - num_nodes[at] + total_nodes - num_nodes[at]
            for to in children[at]:
                if to == p:
                    continue
                add_parent_sum(to, at)
        
        calc_child_sum(0, -1)
        total_nodes = num_nodes[0]
        for to in children[0]:
            add_parent_sum(to, 0)
        
        return sum_dist