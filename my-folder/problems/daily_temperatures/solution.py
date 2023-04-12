class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st = []
        for i in range(len(temp)-1, -1, -1):
            while st and temp[st[-1]]&0xFF <= temp[i]&0xFF:
                st.pop()
            temp[i] |= (st[-1] - i if st else 0) << 8
            st.append(i)

        for i in range(len(temp)):
            temp[i] >>= 8
        return temp