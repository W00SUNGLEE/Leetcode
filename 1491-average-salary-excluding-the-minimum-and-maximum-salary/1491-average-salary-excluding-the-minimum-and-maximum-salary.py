import statistics

class Solution:
    def average(self, salary: List[int]) -> float:
        del salary[salary.index(max(salary))]
        del salary[salary.index(min(salary))]
        
        return statistics.mean(salary)