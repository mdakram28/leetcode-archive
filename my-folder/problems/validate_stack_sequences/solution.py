class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = [-1]
        i = 0
        j = 0
        n = len(pushed)

        while i<n:
            while st[-1] != popped[j] and i < n:
                st.append(pushed[i])
                i += 1

            while j < n and st[-1] == popped[j]:
                st.pop()
                j += 1
        
        return j == n