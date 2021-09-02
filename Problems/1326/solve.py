class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        lines = []
        for i in range(len(ranges)):
            lines.append([i - ranges[i], i + ranges[i]])
        left, count = 0, 0
        while left < n:
            right = 0
            for i, j in lines:
                if i <= left and j > right:
                    right = j
            if right > left:
                count += 1
                left = right
            else:
                count = -1
                break
        return count