class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 升序排序线段列表
        intervals.sort(key=lambda x: x[0])
        # 创建合并后的结果
        merged = []
        for interval in intervals:
            # 无需合并
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # 需要合并
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged