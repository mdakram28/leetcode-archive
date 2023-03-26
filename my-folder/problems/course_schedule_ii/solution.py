from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = [False] * numCourses
        taken = [False] * numCourses
        starts = set(range(numCourses))

        edges = defaultdict(list)
        for f, t in prerequisites:
            edges[f].append(t)
            # print(f"{t=}, {starts=}")
            starts.discard(t)

        path = []
        def travel_append(node):
            if taken[node]:
                return
            for next_node in edges[node]:
                travel_append(next_node)
            taken[node] = True
            path.append(node)

        def travel_check(node):
            if visiting[node]:
                return False
            if taken[node]:
                return True
            visiting[node] = True
            for next_node in edges[node]:
                if not travel_check(next_node):
                    return False
            taken[node] = True
            visiting[node] = False
            return True
        
        for node in range(numCourses):
            if not travel_check(node):
                return []
        taken = [False] * numCourses
        # print(f"{starts=}")
        for node in starts:
            travel_append(node)

        return path