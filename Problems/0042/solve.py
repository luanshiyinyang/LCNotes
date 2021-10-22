class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftmax, rightmax = 0, 0
        count = 0
        while left < right:
            leftmax = max(height[left], leftmax)
            rightmax = max(height[right], rightmax)
            if height[left] < height[right]:
                count += (leftmax - height[left])
                left += 1
            else:
                count += (rightmax - height[right])
                right -= 1
        return count