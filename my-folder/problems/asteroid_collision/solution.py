class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for num in asteroids:
            if num > 0:
                st.append(num)
            else:
                val = abs(num)
                while st and st[-1] > 0 and st[-1] < val:
                    st.pop()
                if st and st[-1] == val:
                    st.pop()
                elif not st or st[-1] < 0:
                    st.append(num)
        return st