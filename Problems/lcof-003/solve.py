class Solution:
    def findRepeatNumber1(self, nums: List[int]) -> int:
        re = []
        for n in nums:
            if n in re:
                return n
            else:
                re.append(n)
        return -1
    
    def findRepeatNumber2(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while i != nums[i]:
                temp = nums[i]
                if temp == nums[temp]:
                    return temp
                t = nums[temp]
                nums[temp] = temp
                nums[i] = t
        return -1