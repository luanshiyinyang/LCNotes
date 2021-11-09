class Solution:
    def minDeletions(self, s: str) -> int:
        stats = list(collections.Counter(s).values())
        res = 0
        for i in range(len(stats)):
            while stats[i] > 0 and stats[i] in stats[:i] + stats[i+1:]:
                stats[i] -= 1
                res += 1
        return res