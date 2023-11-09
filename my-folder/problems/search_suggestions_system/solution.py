class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        l = 0
        r = len(products)

        ans = []
        for i, c in enumerate(searchWord):
            while l<r and (len(products[l]) <= i or products[l][i] != c):
                l += 1
            while l<r and(len(products[r-1]) <= i or products[r-1][i] != c):
                r -= 1
            ans.append(products[l:min(r, l+3)])
        return ans
