class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        arr.append(0)
        left_spans = [0]*n
        # right_spans = [0]*n
        st = [-1]
        mod = 10**9 + 7

        for i in range(n):
            while arr[st[-1]] >= arr[i]:
                st.pop()
            left_spans[i] = i-st[-1]
            st.append(i)
        
        st.clear()
        st.append(n)
        ret = 0
        for i in range(n-1, -1, -1):
            while arr[st[-1]] > arr[i]:
                st.pop()
            # right_spans[i] = st[-1]-i
            ret = (ret + left_spans[i]*(st[-1]-i)*arr[i]) % mod
            st.append(i)

        # print(left_spans, right_spans)

        return ret