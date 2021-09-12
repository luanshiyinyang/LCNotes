class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x: (x[1] - x[0]))
        res = 0
        for cost, threshold in tasks:
            res = max(res + cost, threshold)
        return res