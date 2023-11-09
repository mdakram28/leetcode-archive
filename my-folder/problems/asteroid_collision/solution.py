class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for num in asteroids:
            st.append(num)

            while len(st) > 1 and st[-1]<0 and st[-2]>0:
                if st[-2] == -st[-1]:
                    st.pop()
                    st.pop()
                elif st[-2] < -st[-1]:
                    st[-2] = st[-1]
                    st.pop()
                else:
                    st.pop()
        
        return st
                    