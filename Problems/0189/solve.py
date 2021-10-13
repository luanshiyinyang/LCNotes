class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        count = 0
        start = 0
        while count < n:

            current = start
            pre = nums[current]
            
            while True:
                next_index = (current + k) % n
                temp = nums[next_index]
                nums[next_index] = pre
                current = next_index
                pre = temp
                count += 1
                if start == current:
                    break
                
            start += 1