class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        
        score = {}
        
        for word in positive_feedback:
            score[word] = 3
        
        for word in negative_feedback:
            score[word] = -1
        
        scores = [(sum(score.get(word, 0) for word in report.split(" ")), -id) for id, report in zip(student_id, report)]
        scores.sort(reverse=True)
        # print(scores[:k])
        return [-id for s, id in scores[:k]]
            