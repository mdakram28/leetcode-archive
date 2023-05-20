class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max_dur = 0
        max_id = None
        
        start_time = 0
        for curr_id, end_time in logs:
            dur = end_time - start_time
            if dur > max_dur:
                max_dur = dur
                max_id = curr_id
            elif dur == max_dur and curr_id < max_id:
                max_id = curr_id
            start_time = end_time
        
        return max_id