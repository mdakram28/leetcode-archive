class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        return chain.from_iterable(("Push", "Pop")*(n-p-1)+("Push",) for p, n in pairwise(chain((0,),target)))