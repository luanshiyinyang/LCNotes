import functools

# 题目2
class Solution2:
    def singleNumbers(self, nums: list[int]) -> list[int]:
        ret = functools.reduce(lambda x, y : x ^ y, nums) # 将nums中的每一个元素都进行异或操作：a ^ b ^ c ^ ... 
        div = 1
        while div & ret == 0:
            div <<= 1 # 这里找的是最右边一个“1”，任意一个“1”都行
        a, b = 0, 0
        for n in nums:
            if n & div:
                a ^= n
            else:
                b ^= n
        return [a, b]

# 题目3
class Solution3:
    def singleNumber(self, nums: list[int]) -> int:
        q, p = 0, 0
        for num in nums:
            q = q ^ num & ~p
            p = p ^ num & ~q
        return q