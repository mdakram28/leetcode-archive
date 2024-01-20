from sortedcontainers import SortedList

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        mod = (10**9+7)
        arr.append(-float('inf'))

        st = [n]
        next_i = [0]*n
        for i in range(n-1, -1, -1):
            while arr[st[-1]] >= arr[i]:
                st.pop()
            
            next_i[i] = st[-1]
            st.append(i)
        
        st = [-1]
        total = 0
        for i in range(n):
            while arr[st[-1]] > arr[i]:
                st.pop()
            
            total = (total + arr[i]*(i-st[-1])*(next_i[i]-i))%mod

            st.append(i)
        
        return total
