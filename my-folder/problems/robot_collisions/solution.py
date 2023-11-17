class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = list(zip(positions, range(len(positions)), healths, directions))
        robots.sort()

        st = []
        for _,i,_,d in robots:
            st.append((i,d))
            while len(st) > 1 and st[-1][1] == 'L' and st[-2][1] == 'R':
                il, dl = st.pop()
                ir, dr = st.pop()
                if healths[il] > healths[ir]:
                    healths[il] -= 1
                    st.append((il, dl))
                elif healths[il] < healths[ir]:
                    healths[ir] -= 1
                    st.append((ir, dr))
        st.sort()
        return [healths[i] for i, _ in st]