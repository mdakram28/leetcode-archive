class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = [False] * n
        roots = set(range(n))

        for num in chain(leftChild, rightChild):
            if num == -1: continue
            if num in roots:
                roots.remove(num)
            else:
                return False
        
        if len(roots) != 1:
            return False

        q = list(roots)
        for at in q:
            if visited[at]:
                return False
            visited[at] = True
            if leftChild[at] >= 0:
                q.append(leftChild[at])
            if rightChild[at] >= 0:
                q.append(rightChild[at])
        
        return len(q) == n