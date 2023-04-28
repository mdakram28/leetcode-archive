class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], prices: List[int]) -> int:
        graph = [[] for _ in range(n)]
        
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        final_ans = 0
        
        def dfs(at, p):
            nonlocal final_ans
            if len(graph[at]) == 1:
                return prices[at], 0

            ans_leaf = 0
            ans_non_leaf = 0

            leafg_to = None
            nonleafg_to = None
            leaf1, leaf2 = 0, 0
            non_leaf1, non_leaf2 = 0, 0
            
            for to in graph[at]:
                if to == p:
                    continue
                leaf, non_leaf = dfs(to, at)
                ans_leaf = max(leaf, ans_leaf)
                ans_non_leaf = max(non_leaf, ans_non_leaf)
                
                if leaf > leaf1:
                    leaf1, leaf2 = leaf, leaf1
                    leafg_to = to
                elif leaf > leaf2:
                    leaf2 = leaf
                
                if non_leaf > non_leaf1:
                    non_leaf1, non_leaf2 = non_leaf, non_leaf1
                    nonleafg_to = to
                elif non_leaf > non_leaf2:
                    non_leaf2 = non_leaf

            # print()
            # if len(graph[at]) > 2 or p is None:
            if leafg_to != nonleafg_to:
                final_ans = max(final_ans, leaf1 + non_leaf1 + prices[at])
            else:
                final_ans = max(final_ans,
                    leaf1 + non_leaf2 + prices[at],
                    leaf2 + non_leaf1 + prices[at]
                )
            print(f"{at=}, {ans_leaf=}, {ans_non_leaf=}")
            return ans_leaf+prices[at], ans_non_leaf+prices[at]
        
        if n == 1: return 0
        elif n == 2: return max(prices)

        for i in range(n):
            if len(graph[i]) > 1:
                dfs(i, None)
                break
        return final_ans
        