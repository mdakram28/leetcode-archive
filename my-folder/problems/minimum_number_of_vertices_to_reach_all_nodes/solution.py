class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:   
        xfrom = {i for i, n in edges}
        xto = {n for i, n in edges}
        return xfrom - xto
        # return list({i for i, n in edges if i not in [n for i, n in edges]})