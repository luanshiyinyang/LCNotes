class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def count_groups(mid):
            temp, count = 0, 1  # count表示组数，从1开始，因为无论如何都有一组
            for num in nums:
                temp += num
                if temp > mid:
                    count += 1
                    temp = num
            return count
        
        left, right = max(nums), sum(nums)  # 定义边界
        while left < right:
            mid = (left + right) // 2
            num_g = count_groups(mid)
            if num_g > m:
                # mid过小
                left = mid + 1
            else:
                # mid 过大
                right = mid
        return left
        