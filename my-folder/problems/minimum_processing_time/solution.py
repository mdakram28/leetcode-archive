class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort(reverse=True)
        return max(t+tasks[i*4+3] for i, t in enumerate(processorTime))