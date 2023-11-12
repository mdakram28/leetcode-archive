class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        ans = set()
        access_times.sort(key=lambda a: a[1])
        
        for i in range(len(access_times)):
            h = int(access_times[i][1][:2])
            m = int(access_times[i][1][2:])
            access_times[i][1] = h*60+m
        
        def is_ha(name):
            times = [t for n, t in access_times if n == name]
            for i in range(2, len(times)):
                if times[i]-times[i-2] < 60:
                    return True
            return False
        
        for name in set(name for name, time in access_times):
            if is_ha(name):
                ans.add(name)
        
        return ans