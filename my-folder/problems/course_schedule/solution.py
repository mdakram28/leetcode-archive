class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        children = [[] for _ in range(numCourses)]
        for node, child in prerequisites:
            children[node].append(child)
        
        visiting = [False] * numCourses
        satisfied = [False] * numCourses
        def check_children(node: int):
            if satisfied[node]:
                return True
            if visiting[node]:
                return False
            visiting[node] = True
            for child in children[node]:
                if not check_children(child):
                    return False
            satisfied[node] = True
            visiting[node] = False

            return True
        
        return all(map(check_children, range(numCourses)))
