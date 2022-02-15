class Solution:
    def reversePairs1(self, nums: list[int]) -> int:
        temp = [0] * len(nums)
        def guibing(l, r):
            if l >= r: return 0
            mid = (l + r) // 2
            ans = guibing(l, mid) + guibing(mid + 1, r)
            temp[l:r + 1] = nums[l:r + 1]
            i, j = l, mid + 1
            for k in range(l, r + 1):
                if i == mid + 1:
                    nums[k] = temp[j]
                    j += 1
                elif j == r + 1 or temp[i] <= temp[j]:
                    nums[k] = temp[i]
                    i += 1
                else:
                    nums[k] = temp[j]
                    j += 1
                    ans += mid - i + 1
            return ans

        return guibing(0, len(nums) - 1)

    
    def reversePairs2(self, nums: list[int]) -> int:
        class FenwickTree:
            def __init__(self, n):
                self.size = n
                self.tree = [0 for _ in range(n + 1)]

            def __lowbit(self, index):
                return index & (-index)

            # 单点更新：将 index 这个位置 + 1
            def update(self, index, delta):
                # 从下到上，最多到 size，可以等于 size
                while index <= self.size:
                    self.tree[index] += delta
                    index += self.__lowbit(index)

            # 区间查询：查询小于等于 index 的元素个数
            # 查询的语义是"前缀和"
            def query(self, index):
                res = 0
                # 从上到下，最少到 1，可以等于 1
                while index > 0:
                    res += self.tree[index]
                    index -= self.__lowbit(index)
                return res
        size = len(nums)
        if size == 0 or size == 1: return 0
        # 去重
        s = list(set(nums))
        len_s = len(s)
        import heapq
        heapq.heapify(s)
        rank_map = dict()
        rank = 1
        for _ in range(len_s):
            num = heapq.heappop(s)
            rank_map[num] = rank
            rank += 1
        fenwick_tree = FenwickTree(len_s)
        res = 0
        # 从后向前填表
        for index in range(size - 1, -1, -1):
            # 1、查询排名
            rank = rank_map[nums[index]]
            # 2、在树状数组排名的那个位置 + 1
            fenwick_tree.update(rank, 1)
            # 3、查询一下小于等于“当前排名 - 1”的元素有多少
            res += fenwick_tree.query(rank - 1)
        return res